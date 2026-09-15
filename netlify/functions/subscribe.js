/* Adds an email to the Resend Audience used for "Join The WFTH Family"
   notifications. This runs server-side (on Netlify) specifically so the
   Resend API key never reaches the browser -- calling Resend directly from
   client-side JS would expose the key to anyone viewing the page source.

   Requires two environment variables, set in the Netlify site's
   Environment variables settings (never committed to the repo):
     RESEND_API_KEY      the API key from the Resend dashboard
     RESEND_AUDIENCE_ID  the id of the Audience contacts should join
*/

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

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

    return { statusCode: 200, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    return { statusCode: 502, body: JSON.stringify({ error: "Couldn't reach Resend." }) };
  }
};
