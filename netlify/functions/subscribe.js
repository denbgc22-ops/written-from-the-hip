/* Adds an email to the Resend Audience used for "Join The WFTH Family"
   notifications, then sends that address a one-time welcome email. This
   runs server-side (on Netlify) specifically so the Resend API key never
   reaches the browser -- calling Resend directly from client-side JS would
   expose the key to anyone viewing the page source.

   Requires two environment variables, set in the Netlify site's
   Environment variables settings (never committed to the repo):
     RESEND_API_KEY      the API key from the Resend dashboard
     RESEND_AUDIENCE_ID  the id of the Audience contacts should join

   Sending the welcome email itself needs writtenfromthehip.com verified
   as a sending domain in Resend (Domains tab) -- until then, Resend only
   allows delivery to the account's own address, not real subscribers.
*/

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const WELCOME_FROM = "Denby and Bolt <hello@writtenfromthehip.com>";
const WELCOME_SUBJECT = "We Are Now On Ur Dome 4Life";
const WELCOME_BODY = `yo.

You are officially an "off the domer."

grats.

We will now send you our unsolicited, unforgivable, terrible, no-good writing and ideas to this very email.

Love,
Denby and Bolt`;

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ error: "Method not allowed." }) };
  }

  let email;
  try {
    email = (JSON.parse(event.body || "{}").email || "").trim();
  } catch (err) {
    return { statusCode: 400, body: JSON.stringify({ error: "Invalid request." }) };
  }

  if (!EMAIL_RE.test(email)) {
    return { statusCode: 400, body: JSON.stringify({ error: "Please enter a valid email address." }) };
  }

  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;
  if (!apiKey || !audienceId) {
    return { statusCode: 500, body: JSON.stringify({ error: "Subscribe isn't configured yet." }) };
  }

  try {
    const resendRes = await fetch(`https://api.resend.com/audiences/${audienceId}/contacts`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, unsubscribed: false }),
    });

    // Resend returns 409 when the contact already exists -- that's still a
    // successful "you're subscribed" outcome from the visitor's side.
    if (!resendRes.ok && resendRes.status !== 409) {
      return { statusCode: 502, body: JSON.stringify({ error: "Resend rejected the request." }) };
    }

    // Best-effort: a subscriber is still successfully saved even if the
    // welcome email fails to send (e.g. the domain isn't verified yet).
    try {
      await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          from: WELCOME_FROM,
          to: email,
          subject: WELCOME_SUBJECT,
          text: WELCOME_BODY,
        }),
      });
    } catch (err) {
      // ignored -- see comment above
    }

    return { statusCode: 200, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    return { statusCode: 502, body: JSON.stringify({ error: "Couldn't reach Resend." }) };
  }
};
