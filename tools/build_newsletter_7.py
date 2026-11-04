"""Builds Issue #7 (The Winged Bison at Bdubs is my God): reads newsletter-6.html
as a template, keeps the shared header/dividers/footer, and regenerates each
section from the text defined below.
WARNING: running this OVERWRITES newsletter-7.html.
"""
import re

import os

# Repo root (this file lives in tools/), so the script works from any checkout.
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
src = open(ROOT + "newsletter-6.html", encoding="utf-8").read()


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
header = header.replace("Written From The Hip &mdash; Bad Haircut", "Written From The Hip &mdash; The Winged Bison at Bdubs is my God")
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
    ("margin:0 0 16px;", "I tried out a **super niche** costume over the weekend, and it did not land. Turns out no one knows who the **Purple Hosier is in Dude Perfect’s Ping Pong Trick Shots 3**. We were once a great country."),
    ("margin:0 0 16px;", "It’s 10 am Eastern Standard Time on a Wednesday. Welcome Home."),
    ("margin:0 0 16px;", "**Domo Arigato,**"),
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
    "We are adding **daylight savings** to the starting lineup this week.",
    "What the fuck is **daylight savings**? Who reads the **farmers** almanac other than **farmers**?",
    "Having an extra hour of sleep would’ve been sick, but I haven’t fallen asleep before **2:00 am** since **7th grade**. Why don’t they do the extra hour at like **10 am** when I’m asleep and everyone else is at their jobs. It would be way more productive as a society if everyone worked an extra hour as I get an extra hour of my much needed rest. **This is for the farmers after all**.",
    "This weird vacuum of time that was just added so that we can have sunsets at 4:30 literally makes everyone's life so much worse. If you have a job you wake up and it’s dark, and when you leave your job it’s dark.",
    "Ew.",
    "**I have an idea.**",
    "Instead of an extra hour we just add an entire day every **25 years** or however many hours are in a day.",
    "That extra day every **25 years** would be the most looked forward to day of all time.",
    "I asked one of my smart cousins this, and he said that literally wouldn’t do anything to the crops because it’s all about getting the right amount of **sunlight**.",
    "**Uh, shut up nerd**. You’ve never experienced what it feels like to have an eighth day in a week.",
    "You’re welcome Earth.",
]
waiver_body = "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_paras)
waiver = f'''        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-blue" style="border:3px solid #00c6ff; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:12px;">
                    Waiver Wire Week Seven: Daylight Savings
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/waiver-wire-daylight-savings.png" width="360" alt="Clocks falling back from 2:00 AM to 1:00 AM" style="display:block; width:360px; max-width:100%; height:auto; margin:0 auto 18px; border-radius:8px;">
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
book_paras = [
    "Allow me to take you back in time.",
    "It’s **Fucking** kindergarten.",
    "The walls were draped in numbers and letters that looked like hieroglyphics to my young mind.",
    "Hanging by the door were the Red, Yellow, and Green cards that we lived and died by.",
    "Next to that was everyone's jobs for the day.",
    "I (me) got to do the coolest job that day. I was the line leader.",
    "We had one of those classrooms that had the bathroom attached because we were still too young to wander the super scary hallways. Also, the teachers weren’t paid enough to take us to the bathroom every five minutes.",
    "Well, this was the beginning of my end.",
    "It was reading time, and the God above made me have the sudden urge to **piss**.",
    "While everyone was sitting on the carpet that looked like a birds-eye-view of a perfect little village. I got up and walked towards the bathroom, gracefully, like Neil Armstrong walking on the moon, in the soundstage, in Warner Brothers studios.",
    "The door was locked. “**FUCK**. SHIT. **FUCK** ME TO TEARS. WHAT DO I DO??” I screamed. Mrs. Arnold was **piss**ed about the cursing. Wordplay.",
    "I did the ole standing up leg cross to pinch my **crotch**, but it was too late, **piss** was pouring out of me and there was nothing I could do about it. I grabbed the nearest book and stood in the back of the class.",
    "That book was the Rainbow Fish, by Marcus **Pfister**. Now that’s a last name. The tantalizing scales on the book cover made the whole class start staring at me. It was pretty embarrassing. My nickname was **pissboy** for a really long time. Luckily my nickname got changed to **chug** when I got older because I **chug** beer so well.",
    "Ever since I **piss**ed myself I made an ode to myself that I would never read again. Look at me now Mrs. Arnold.",
    "8/10 I like the scales.",
]
book_inner = "".join(p(t, "margin:0 0 16px;") for t in book_paras[:-1]) + p(book_paras[-1], "margin:0;")
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
                        <a href="https://www.amazon.com/dp/1558585362" target="_blank">
                          <img src="https://writtenfromthehip.com/assets/images/book-rainbow-fish.jpg" width="240" alt="The Rainbow Fish by Marcus Pfister" style="display:block; width:240px; max-width:100%; height:auto; border-radius:4px;">
                        </a>
                      </td>
                    </tr>
                    <tr>
                      <td align="center" style="padding-top:10px; font-family:Verdana, Geneva, sans-serif; font-size:13px; line-height:1.5; color:#ffffff;">
                        Rating: 8/10
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
    "Mecca.",
    "When you think of Mecca, you’re probably thinking of the holiest city in Islam, the place where millions if not billions make the yearly pilgrimage to circle around the black cube called the Kaaba, and pray your heart out with your absolute boys.",
    "When I think of Mecca, I also think of a black building with gold text on it. That black building in question is not in Western Saudi Arabia, but just five minutes away from my crib on the side of the highway, and it serves the most mediocre food with the worst hospitality you can ever imagine.",
    "Buffalo Wild Wings.",
    "A yearly pilgrimage every man aged 13-38 has to make if they want to see the Winged-Bison in the afterlife. Us men spend an insurmountable amount of money to wait an unimaginable amount of time to eat and drink to the point where you are completely unsatisfied in both categories. It’s perfect. It’s religion. It’s Bdubs.",
    "I made that pilgrimage last Friday for some fucking reason. Maybe it came to me in a dream to visit Bdubs, or maybe someone sent “wanna hit up buffalo wild wings tn” and it got three thumbs up reactions. I don’t know, but I found myself at my definition of Mecca this Friday.",
    "I arrived at the black cube with three of my closest “friends.” All wearing our specific garb for this special occasion. A niche jersey, pants, and flip flops. This religious experience began once we sat on a four person hightop of backless metal stools.",
    "The waiter came by the table and served me a look. A look that said this guy didn’t need a menu.",
    "“I’ll have the Wild Herd Draft, 15 bone-in buffalo dry rub wings, a side of fries, and ranch.” I said with utmost gusto.",
    "“Okay Lardo.” The waiter snickered.",
    "I didn’t know how to respond. This was the first of many tests the Winged-Bison will give me tonight. I decided to get up and visit the men's room to yell profanities in the mirror. My blood curling screams induced a headache that could only be resolved by drinking a draft beer. I headed back to the table to consume said draft beer, and started the Bdubs patented forty five minute wait. The fast.",
    "My own Ramadan.",
    "I would be so good at Ramadan if Ramadan was forty five minutes long, and I could also drink beer during the fast. This was my mental test. I knew walking into this establishment this food fast would happen, but I still needed inner peace, my inner chakra. This wasn’t supposed to be easy. As fifty cent once said: Sunny days wouldn’t be special if it wasn’t for rain. Joy wouldn’t feel so good if it wasn’t for pain.",
    "My “friends” were talking to each other in order to fill this void of time. I decided to take an oath of silence. To focus on what really mattered. I wanted to learn from this experience.",
    "Then my “friend's” orders came in. Food filled every square inch of the table except for where I was sitting.",
    "Another test from the Winged-Bison-God from above.",
    "I did the respectful thing and said “you guys can go ahead and start while it’s hot!” I was trying to have manners, usually “friends” respond by saying “no worries we can wait.” Then I say “no no no I insist” and then they say “it’s alright really it shouldn’t be too long.”",
    "But no.",
    "They began to eat. I was left astray. Sitting on a backless metal stool. Watching my friends eat.",
    "Minutes passed. Still no food, my friends gnawing on cartilage and gristle. I began to feel like a cuck watching people do what I wanted to do. I tried to veer my perverted thoughts away from the task at hand and look at the fourteen tv’s in front of me all playing the same WNBA finals game. It didn’t work. I was going crazy.",
    "I was going to speak up about the wait time, but I am afraid of confrontation. So I stayed silent waiting.",
    "Then out of the corner of my eye. A sizzling luke-warm plate of 15 bone-in buffalo dry rub wings, and a side of fries reached my placemat.",
    "It’s here. The task is accomplished. The fast is over. I’ve reached nirvana.",
    "I took a bite of the drum. Fully dipped in blue cheese when I specifically asked for ranch.",
    "Nonetheless, the taste, so mediocre. Exactly what I wanted. The Winged-Bison has blessed my soul once again. I’ll see you next year.",
    "Buffalo Wild Wings. The true Mecca.",
]
otd = f'''        <!-- ================= SECTION: OFF THE DOME ESSAY ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-purple" style="border:3px solid #7a2bd0; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:28px 26px;">
                  <div class="glow-gold" style="color:#ffd700; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    This Is Off The Dome But going to Bdubs is a religious experience.
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/off-the-dome-week-seven.png" width="100%" alt="The Kaaba equals Buffalo Wild Wings" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
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
fark_inner = ps([
    "Over this halloweekend Martha Stewart’s niche costume was a homeless person.",
    "Bear with me as I try to be the devil’s advocate. Let’s try to see the vision behind it.",
    "When you are homeless you have no responsibilities, no house to take care of, no lawn to mow, no kitchen to clean up, no food to eat before it goes bad, nobody to answer to, nobody who’s gonna call you asking for a favor. It really does seem quite nice, you just get to walk around and explore different parts of the city that you call home.",
    "Okay this is starting to sound pretty chill.",
    "I was also once told that you will never be happier than the guy chugging Aristocrat laying on the street five minutes down the road.",
    "I don’t know why my own father would tell me this, but it has been the single most important piece of advice I have ever received.",
    "I can see the vision here.",
    "But also if you take a step back you then realize that for Halloween you can literally be whatever you want, and Martha decided to be homeless. It’s a bold strategy, Cotton. Let’s see if it pays off for ‘em.",
    "It indeed did not.",
    "I’m excited for what she’s gonna be for Halloween next year. My money is on Snoop Dogg.",
])
fark = f'''        <!-- ================= SECTION: FARK OF THE WEEK ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box" style="border:3px solid #ff3b3b; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Fark of the week: Martha Stewart
                  </div>
                  <img src="https://writtenfromthehip.com/assets/images/fark-week-seven-martha.jpg" width="320" alt="Martha Stewart in her Halloween costume" style="display:block; width:320px; max-width:100%; height:auto; border-radius:8px; margin:0 auto 20px;">
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
    "**What's venus up 2? Venus** Williams played in the **Hong Kong Open** this past weekend. She sadly lost again in the **first round**. She **technically** hasn’t won a singles match in **470 days**. That’s equal to 676,800 minutes.",
    "You could take **pity** on my girl but just remember this. While everyone was out partying, **dressing** up as **homeless people** for Halloween, Venus was **working** on her craft, **technically** playing pro tennis.",
    "**Venus** was a **wildcard** again for this tournament. For those who do not follow WTA pro women's tennis. This means she was selected to play in the tournament for **commercial benefits** rather than her **official WTA rank**. In the tennis world this is frowned upon because technically Venus is taking a spot from **younger** tennis players that are good enough to play in these tournaments.",
    "Since pro women’s tennis players don’t have a fixed **salary**, Venus is practically **taking money** away from the **young promising** tennis players, so she can design more furniture for **Crate & Barrel**.",
    "She is pretty much a reverse Robin Hood in the tennis world. **Which is fucking sick**. She needs to buy in on this **villain arc** she’s created for herself. According to her WTA bio she has **$43,357,200** in winnings. I need that **doubled** solely from wildcard tournament appearances.",
]
venus = venus_top
venus += '                  <img src="https://writtenfromthehip.com/assets/images/venus-week-seven.png" width="100%" alt="Venus Williams at the Hong Kong Open" style="display:block; max-width:500px; border-radius:8px; margin:22px auto 0;">\n'
venus += '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">\n'
for i, txt in enumerate(venus_rows):
    venus += venus_row("", txt, last=i == len(venus_rows) - 1)
venus += '''                  </table>

                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- PUBLIC DOME-AIN ----------------
subs = [
    ("Rob From New York", "Oct 30, 10:33 PM", "“This is off the dome, but a good vocal stem can keep me occupied for hours, and the only downside is that my mom thinks she might need to take me to a “doctor” to get tested.”"),
    ("Stacy From Chicago", "Oct 31, 9:24 PM", "“This is off the dome but a costume party full of niche costumes from niche pop culture events just ends up looking like a normal party with people wearing normal clothes not knowing who anybody is dressed up as.”"),
    ("Wilson From Stillwater", "Nov 1, 3:32 AM", "“This is off the dome but my white rat dog is better than your perfect golden retriever.”"),
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
open(ROOT + "newsletter-7.html", "w", encoding="utf-8").write(out)
print("written", len(out))
