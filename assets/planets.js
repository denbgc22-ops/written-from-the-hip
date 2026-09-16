/* Draws each planet as an inline SVG so it stays sharp at any size and its
   colors can be changed from config.js. You shouldn't need to edit this file. */

let __uid = 0;

function planetSVG(art, size) {
  const a = art || {};
  const type = a.type || "sphere";
  const c = a.color || "#f5871f";
  const s = a.shade || "#3a1a00";
  const l = a.light || "#ffe6c2";
  const ring = a.ring || l;
  const id = "p" + ++__uid;
  const body = {
    sphere: sphere,
    ringed: ringed,
    banded: banded,
    swirl: swirl,
    marbled: marbled,
    shorts: shorts,
    earth: earth,
    basketball: basketball,
    photo: photo,
  }[type] || sphere;

  // an optional word curved along the top of the sphere's own circle, like
  // a badge/seal (e.g. "DERP" on the Derp planet)
  const curvedLabelSVG = a.curvedLabel
    ? '<path id="' +
      id +
      'arc" d="M 26,60 A 34,34 0 1,1 94,60" fill="none"/>' +
      '<text font-family="Verdana, Geneva, sans-serif" font-weight="700" font-size="17" letter-spacing="1.5" fill="' +
      (a.curvedLabelColor || "#ffffff") +
      '" stroke="' +
      (a.curvedLabelOutline || "#000000") +
      '" stroke-width="2" paint-order="stroke">' +
      '<textPath href="#' +
      id +
      'arc" startOffset="50%" text-anchor="middle">' +
      esc(a.curvedLabel) +
      "</textPath></text>"
    : "";

  return (
    '<svg class="planet-art" width="' +
    size +
    '" height="' +
    size +
    '" viewBox="0 0 120 120" aria-hidden="true" focusable="false">' +
    defs(id, c, s, l) +
    body(id, c, s, l, ring, a.photo, a.ring, a.vignette) +
    curvedLabelSVG +
    "</svg>"
  );
}

function defs(id, c, s, l) {
  return (
    "<defs>" +
    '<radialGradient id="' +
    id +
    'g" cx="34%" cy="30%" r="78%">' +
    '<stop offset="0%" stop-color="' +
    l +
    '"/>' +
    '<stop offset="42%" stop-color="' +
    c +
    '"/>' +
    '<stop offset="100%" stop-color="' +
    s +
    '"/>' +
    "</radialGradient>" +
    '<clipPath id="' +
    id +
    'c"><circle cx="60" cy="60" r="42"/></clipPath>' +
    '<clipPath id="' +
    id +
    'f"><rect x="0" y="60" width="120" height="60"/></clipPath>' +
    "</defs>"
  );
}

const ball = (id) => '<circle cx="60" cy="60" r="42" fill="url(#' + id + 'g)"/>';
const gloss =
  '<ellipse cx="44" cy="40" rx="14" ry="9" fill="#ffffff" opacity="0.30" transform="rotate(-28 44 40)"/>';

function sphere(id) {
  return ball(id) + gloss;
}

function ringed(id, c, s, l, ring) {
  const r =
    '<g transform="rotate(-18 60 60)">' +
    '<ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    ring +
    '" stroke-width="6" opacity="0.95"/>' +
    "</g>";
  const front =
    '<g clip-path="url(#' +
    id +
    'f)"><g transform="rotate(-18 60 60)">' +
    '<ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    ring +
    '" stroke-width="6"/>' +
    "</g></g>";
  return r + ball(id) + front + gloss;
}

function banded(id, c, s, l) {
  const g =
    '<g clip-path="url(#' +
    id +
    'c)" opacity="0.55">' +
    '<path d="M0,44 q30,-9 60,0 t60,0 v11 q-30,9 -60,0 t-60,0 Z" fill="' +
    l +
    '"/>' +
    '<path d="M0,64 q30,9 60,0 t60,0 v10 q-30,-9 -60,0 t-60,0 Z" fill="' +
    s +
    '"/>' +
    '<path d="M0,84 q30,-8 60,0 t60,0 v9 q-30,8 -60,0 t-60,0 Z" fill="' +
    l +
    '" opacity="0.7"/>' +
    '<path d="M0,28 q30,7 60,0 t60,0 v7 q-30,-7 -60,0 t-60,0 Z" fill="' +
    s +
    '" opacity="0.8"/>' +
    "</g>";
  return ball(id) + g + gloss;
}

function swirl(id, c, s, l) {
  const g =
    '<g clip-path="url(#' +
    id +
    'c)" fill="none" stroke="' +
    l +
    '" stroke-linecap="round" opacity="0.8">' +
    '<path d="M6,52 q54,-22 108,-4" stroke-width="5"/>' +
    '<path d="M2,68 q58,20 116,2" stroke-width="4" opacity="0.75"/>' +
    '<path d="M10,84 q50,-16 100,2" stroke-width="3" opacity="0.6"/>' +
    '<path d="M14,36 q46,14 92,-2" stroke-width="3" opacity="0.5"/>' +
    "</g>";
  return ball(id) + g + gloss;
}

function photo(id, c, s, l, ring, photoUrl, rawRing, showVignette) {
  if (!photoUrl) return sphere(id);
  const img =
    '<g clip-path="url(#' +
    id +
    'c)"><image href="' +
    photoUrl +
    '" x="18" y="18" width="84" height="84" preserveAspectRatio="xMidYMid slice"/></g>';
  // a moderate radial shade over the photo so it reads as a lit ball, not a
  // flat cutout — white does nothing under multiply, only the dark side
  // darkens.
  const shading =
    '<circle cx="60" cy="60" r="42" fill="url(#' +
    id +
    'g)" opacity="0.45" style="mix-blend-mode:multiply" clip-path="url(#' +
    id +
    'c)"/>';
  // an all-around inner rim, like the limb-darkening at the edge of a ball,
  // so the silhouette reads as round from every angle, not just one diagonal —
  // skipped when a planet's config explicitly turns it off (art.vignette:false)
  const vignette =
    showVignette === false
      ? ""
      : '<circle cx="60" cy="60" r="42" fill="none" stroke="#000000" stroke-width="12" opacity="0.3" clip-path="url(#' +
        id +
        'c)"/>';
  const softGloss =
    '<ellipse cx="44" cy="40" rx="14" ry="9" fill="#ffffff" opacity="0.16" transform="rotate(-28 44 40)"/>';
  // a ring is only drawn when this planet's config explicitly sets one
  if (!rawRing) return img + shading + vignette + softGloss;
  const ringBack =
    '<g transform="rotate(-18 60 60)"><ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    rawRing +
    '" stroke-width="6" opacity="0.95"/></g>';
  const ringFront =
    '<g clip-path="url(#' +
    id +
    'f)"><g transform="rotate(-18 60 60)"><ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    rawRing +
    '" stroke-width="6"/></g></g>';
  return ringBack + img + shading + vignette + softGloss + ringFront;
}

function shorts(id, c, s, l, ring) {
  const ringColor = ring || l;
  const ringBack =
    '<g transform="rotate(-18 60 60)"><ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    ringColor +
    '" stroke-width="6" opacity="0.95"/></g>';
  const ringFront =
    '<g clip-path="url(#' +
    id +
    'f)"><g transform="rotate(-18 60 60)"><ellipse cx="60" cy="62" rx="58" ry="15" fill="none" stroke="' +
    ringColor +
    '" stroke-width="6"/></g></g>';
  const body =
    '<path d="M20,28 L100,28 L96,104 L68,104 L60,56 L52,104 L24,104 Z" fill="' +
    c +
    '"/>';
  const waistband =
    '<rect x="16" y="16" width="88" height="16" rx="8" fill="' +
    s +
    '"/>' +
    '<rect x="16" y="16" width="88" height="5" rx="2.5" fill="' +
    l +
    '" opacity="0.55"/>';
  const button = '<circle cx="60" cy="24" r="3" fill="' + l + '" opacity="0.8"/>';
  const pockets =
    '<g stroke="' +
    s +
    '" stroke-width="3" stroke-linecap="round" opacity="0.55">' +
    '<path d="M26,36 L42,46"/>' +
    '<path d="M94,36 L78,46"/>' +
    "</g>";
  const seams =
    '<g stroke="' +
    s +
    '" stroke-width="2" opacity="0.35" fill="none">' +
    '<path d="M30,52 L26,100"/>' +
    '<path d="M90,52 L94,100"/>' +
    "</g>";
  const highlight =
    '<ellipse cx="42" cy="42" rx="14" ry="7" fill="' +
    l +
    '" opacity="0.32" transform="rotate(-18 42 42)"/>';
  return ringBack + body + waistband + pockets + seams + highlight + button + ringFront;
}

function earth(id, c, s, l) {
  const land = "#3fae4b";
  const landDark = "#2a7a37";
  const desert = "#c9a227";
  const g =
    '<g clip-path="url(#' +
    id +
    'c)">' +
    '<path d="M22,36 q10,-10 20,-3 t2,16 q-3,11 -14,15 t-17,-8 q-4,-13 9,-20 Z" fill="' +
    land +
    '"/>' +
    '<path d="M28,46 q7,-4 11,2 t-3,11 q-6,4 -11,-2 t3,-11 Z" fill="' +
    landDark +
    '" opacity="0.65"/>' +
    '<path d="M70,26 q16,-4 18,11 t-7,24 q-11,9 -20,-2 t-4,-22 q2,-9 13,-11 Z" fill="' +
    land +
    '"/>' +
    '<path d="M76,44 q9,2 6,11 t-11,7 q-7,-2 -5,-11 t10,-7 Z" fill="' +
    desert +
    '" opacity="0.75"/>' +
    '<ellipse cx="58" cy="20" rx="15" ry="6" fill="#eaf6ff" opacity="0.75"/>' +
    "</g>";
  const clouds =
    '<g clip-path="url(#' +
    id +
    'c)" fill="' +
    l +
    '" opacity="0.55">' +
    '<path d="M12,52 q16,-11 30,-2 t27,4 q10,4 3,10 q-15,6 -30,0 t-30,-5 Z"/>' +
    '<path d="M38,80 q14,-8 28,0 t21,6 q-6,6 -21,4 t-28,-4 Z" opacity="0.4"/>' +
    "</g>";
  const atmosphere =
    '<circle cx="60" cy="60" r="43" fill="none" stroke="' +
    l +
    '" stroke-width="2" opacity="0.4"/>';
  return ball(id) + g + clouds + gloss + atmosphere;
}

function basketball(id, c, s, l) {
  const line = "#22160a";
  const lines =
    '<g clip-path="url(#' +
    id +
    'c)" fill="none" stroke="' +
    line +
    '" stroke-width="3.4" stroke-linecap="round">' +
    '<path d="M60,18 L60,102"/>' +
    '<path d="M18,60 L102,60"/>' +
    '<path d="M39,20 Q13,60 39,100"/>' +
    '<path d="M81,20 Q107,60 81,100"/>' +
    "</g>";
  return ball(id) + lines + gloss;
}

function marbled(id, c, s, l) {
  const g =
    '<g clip-path="url(#' +
    id +
    'c)" fill="none" stroke="' +
    l +
    '" stroke-linecap="round" opacity="0.9">' +
    '<path d="M8,40 q14,-12 26,0 t26,0 t26,0 t26,0" stroke-width="6"/>' +
    '<path d="M2,58 q14,12 26,0 t26,0 t26,0 t26,0" stroke-width="6"/>' +
    '<path d="M8,76 q14,-12 26,0 t26,0 t26,0 t26,0" stroke-width="6"/>' +
    '<path d="M2,94 q14,12 26,0 t26,0 t26,0 t26,0" stroke-width="6"/>' +
    "</g>";
  return ball(id) + g + gloss;
}
