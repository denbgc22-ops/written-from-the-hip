"""EXAMPLE of how Issue #6 was generated: it reads newsletter-5.html as a template,
keeps the shared header/dividers/footer, and regenerates each section from the
text defined below. For a new issue, copy this file, point `src` at the latest
newsletter-N.html, change the output file name and the content, then run it.
WARNING: as written this OVERWRITES newsletter-6.html. Change the output name first.
"""
import re

import os

# Repo root (this file lives in tools/), so the script works from any checkout.
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
src = open(ROOT + "newsletter-5.html", encoding="utf-8").read()


def e(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for a, b in (("’", "&rsquo;"), ("‘", "&lsquo;"), ("“", "&ldquo;"), ("”", "&rdquo;"),
                 ("—", "&mdash;"), ("–", "&ndash;"), ("…", "&hellip;"), ("'", "&rsquo;")):
        s = s.replace(a, b)
    return s


def fmt(t):
    t = e(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"__(.+?)__", r"<em>\1</em>", t)
    return t.replace("\n", "<br>")


def cut(start, end=None):
    i = src.index(start)
    j = src.index(end) if end else len(src)
    return src[i:j]


header = src[: src.index("        <!-- ================= SECTION 1: WELCOME")]
header = header.replace("Written From The Hip &mdash; A Mother&rsquo;s Hug", "Written From The Hip &mdash; Bad Haircut")
footer = cut("        <!-- ================= DIVIDER: WFTH MOON")
nfl_divider = cut("        <!-- ================= DIVIDER: NFL", "        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE")
d_book = cut("        <!-- ================= DIVIDER: BOOK COVERZ", "        <!-- ================= SECTION: BOOK COVER")
d_otd = cut("        <!-- ================= DIVIDER: OFF THE DOME", "        <!-- ================= SECTION: OFF THE DOME ESSAY")
d_fark = cut("        <!-- ================= DIVIDER: FARK", "        <!-- ================= SECTION: FARK OF THE WEEK")
d_venus = cut("        <!-- ================= DIVIDER: VENUS", "        <!-- ================= SECTION: VENUS")
d_pub = cut("        <!-- ================= DIVIDER: PUBLIC DOME-AIN", "        <!-- ================= SECTION: PUBLIC DOME-AIN")
venus_top = cut("        <!-- ================= SECTION: VENUS", '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">')
pub_section = cut("        <!-- ================= SECTION: PUBLIC DOME-AIN", "        <!-- ================= DIVIDER: WFTH MOON")

# ---------------- WELCOME ----------------
welcome = cut("        <!-- ================= SECTION 1: WELCOME", "        <!-- ================= DIVIDER: NFL")
a = welcome.index('                    <p style="margin:0 0 16px;"><strong>Yo,</strong></p>')
b = welcome.index('                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">')
open_paras = [
    ("margin:0 0 16px;", "**Yo,**"),
    ("margin:0 0 12px;", "“Did you see the **big game** last night?”"),
    ("margin:0 0 12px;", "“Man, this **weather** has been great lately!”"),
    ("margin:0 0 16px;", "“I cannot believe **Venus Williams** fucking **lost** in the first round of the **2026 WTA Guangzhou Open**.”"),
    ("margin:0 0 16px;", "Do you see how **easy** it is to sneak in some **Written From The Hip** conversation topics into your **day to day** life? Try it out today at the **water cooler**. Spread **our** message."),
    ("margin:0 0 16px;", "It’s 10 am Eastern Standard Time on a Wednesday. Welcome Home."),
    ("margin:0 0 16px;", "**P.S.** If you forward this email to **three people** and those **three people** forward it to **three more people**, and so on/so forth. We could create our own **pyramid scheme**. You make **money**, we make **money**, we all make **money**. We would like for that to happen."),
    ("margin:0 0 10px;", "**Domo Arigato,**"),
]
new_paras = "\n".join(f'                    <p style="{st}">{fmt(t)}</p>\n' for st, t in open_paras)
welcome = welcome[:a] + new_paras + welcome[b:]


def p(text, style="margin:0 0 14px;"):
    return f'                    <p style="{style}">{fmt(text)}</p>\n'


def ps(paras):
    return "".join(p(t) for t in paras[:-1]) + p(paras[-1], "margin:0;")


def listtable(items, color, last=False):
    rows = "\n".join(
        f'                      <tr><td valign="top" style="padding:4px 0; width:26px; font-family:Verdana, Geneva, sans-serif; font-size:15px; color:{color};">{n}</td>'
        f'<td style="padding:4px 0; font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.7; color:{color}; font-weight:700;">{fmt(t)}</td></tr>'
        for n, t in items
    )
    mb = "0" if last else "14px"
    return f'                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 {mb};">\n{rows}\n                    </table>\n'


# ---------------- WAIVER WIRE ----------------
waiver_paras = [
    "We are adding my **Barbour Jacket** that has been **waiting** patiently in the back of my **closet** for the last seven months to the **starting lineup** this week.",
    "The **weather** has turned. It’s **70** degrees. Winter is **coming**.",
    "I was walking past my closet on Sunday, and I heard a faint song **coming** from within. I had put **wax** in my ears, so that I might not be able to hear, but I was intrigued by the sound, so I opened the door to find my **Barbour Jacket** singing the **siren** song to me. I tried my best to stop listening, but I **caved**, and let this wax coated jacket wrap around me like a **20 foot anaconda**.",
    "It’s been **five** years since I bought this **jacket**, and every single year I have the uncontrollable urge to wear the living **fuck** out of it once the temperature is under **seventy degrees**. I don’t know why I keep coming back to this jacket. It either makes me feel way **too hot**, or I need two more layers under the jacket so I don’t die of **hypothermia**.",
    "If I was a hunter in the **English countryside** this jacket would have so many **practical** uses, but sadly I'm not, so the fifteen pockets in this bad boy will be unused once again this winter.",
    "I’m still wearing it though. I can’t wait to find this Jacket under **#Oldmoney** on the TikTok shop this week for $14.99",
]
waiver_body = "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_paras)
waiver = f'''        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-blue" style="border:3px solid #00c6ff; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:12px;">
                    Waiver Wire Week Six: The Barbour Jacket In The Back Of My Closet
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/waiver-wire-barbour-jacket.png" width="360" alt="Barbour jacket" style="display:block; width:360px; max-width:100%; height:auto; margin:0 auto 18px; border-radius:8px;">
                  <div style="font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:#b8e2ff;">
{waiver_body}
                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- BOOK COVER ----------------
YEL = "#fff6a8"
book_inner = ""
book_inner += p("This week’s **Book Cover** is **“Quotations from Chairman Mao Tse-tung”** aka the **“Little Red Book”**. I found this book whilst **perusing** through my dad’s closet to **steal** some of his clothes.", "margin:0 0 16px;")
book_inner += p("I steal my dad’s clothes all of the time now that I am **officially** the same size as a **fully grown man**. I had just spilled some queso on my dad’s **old polo** and needed a **new polo** to spill some more queso on. As I was flipping through the endless selection of **striped** collared shirts I saw a box that said, “**The Second Family**”", "margin:0 0 16px;")
book_inner += p("**I really didn’t want to open the box**. I felt that it would be best if I let this **second family thing** come out naturally down the line, but I saw this **little red book** poking out of the box and I just had to check it out.", "margin:0 0 16px;")
book_inner += p("I opened the Second Family Box and saw three things.", "margin:0 0 8px;")
book_inner += listtable([
    ("1.", "**“Quotations from Chairman Mao Tse-tung”**"),
    ("2.", "A pair of diamond studded **brass** knuckles"),
    ("3.", "A christmas card with what looked to be my **dad**, and twenty dogs holding him up with their **paws**. It read “¡**Feliz Navidad**! De parte de **mi familia favorita** para la tuya.”"),
], YEL)
book_inner += p("It was the first time I'd seen him **smile** for a photo.", "margin:0 0 16px;")
book_inner += p("This book cover is interesting to say the least. It’s red, and supposedly it’s little. Pretty **slick** photo of **Mao**. There’s **something** about this book that **makes me** want to be **forced** to listen to everything this guy says.", "margin:0 0 16px;")
book_inner += p("7/10 Could be **redder** and **littler**", "margin:0;")
book = f'''        <!-- ================= SECTION: BOOK COVER ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-yellow" style="border:3px solid #ffe81f; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px;">
                  <div class="glow-blue" style="color:#6ec6ff; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Judge A Book By Its Cover
                  </div>
                  <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto 16px;">
                    <tr>
                      <td align="center">
                        <a href="https://www.amazon.com/dp/1790752809" target="_blank">
                          <img src="https://writtenfromthehip.com/assets/images/book-little-red-book.png" width="240" alt="Quotations from Chairman Mao Tse-tung" style="display:block; width:240px; max-width:100%; height:auto; border-radius:4px;">
                        </a>
                      </td>
                    </tr>
                    <tr>
                      <td align="center" style="padding-top:10px; font-family:Verdana, Geneva, sans-serif; font-size:13px; line-height:1.5; color:#ffffff;">
                        Rating: 7/10
                      </td>
                    </tr>
                  </table>
                  <div style="font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:{YEL};">
{book_inner}                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- OFF THE DOME ----------------
otd_paras = [
    "Hair, the thing that never stops stopping. The unmoving force that needs to be maintained, so that my unemployable look can look employable.",
    "Other things grow on your body. Nails, for instance. But even my dumb hands have enough motor function and coordination to cut them.",
    "My dumb hands/brain can’t handle cosmetology school, so I have to get my hair cut by a professional.",
    "I just left my monthly appointment at my local, family run, small business. It’s a barbershop called Supercuts, and they have this weekly special where you can pay a small price of $32.95 and in return they royally fuck your shit up to the point where you can’t step a foot outside of your house for the next four days. It’s a great deal, you guys should definitely check it out.",
    "A haircut is the only place where you specifically ask for something, and you don’t get the thing you specifically ask for. Imagine going to a restaurant getting the wrong sandwich, and when you ask the waiter to send it back, they spit in your face and cut another inch off of your sandwich.",
    "Getting over a bad haircut is literally like getting over a drug addiction (I have never been addicted to anything, but I saw Beautiful Boy eight years ago, so I know exactly what I am talking about). Where, like quitting something cold turkey, the first three days are the hardest and then you relapse with an excessive amount of substances to the point where you feel comfortable in your own skin to go to the grocery store. That’s what I go through every time I leave a Supercuts.",
    "Do you know what’s worse than being addicted to drugs, and also happens every time you get your hair cut?",
    "Two words, two syllables.",
    "Small talk.",
    "At Supercuts, small talk is forced upon you whether you like it or not. During the haircut you are literally held at knife point (technically scissors, but you get the point), you are forcefully tied down (via the barber cape), whilst getting choked out with the white paper thing so little hairs don’t fall down your shirt.",
    "And the cherry on top.",
    "OneRepublic on 102.7 KIIS-FM is playing on the speaker directly over your head. The sound waves of ‘Counting Stars’ birth an earworm in your brain that doesn’t crawl out until your next haircut. While all of this is happening to you, you’re also answering questions left and right about what you have been doing that day, and the weather outside.",
    "If these tactics were used at Guantanamo bay we would know every secret from every terrorist organization in human history.",
    "At the end of the “haircut” they ask if you want “the hot towel” Just another torture device. I say yes because I’m a masochist, I like the pain. Wrap that boiling towel around my face until I can’t breathe, and all I can smell is the last person’s face you used it on. GIVE IT TO ME!",
    "Right as you’re about to leave the chair they have the audacity to ask you if your hair cut looks good. You bite your tongue and say “Yes” even though you look like a psych ward patient on the fritz.",
    "After this hellride is all set and done, you pay with your mom’s credit card because you can. You have a choice to tip some of your mom’s money, and you don’t because you can. These were the only choices that were offered to you in this godforsaken place.",
    "You leave the establishment by pushing on the door that emphatically says pull.",
    "Sick, I can’t wait till I do this again in thirty days.",
]
otd = f'''        <!-- ================= SECTION: OFF THE DOME ESSAY ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-purple" style="border:3px solid #7a2bd0; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:28px 26px;">
                  <div class="glow-gold" style="color:#ffd700; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    This Is Off The Dome But getting a haircut is worse than whatever happened at Guantanamo Bay.
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/off-the-dome-week-six.png" width="100%" alt="Bad haircut" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
                  <div class="glow-blue" style="color:#6ec6ff; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:15px; line-height:1.7;">
{ps(otd_paras)}                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- FARK ----------------
GOLD = "#ffd700"
fark_inner = ""
fark_inner += p("If you thought I was done talking about Mao, you are foolishly incorrect. This is a double Mao week motherfucker.")
fark_inner += p("A couple of days ago, Kylian Mbappe was asked on a podcast what his favorite Mbappe meme was. He responded in French, so it kinda sounded like gibberish to me, but according to google translator he said:")
fark_inner += p("“The one where they put my face on a Chinese dictator (Mao Zedong). That really makes me laugh, I use it with my friends all the time”")
fark_inner += p("From the statement above Kylian thought that Mao Zedong was a Chinese Dictator when in reality Mao was actually a Totalitarian Dictator.")
fark_inner += p("How did world renowned soccer player Kylian Mbappe not know this? This guy clearly hasn’t read the cover of “Quotations from Chairman Mao Tse-tung” aka the “Little Red Book”")
fark_inner += p("This angered his Chinese fanbase, and he ended up losing two sponsorships:", "margin:0 0 8px;")
fark_inner += listtable([("1.", "Dongpeng, maker of beverages."), ("2.", "Mengniu, a dairy giant that makes cheese.")], GOLD)
fark_inner += p("I have two thoughts on this situation.", "margin:0 0 8px;")
fark_inner += listtable([
    ("1.", "These sponsorships sound like Mythological food gods"),
    ("2.", "Kylian is a complete idiot for thinking Mao was a “dictator” instead of a “totalitarian dictator that technically caused the Great Chinese Famine that killed 15-55 million people”"),
], GOLD)
fark_inner += p("How do you mix up the two? Having read the book cover of the Little Red Book, I know a lot about his situation. Way more than the average person, and I would have never made this mistake.", "margin:0;")
fark = f'''        <!-- ================= SECTION: FARK OF THE WEEK ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box" style="border:3px solid #ff3b3b; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Fark of the week: Kylian Mbappe thought Mao Zedong was a dictator
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/fark-week-six-mbappe.png" width="100%" alt="Kylian Mbappe and Mao meme" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
                  <div class="glow-gold" style="color:{GOLD}; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:15px; line-height:1.7;">
{fark_inner}                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''


# ---------------- VENUS ----------------
def venus_row(label, text, last=False, extra=""):
    pad = "" if last else "padding-bottom:14px; "
    lab = f'<span class="glow-green" style="color:#39ff14; font-weight:700; text-transform:uppercase;">{e(label)}</span>' if label else ""
    return f'''                    <tr>
                      <td style="{pad}font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:#e9d1ff;">
                        {lab}
                        <span>{" " if label else ""}{fmt(text)}</span>{extra}
                      </td>
                    </tr>
'''


venus_rows = [
    "Okay so Venus **technically** lost in the first round of the 2026 WTA Guangzhou open.",
    "She has **technically** lost her last sixteen singles matches.",
    "She also **technically** lost to Lilli Tagger, who is **technically** eighteen.",
    "That’s **technically** a 28-year age gap between both players.",
    "Venus has also won six Grand Slam singles titles which is six more than the person reading this, so fuck you. **Technically** the six Grand Slam singles titles were all won before her opponent was born.",
    "We also made merch to commemorate this tournament, please let us know if you want these:",
]
venus = venus_top
venus += '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">\n'
for i, txt in enumerate(venus_rows):
    last = i == len(venus_rows) - 1
    extra = ""
    if last:
        extra = '\n                        <br><br>\n                        <img src="https://writtenfromthehip.com/assets/images/venus-week-six-merch.png" width="100%" alt="Venus Williams Guangzhou merch" style="display:block; max-width:520px; border-radius:8px; margin:0 auto;">'
    venus += venus_row("", txt, last=last, extra=extra)
venus += '''                  </table>

                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- PUBLIC DOME-AIN ----------------
subs = [
    ("Will From Sydney, Australia", "Oct 20, 12:36 AM", "“This is off the dome but jumping in a body of water and petty theft from a struggling bodega are 1 and 2 when it comes to beating a hangover.”"),
    ("Sam From Florence", "Oct 20, 4:41 PM", "“This is off the dome but, what was the housewife equivalent to burning the tuna casserole 2000 years ago? Imagine being a Roman soldier and coming home to fucking bread and olives again.”"),
    ("William From Guangzhou, China", "Oct 21, 3:17 AM", "“This is off the dome but I’m currently sitting in the Guangzhou airport with no sign of Venus Williams yet. However, I think that Chinese futuristic toilets may be a bigger threat to humanity than the rapid growth of AI and data centers.”"),
    ("Dan From Neptune", "Oct 21, 9:13 AM", "“This is off the dome, but graduate school is just daycare for unemployed people.”"),
]
sub_rows = ""
for i, (n, t, q) in enumerate(subs):
    border = "" if i == len(subs) - 1 else " border-bottom:1px dashed #6b2222;"
    sub_rows += f'''                    <tr>
                      <td style="padding:12px 0;{border}">
                        <div style="font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:#ffff33; margin-bottom:4px;">{e(n)} on {e(t)}</div>
                        <div style="font-family:'Courier New', Courier, monospace; font-weight:700; font-size:16px; line-height:1.5; color:#ff0000;">{e(q)}</div>
                      </td>
                    </tr>
'''
open_tag = '                      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="left">\n'
i0 = pub_section.index(open_tag) + len(open_tag)
j0 = pub_section.index("                      </table>\n                    </td></tr>")
pubdome = pub_section[:i0] + sub_rows + pub_section[j0:]

out = header + welcome + nfl_divider + waiver + d_book + book + d_otd + otd + d_fark + fark + d_venus + venus + d_pub + pubdome + footer

# ---------------- DARK-MODE-SAFE COLORS ----------------
# Gmail's dark mode inverts every color it can read in a style (backgrounds,
# borders, text) but leaves images alone. So: dark panels and "borders" are
# built from tiny solid-color PNG tiles (a border is a tile-colored outer
# table with 3px padding around the dark inner table), and every text color
# is repeated as -webkit-text-fill-color, which paints over `color`. An
# Outlook-only (mso) style block restores colors where background images
# are ignored.
BASE = "https://writtenfromthehip.com/assets/images/"
TILES = {"#050505": ("tile-050505.png", "mso-dk"), "#000000": ("tile-000000.png", "mso-bk"),
         "#39ff14": ("tile-39ff14.png", "mso-gn"), "#7a2bd0": ("tile-7a2bd0.png", "mso-pu"),
         "#00c6ff": ("tile-00c6ff.png", "mso-bl"), "#ffe81f": ("tile-ffe81f.png", "mso-ye"),
         "#ff3b3b": ("tile-ff3b3b.png", "mso-rd"), "#6ec6ff": ("tile-6ec6ff.png", "mso-lb")}
TEXT_MAP = {"#ffd700": "#c99800", "#ffe81f": "#c99800", "#ffff33": "#c99800", "#ffe14d": "#c99800",
            "#fff6a8": "#c99800", "#6ec6ff": "#2ea0e8", "#b8e2ff": "#2ea0e8", "#e9d1ff": "#b070f0",
            "#39ff14": "#22c800", "#ffffff": "#8f8f8f"}
TABLE_TOKEN = re.compile(r"<table\b|</table>")


def wrap_section_borders(html):
    out, pos = [], 0
    pat = re.compile(r'<table\b[^>]*class="[^"]*section-box[^"]*"[^>]*>')
    while True:
        m = pat.search(html, pos)
        if not m:
            out.append(html[pos:])
            break
        out.append(html[pos:m.start()])
        tag = m.group(0)
        depth, i = 1, m.end()
        while depth:
            t = TABLE_TOKEN.search(html, i)
            depth += -1 if t.group(0) == "</table>" else 1
            i = t.end()
        inner_html = html[m.end(): i - len("</table>")]
        color = re.search(r"border:3px solid (#[0-9a-fA-F]{6});", tag).group(1).lower()
        cls = re.search(r'class="([^"]*)"', tag).group(1)
        outer = ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="' + cls +
                 '" style="border-radius:10px; background-image:url(\'' + BASE + "tile-" + color[1:] + '.png\');"><tr><td style="padding:3px;">')
        inner = ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
                 'style="border-radius:7px; background-image:url(\'' + BASE + 'tile-050505.png\');">')
        out.append(outer + inner + inner_html + "</table></td></tr></table>")
        pos = i
    return "".join(out)


def darkmode_safe(html):
    # the 600px column already has the star-field image; drop its black color
    html = re.sub(r"background-color:#000000;\s*(background-image:url\('[^']*stars-denser\.png'\))", r"\1", html)
    for color, (tile, cls) in TILES.items():
        html = html.replace(f"background-color:{color};", f"background-image:url('{BASE}{tile}');")
    html = wrap_section_borders(html)
    for color, (tile, cls) in TILES.items():
        def addcls(m, tile=tile, cls=cls):
            tag = m.group(0)
            if tile not in tag:
                return tag
            if 'class="' in tag:
                return tag.replace('class="', f'class="{cls} ', 1)
            return tag.replace(">", f' class="{cls}">', 1)
        html = re.sub(r"<(?:table|td|div)\b[^>]*>", addcls, html)
    # Gmail dark mode maps text brightness into a narrow band (very light
    # colors become dark, mid-tones stay about the same), so text uses
    # vivid mid-brightness colors that read well in both modes.
    html = re.sub(r"(?<![\w-])color:\s*(#[0-9a-fA-F]{3,6})(?=\s*[;\"])",
                  lambda m: "color:" + TEXT_MAP.get(m.group(1).lower(), m.group(1)), html)
    if ".mso-dk" not in html:
        rules = "".join(f"  .{cls} {{background-color:{color} !important;}}\n" for color, (_, cls) in TILES.items())
        html = html.replace("</head>", '<!--[if mso]>\n<style type="text/css">\n' + rules + "</style>\n<![endif]-->\n</head>", 1)
    return html


# dark-mode tweaks reverted at the user's request: out = darkmode_safe(out)
open(ROOT + "newsletter-6.html", "w", encoding="utf-8").write(out)
print("written", len(out))
