# Written From The Hip — site

A 1996-Space-Jam-style site for the newsletter. Open `index.html` in a browser
to see it. No build step, no server needed.

```
index.html      the star field + the moon (home page)
page.html       one template that renders every planet's page
sitemap.html    the site map table
config.js       <-- everything you edit lives here
assets/
  site.css      layout + the house style (fonts, colors, spacing)
  planets.js    draws the planets as SVG
  app.js        builds the pages from config.js
  images/
    moon.png    the moon in the middle
    stars.png   the tiling star background
```

## Changing a planet's name

Open `config.js`, find the planet, change `name`. That's it — the home page,
the page heading and the site map all update.

```js
{
  id: "playlist",          // don't change unless you want the URL to change
  name: "The Playlist",    // <-- change this
  ...
}
```

## Moving a planet

`x` and `y` are percentages of the star field. `x: 0` is the far left, `x: 100`
the far right. `y: 0` is the top, `y: 100` the bottom. The moon sits at 50 / 47,
so keep planets away from there unless you want them overlapping it.
`size` is the planet's width in pixels.

## Changing a planet's look

```js
art: { type: "ringed", color: "#2f6fd0", shade: "#102a5c", light: "#8fc2ff", ring: "#ff3b3b" }
```

- `type` — `sphere`, `ringed`, `banded`, `swirl`, or `marbled`
- `color` — the main body color
- `shade` — the dark side
- `light` — the lit side, and the color of the bands/streaks
- `ring` — ring color, only used by `ringed`

## Changing a page

Each planet's `page` block controls its page:

- `oval` — the color of the title bubble and its text
- `panel` — the two gradient colors of the big rectangle, the link color, and
  `layout`, which is `right`, `left` or `diagonal`
- `blurb` — the red paragraph under the panel
- `links` — the links inside the panel. Replace `href: "#"` with a real URL,
  e.g. `href: "https://writtenfromthehip.substack.com/p/issue-one"`
- `orb` — optional. Adds the floating round button on the right side.

## Adding or removing a planet

Delete a whole `{ ... }` block to remove one. To add one, copy an existing
block, give it a new unique `id`, and pick an `x` / `y` that isn't taken.

## The moon

The title text on the moon is real text, not part of the image, so it's
editable and stays sharp. Change `title` and `issue` at the top of `config.js`.
The title shrinks automatically to fit on one line.

To swap the moon picture itself, replace `assets/images/moon.png` with another
square PNG (transparent background works best).

## More stars

The background is a small square image tiled across the page, so there are two
knobs. In `assets/site.css`, near the top, find the `background:` line on
`body` and either:

1. Point it at a busier tile — `images/stars-dense.png` has about twice as many
   stars, `images/stars-denser.png` about three times as many.
2. Add `background-size: 100px 100px;` underneath it. That shrinks the tile, so
   it repeats more often and the stars sit closer together. The tile is really
   140px, so smaller numbers mean a denser sky and bigger numbers a sparser one.

The two can be combined. Past roughly 80px the stars start to read as noise
rather than a sky.

## Putting it online

It's plain HTML, so any static host works — Netlify, GitHub Pages, Vercel,
Cloudflare Pages. Drag the whole folder in. On Netlify you can literally drop
the folder onto the deploy page.

## A note on the original

The layout, structure and tone are modeled on the 1996 Space Jam site, but none
of Warner Bros.' images, logos or copy are used here. Every planet, banner and
background in this folder was generated from scratch, so it's yours to ship.
