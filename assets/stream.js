/* The live, public "Stream Of Consciousness" feed off the Off The Dome
   planet. Anyone who opens this page watches it update in real time.
   Only the site owner (signed in with the Firebase account set up for
   this) can post — enforced by the database's security rules, not by
   anything in this file, so there is nothing secret to protect here. */

const firebaseConfig = {
  apiKey: "AIzaSyB40pjOpCT6brtZ9-PUuTv7pw3VTPxaHI4",
  authDomain: "written-from-the-hip.firebaseapp.com",
  databaseURL: "https://written-from-the-hip-default-rtdb.firebaseio.com",
  projectId: "written-from-the-hip",
  storageBucket: "written-from-the-hip.firebasestorage.app",
  messagingSenderId: "791285249884",
  appId: "1:791285249884:web:cd7af802e4852e57c5b399",
};

firebase.initializeApp(firebaseConfig);
const streamAuth = firebase.auth();
const streamDb = firebase.database();

document.getElementById("stream").innerHTML =
  planetNavHTML() +
  topbarHTML("Stream Of Consciousness — updates live") +
  '<div class="stream-feed" id="streamFeed"><div class="stream-empty">Loading the feed…</div></div>' +
  '<div class="stream-composer">' +
  '<a href="#" id="streamSignInLink" class="stream-signin-link">sign in</a>' +
  '<form id="streamLoginForm" class="stream-login" hidden>' +
  '<input type="email" id="streamEmail" placeholder="email" autocomplete="username">' +
  '<input type="password" id="streamPassword" placeholder="password" autocomplete="current-password">' +
  '<button type="submit">Sign In</button>' +
  "</form>" +
  '<form id="streamPostForm" class="stream-post" hidden>' +
  '<textarea id="streamText" placeholder="What art thou is steamith of your consciousness brethren?" rows="1"></textarea>' +
  '<button type="submit">Transmit</button>' +
  "</form>" +
  '<a href="#" id="streamSignOutLink" class="stream-signin-link" hidden>sign out</a>' +
  '<div class="stream-status" id="streamStatus"></div>' +
  "</div>" +
  legalHTML("page-legal");

const feedEl = document.getElementById("streamFeed");
const signInLinkEl = document.getElementById("streamSignInLink");
const signOutLinkEl = document.getElementById("streamSignOutLink");
const loginFormEl = document.getElementById("streamLoginForm");
const postFormEl = document.getElementById("streamPostForm");
const emailEl = document.getElementById("streamEmail");
const passwordEl = document.getElementById("streamPassword");
const textEl = document.getElementById("streamText");
const statusEl = document.getElementById("streamStatus");

function setStatus(msg, kind) {
  statusEl.textContent = msg || "";
  statusEl.className = "stream-status" + (kind ? " " + kind : "");
}

function fmtTime(ms) {
  const d = new Date(ms);
  return d.toLocaleString(undefined, {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

function renderEntries(list) {
  if (!list.length) {
    feedEl.innerHTML = '<div class="stream-empty">Nothing up there yet. First thought wins.</div>';
    return;
  }
  const atBottom = feedEl.scrollHeight - feedEl.scrollTop - feedEl.clientHeight < 60;
  feedEl.innerHTML = list
    .map(
      (e) =>
        '<div class="stream-entry"><time>' +
        fmtTime(e.postedAt) +
        "</time><p>" +
        esc(e.text) +
        "</p></div>"
    )
    .join("");
  if (atBottom) feedEl.scrollTop = feedEl.scrollHeight;
}

streamDb
  .ref("stream/entries")
  .orderByChild("postedAt")
  .limitToLast(200)
  .on(
    "value",
    (snap) => {
      const val = snap.val() || {};
      const list = Object.keys(val)
        .map((k) => val[k])
        .sort((a, b) => (a.postedAt || 0) - (b.postedAt || 0));
      renderEntries(list);
    },
    () => {
      feedEl.innerHTML = '<div class="stream-empty">Couldn’t reach the feed. Reload to try again.</div>';
    }
  );

streamAuth.onAuthStateChanged((user) => {
  const isOwner = !!user;
  signInLinkEl.hidden = isOwner;
  signOutLinkEl.hidden = !isOwner;
  loginFormEl.hidden = true;
  postFormEl.hidden = !isOwner;
  if (user) setStatus("Signed in.", "ok");
});

signInLinkEl.addEventListener("click", (e) => {
  e.preventDefault();
  signInLinkEl.hidden = true;
  loginFormEl.hidden = false;
});

signOutLinkEl.addEventListener("click", (e) => {
  e.preventDefault();
  streamAuth.signOut();
  setStatus("Signed out.");
});

loginFormEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  setStatus("Signing in…");
  try {
    await streamAuth.signInWithEmailAndPassword(emailEl.value, passwordEl.value);
    setStatus("");
  } catch (err) {
    setStatus("Sign-in failed.", "error");
  }
});

postFormEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = textEl.value.trim();
  if (!text) return;
  const btn = postFormEl.querySelector("button");
  btn.disabled = true;
  setStatus("Sending…");
  try {
    await streamDb.ref("stream/entries").push({
      text: text,
      postedAt: firebase.database.ServerValue.TIMESTAMP,
    });
    textEl.value = "";
    textEl.style.height = "auto";
    setStatus("Posted.", "ok");
    setTimeout(() => setStatus(""), 2000);
  } catch (err) {
    setStatus("Couldn't post that — try again.", "error");
  } finally {
    btn.disabled = false;
  }
});

textEl.addEventListener("input", () => {
  textEl.style.height = "auto";
  textEl.style.height = Math.min(textEl.scrollHeight, 140) + "px";
});

textEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    postFormEl.requestSubmit();
  }
});
