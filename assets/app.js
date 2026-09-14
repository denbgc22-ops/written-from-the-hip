/* Builds every page out of config.js. You shouldn't need to edit this file. */

const esc = (s) =>
  String(s == null ? "" : s).replace(
    /[&<>"']/g,
    (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m])
  );

const planetHref = (p) => p.href || "page.html?p=" + encodeURIComponent(p.id);
const findPlanet = (id) => SITE.planets.filter((p) => p.id === id)[0];
const findScript = (id) => (SITE.scripts || []).filter((s) => s.id === id)[0];
const findBio = (id) => (SITE.bios || []).filter((b) => b.id === id)[0];

/* Renders a label with each letter sized on a curve: smallest at the two
   ends, growing to the biggest letter in the middle. minSize/maxSize are in px. */
function arcLabel(name, minSize, maxSize) {
  const chars = String(name == null ? "" : name).split("");
  const n = chars.length;
  const center = (n - 1) / 2;
  return chars
    .map(function (ch, i) {
      const dist = center === 0 ? 0 : Math.abs(i - center) / center; // 0 = middle, 1 = ends
      const size = maxSize - (maxSize - minSize) * dist;
      return (
        '<span style="font-size:' +
        size.toFixed(1) +
        'px">' +
        esc(ch === " " ? " " : ch) +
        "</span>"
      );
    })
    .join("");
}

function legalHTML(cls) {
  return '<div class="legal ' + (cls || "") + '">' + esc(SITE.legal) + "</div>";
}

/* the top bar every sub page shares: the corner moon (marked "WFTH") that
   links home, plus an optional ribbon line of text next to it */
function topbarHTML(ribbonText) {
  return (
    '<div class="topbar">' +
    '<a class="corner" href="index.html" title="Home">' +
    '<span class="corner-moon">' +
    '<img src="assets/images/moon.png" alt="Home">' +
    '<span class="corner-mark">WFTH</span>' +
    "</span></a>" +
    '<div class="rule">' +
    (ribbonText ? '<span class="ribbon-text">' + esc(ribbonText) + "</span>" : "") +
    "</div></div>"
  );
}

/* the vertical list of every planet down the left edge of a sub page, so
   you can jump straight from one planet to another */
function planetNavHTML() {
  return (
    '<nav class="planet-nav" aria-label="Planets">' +
    SITE.planets
      .map(
        (p) =>
          '<a href="' +
          esc(planetHref(p)) +
          '">' +
          planetSVG(p.art, 30) +
          "<span>" +
          esc(p.name) +
          "</span></a>"
      )
      .join("") +
    "</nav>"
  );
}

function moonHTML(size) {
  // shrink the title until it fits the disc on one line, whatever it says
  const fs = Math.min(size * 0.115, (size * 0.78) / (0.60 * Math.max(SITE.title.length, 1)));
  return (
    '<div class="moon" style="width:' +
    size +
    "px;height:" +
    size +
    'px">' +
    '<img src="assets/images/moon.png" alt="' +
    esc(SITE.title) +
    '">' +
    '<div class="moon-text">' +
    '<div class="moon-title" style="font-size:' +
    fs.toFixed(1) +
    'px">' +
    esc(SITE.title) +
    "</div>" +
    (SITE.issue
      ? '<div class="moon-issue" style="font-size:' +
        (fs * 0.8).toFixed(1) +
        "px;margin-top:" +
        (size * 0.09).toFixed(0) +
        'px">' +
        esc(SITE.issue) +
        "</div>"
      : "") +
    "</div></div>"
  );
}

/* ------------------------------------------------------------------ home -- */

/* the curved pull-quote banner across the top of the home page, text set
   along an SVG arc so it follows the same kind of curve the planets ring
   sits on below it */
function quoteBannerHTML() {
  const q = SITE.pullQuote;
  if (!q || !q.text) return "";
  return (
    '<svg class="quote-svg" viewBox="0 0 1000 170" aria-hidden="true" focusable="false">' +
    "<defs><path id=\"quoteArc\" d=\"M 20 145 A 480 120 0 0 1 980 145\" fill=\"none\"/></defs>" +
    '<text class="quote-text"><textPath href="#quoteArc" startOffset="50%" text-anchor="middle">' +
    esc(q.text) +
    "</textPath></text>" +
    (q.attribution
      ? '<text class="quote-attribution" x="500" y="162" text-anchor="middle">' + esc(q.attribution) + "</text>"
      : "") +
    "</svg>"
  );
}

function renderHome() {
  const banner = document.getElementById("quote-banner");
  if (banner) banner.innerHTML = quoteBannerHTML();

  const stage = document.getElementById("stage");
  let html = moonHTML(300);
  SITE.planets.forEach(function (p) {
    html +=
      '<a class="node" href="' +
      esc(planetHref(p)) +
      '" style="left:' +
      p.x +
      "%;top:" +
      p.y +
      '%">' +
      '<span class="label">' +
      arcLabel(p.name, 9, 13) +
      "</span>" +
      planetSVG(p.art, p.size || 54) +
      "</a>";
  });
  stage.innerHTML = html;

  const list = document.getElementById("node-list");
  if (list) {
    list.innerHTML = SITE.planets
      .map(
        (p) =>
          '<a href="' +
          esc(planetHref(p)) +
          '">' +
          planetSVG(p.art, 38) +
          '<span class="label">' +
          arcLabel(p.name, 11, 15) +
          "</span></a>"
      )
      .join("");
  }

  const mm = document.getElementById("mobile-moon");
  if (mm) mm.innerHTML = moonHTML(230);

  const foot = document.getElementById("home-footer");
  if (foot) {
    foot.innerHTML =
      '<div class="row">' +
      SITE.footerLinks
        .map((l) => '<a href="' + esc(l.href) + '">' + esc(l.label) + "</a>")
        .join("") +
      "</div>" +
      legalHTML();
  }

  fitStage();
  window.addEventListener("resize", fitStage);
}

/* scales the star field down so the whole constellation always fits */
function fitStage() {
  const wrap = document.querySelector(".stage-wrap");
  const stage = document.getElementById("stage");
  if (!wrap || !stage) return;
  const scale = Math.min(1, (wrap.clientWidth - 24) / 1000);
  stage.style.transform = "scale(" + scale + ")";
  wrap.style.height = 700 * scale + "px";
}

/* -------------------------------------------------------------- sub page -- */

const LINK_TOP_PAD = 46; // px, before the first link
const LINK_ROW_HEIGHT = 34; // px, vertical space per link
const LINK_BOTTOM_PAD = 30; // px, after the last link

function linkStyle(layout, i, total) {
  if (layout === "left") {
    return "left:22px;top:" + (LINK_TOP_PAD + i * LINK_ROW_HEIGHT) + "px;text-align:left";
  }
  if (layout === "diagonal") {
    return (
      "right:" +
      (14 + i * 3) +
      "%;top:" +
      (16 + i * 14) +
      "%;transform:rotate(-9deg);transform-origin:right center"
    );
  }
  return "right:22px;top:" + (LINK_TOP_PAD + i * LINK_ROW_HEIGHT) + "px;text-align:right";
}

/* panels default to 258px tall; grow it for pages with enough links that
   the fixed row spacing above would otherwise run past the bottom */
function panelHeight(total) {
  return Math.max(258, LINK_TOP_PAD + total * LINK_ROW_HEIGHT + LINK_BOTTOM_PAD);
}

function renderPage() {
  const id = new URLSearchParams(location.search).get("p");
  const p = findPlanet(id);
  if (!p || !p.page) {
    location.replace("index.html");
    return;
  }

  document.title = p.name + " \u2014 " + SITE.title;
  const pg = p.page;
  const panel = pg.panel || {};
  const oval = pg.oval || {};
  const links = pg.links || [];
  const roster = pg.roster || [];

  const linksHTML = links
    .map(
      (l, i) =>
        '<a href="' +
        esc(l.href) +
        '" style="' +
        linkStyle(panel.layout, i, links.length) +
        ";color:" +
        (panel.link || "#ffe14d") +
        (l.wrap
          ? ";white-space:pre-line;display:block;max-width:min(300px, calc(100% - 44px));line-height:1.35;left:50%;transform:translateX(-50%);text-align:center;font-size:19px;text-shadow:2px 3px 3px rgba(0,0,0,0.85),0 0 12px rgba(0,0,0,0.6)"
          : "") +
        '">' +
        esc(l.label) +
        "</a>"
    )
    .join("");

  // A roster page (photo + name, side by side) replaces the usual link list.
  const rosterHTML = roster
    .map(
      (r) =>
        '<a class="roster-half" href="' +
        esc(r.href) +
        '"><img class="roster-photo" src="' +
        esc(r.photo) +
        '" alt="' +
        esc(r.name) +
        '"><span class="roster-name">' +
        esc(r.name) +
        "</span>" +
        (r.height || r.weight
          ? '<span class="roster-meta">' + esc([r.height, r.weight].filter(Boolean).join(" — ")) + "</span>"
          : "") +
        "</a>"
    )
    .join("");

  // An optional pointing photo, e.g. a mascot gesturing at the link above it.
  // Its exact top position is set after render, once we can measure how
  // tall the (possibly wrapped) link text actually came out.
  const POINTER_SIZE = 130;
  const pointerHTML = pg.pointer
    ? '<img class="panel-pointer" src="' + esc(pg.pointer.photo) + '" alt="" style="left:50%;transform:translateX(-50%)">'
    : "";

  const panelInnerHTML = roster.length ? '<div class="roster">' + rosterHTML + "</div>" : linksHTML + pointerHTML;
  const panelH = pg.pointer
    ? 258 // provisional; corrected below once the link's real height is known
    : roster.length
    ? 260
    : panel.layout === "diagonal"
    ? 258
    : panelHeight(links.length);

  document.getElementById("page").innerHTML =
    planetNavHTML() +
    topbarHTML(pg.ribbon) +
    '<div class="billboard">' +
    '<div class="oval" style="background:radial-gradient(circle at 34% 26%, ' +
    tint(oval.fill) +
    ", " +
    (oval.fill || "#1f74c4") +
    ')"><span style="color:' +
    (oval.text || "#ffe14d") +
    '">' +
    esc(p.name) +
    "</span></div>" +
    '<div class="panel" style="height:' +
    panelH +
    "px;background:linear-gradient(160deg, " +
    (panel.from || "#2a6ea8") +
    ", " +
    (panel.to || "#0c2438") +
    ')">' +
    panelInnerHTML +
    "</div></div>" +
    (pg.blurb
      ? '<p class="blurb' + (p.orb ? " has-orb" : "") + '">' + esc(pg.blurb) + "</p>"
      : "") +
    (p.orb
      ? '<a class="orb" href="' + esc(p.orb.href) + '">' + esc(p.orb.label) + "</a>"
      : "") +
    '<a class="backlink" href="index.html">Back to the home page</a>' +
    legalHTML("page-legal");

  if (pg.pointer) {
    const panelEl = document.querySelector(".panel");
    const linkEl = panelEl.querySelector("a");
    const imgEl = panelEl.querySelector(".panel-pointer");
    const gap = pg.pointer.gap != null ? pg.pointer.gap : 24;
    const top = linkEl.offsetTop + linkEl.offsetHeight + gap;
    imgEl.style.top = top + "px";
    panelEl.style.height = top + POINTER_SIZE + 24 + "px";
  }
}

/* lighter version of a hex color, for the oval highlight */
function tint(hex) {
  if (!hex || hex[0] !== "#" || hex.length !== 7) return "#ffffff";
  const n = (i) => Math.min(255, parseInt(hex.substr(i, 2), 16) + 70).toString(16).padStart(2, "0");
  return "#" + n(1) + n(3) + n(5);
}

/* ---------------------------------------------------------------- script -- */

function renderScript() {
  const id = new URLSearchParams(location.search).get("s");
  const s = findScript(id);
  if (!s) {
    location.replace("index.html");
    return;
  }

  document.title = s.title + " — " + SITE.title;
  document.getElementById("script").innerHTML =
    planetNavHTML() +
    topbarHTML() +
    '<h1 class="script-title">' +
    esc(s.title) +
    "</h1>" +
    '<pre class="script-body">' +
    esc(s.body) +
    "</pre>" +
    '<a class="backlink" href="page.html?p=denbys-shorts">Back to Denby\'s Shorts</a>' +
    legalHTML("page-legal");
}

/* ------------------------------------------------------------------ bio -- */

function renderBio() {
  const id = new URLSearchParams(location.search).get("b");
  const b = findBio(id);
  if (!b) {
    location.replace("index.html");
    return;
  }

  const statsHTML = (b.stats || [])
    .map(
      (s) =>
        '<div class="bio-stat"><span class="bio-stat-label">' +
        esc(s.label) +
        '</span><span class="bio-stat-value">' +
        esc(s.value) +
        "</span></div>"
    )
    .join("");

  const statLineHTML = b.statLine
    ? '<div class="stat-line-wrap"><table class="stat-line"><thead><tr>' +
      b.statLine.columns.map((c) => "<th>" + esc(c) + "</th>").join("") +
      "</tr></thead><tbody>" +
      b.statLine.rows
        .map((row) => "<tr>" + row.map((v) => "<td>" + esc(v) + "</td>").join("") + "</tr>")
        .join("") +
      "</tbody></table></div>"
    : "";

  document.title = b.name + " — " + SITE.title;
  document.getElementById("bio").innerHTML =
    planetNavHTML() +
    topbarHTML() +
    '<div class="bio-card">' +
    '<img class="bio-photo" src="' +
    esc(b.photo) +
    '" alt="' +
    esc(b.name) +
    '">' +
    '<h1 class="bio-name">' +
    esc(b.name) +
    "</h1>" +
    '<div class="bio-stats">' +
    statsHTML +
    "</div>" +
    statLineHTML +
    "</div>" +
    '<a class="backlink" href="page.html?p=lineup">Back to Starting Lineup</a>' +
    legalHTML("page-legal");
}

/* -------------------------------------------------------------- site map -- */

function renderSitemap() {
  const rows = SITE.planets
    .filter((p) => p.page)
    .map(function (p) {
      const links = (p.page.links || [])
        .map((l) => '<a href="' + esc(l.href) + '">' + esc(l.label) + "</a>")
        .join("");
      return (
        "<tr>" +
        '<td class="icon"><a href="' +
        esc(planetHref(p)) +
        '"><span class="name">' +
        arcLabel(p.name, 7.5, 10.5) +
        "</span>" +
        planetSVG(p.art, 40) +
        "</a></td>" +
        "<td>" +
        esc(p.page.blurb) +
        "</td>" +
        '<td class="links">' +
        links +
        "</td>" +
        "</tr>"
      );
    })
    .join("");

  document.getElementById("map-body").innerHTML = rows;
  document.getElementById("map-legal").innerHTML = esc(SITE.legal);
  document.getElementById("map-sub").textContent = SITE.title;
}
