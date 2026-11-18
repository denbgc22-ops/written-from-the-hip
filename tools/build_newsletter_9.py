"""Builds Issue #9 (Counting Sheep): reads newsletter-6.html as a template,
keeps the shared header/dividers/footer, and regenerates each section from the
text defined below. (The unused Gmail dark-mode helpers live in
build_newsletter_7.py.)
WARNING: running this OVERWRITES newsletter-9.html.
"""
import re

import os

# Repo root (this file lives in tools/), so the script works from any checkout.
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
src = open(ROOT + "newsletter-6.html", encoding="utf-8").read()
IMG = "https://writtenfromthehip.com/assets/images/"


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
    # [link text](url)
    t = re.sub(r"\[(.+?)\]\((\S+?)\)",
               r'<a href="\2" target="_blank" style="color:inherit; text-decoration:underline;">\1</a>', t)
    return t.replace("\n", "<br>")


def cut(start, end=None):
    i = src.index(start)
    j = src.index(end) if end else len(src)
    return src[i:j]


header = src[: src.index("        <!-- ================= SECTION 1: WELCOME")]
header = header.replace("Written From The Hip &mdash; Bad Haircut", "Written From The Hip &mdash; Counting Sheep")
footer = cut("        <!-- ================= DIVIDER: WFTH MOON")
nfl_divider = cut("        <!-- ================= DIVIDER: NFL", "        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE")
d_book = cut("        <!-- ================= DIVIDER: BOOK COVERZ", "        <!-- ================= SECTION: BOOK COVER")
d_otd = cut("        <!-- ================= DIVIDER: OFF THE DOME", "        <!-- ================= SECTION: OFF THE DOME ESSAY")
d_fark = cut("        <!-- ================= DIVIDER: FARK", "        <!-- ================= SECTION: FARK OF THE WEEK")
d_venus = cut("        <!-- ================= DIVIDER: VENUS", "        <!-- ================= SECTION: VENUS")
d_pub = cut("        <!-- ================= DIVIDER: PUBLIC DOME-AIN", "        <!-- ================= SECTION: PUBLIC DOME-AIN")
venus_top = cut("        <!-- ================= SECTION: VENUS", '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">')
pub_section = cut("        <!-- ================= SECTION: PUBLIC DOME-AIN", "        <!-- ================= DIVIDER: WFTH MOON")


def p(text, style="margin:0 0 14px;"):
    return f'                    <p style="{style}">{fmt(text)}</p>\n'


def ps(paras):
    return "".join(p(t) for t in paras[:-1]) + p(paras[-1], "margin:0;")


def listtable(items, color, last=False, bold=True, size=15):
    weight = " font-weight:700;" if bold else ""
    rows = "\n".join(
        f'                      <tr><td valign="top" style="padding:4px 0; width:26px; font-family:Verdana, Geneva, sans-serif; font-size:{size}px; color:{color};">{n}</td>'
        f'<td style="padding:4px 0; font-family:Verdana, Geneva, sans-serif; font-size:{size}px; line-height:1.7; color:{color};{weight}">{fmt(t)}</td></tr>'
        for n, t in items
    )
    mb = "0" if last else "14px"
    return f'                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 {mb};">\n{rows}\n                    </table>\n'


# ---------------- WELCOME ----------------
welcome = cut("        <!-- ================= SECTION 1: WELCOME", "        <!-- ================= DIVIDER: NFL")
a = welcome.index('                    <p style="margin:0 0 16px;"><strong>Yo,</strong></p>')
b = welcome.index('                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">')


def wp(text, style="margin:0 0 16px;"):
    return f'                    <p style="{style}">{fmt(text)}</p>\n'


new_paras = (
    wp("**Yo,**")
    + wp("So much **shit** occurred this week. **Really**, very, **extremely**, **end-of-the-world** important **shit**. The type of important shit **where** if you’re just **ever-so-slightly** **misinformed**, you could look like a complete **idiot** when you're trying to look **smart** in front of your friends. That’s why you read this newsletter. To get the most **factual geo-political, and pop-cultural facts** you can ever read, typed straight from my very own finger tips. I got three things for you to do:")
    + listtable([
        ("1.", "**Read** this week's **newsletter**"),
        ("2.", "**Spread** our **gospel**."),
        ("3.", "When a person (a **Fed**) calls you out for being **extremely misinformed**, throw a **hissy-fit-tantrum** towards the person that called you out, and **na-na na-na boo-boo** them to oblivion."),
    ], "#ffe81f", bold=False, size=17)
    + wp("It’s **10 am** Eastern Standard Time on a **Wednesday**. Welcome **Home**.")
    + wp("**Domo Arigato,**")
    + wp("**P.S.** If you forward this email to **three people** and those **three people** forward it to **three more people**, and so on/so forth. We could create our own **pyramid scheme**. You make **money**, we make **money**, we all make **money**. We would like for that to happen.")
    + wp("**Domo Arigato,**", "margin:0 0 10px;")
)
welcome = welcome[:a] + new_paras + welcome[b:]

# ---------------- WAIVER WIRE ----------------
waiver_paras = [
    "**We**, as in **all** of **us**, are adding Reality Television to the starting lineup this week.",
    "A couple of days ago, **Sam Hartman** (**my crush**), was selected to become the newest **Bachelor**.",
    "You have no idea how much this affects my **day to day** life. The last time I watched spicy reality TV was Total Drama Island, but I'm willing to step out of my shell, to watch Sam Hartman **literally** do anything.",
    "I **pray** every night before I go to bed. I only say **one thing**.",
    "**“Lord, why does my face not look exactly like the all-time leading passer in Wake Forest Demon Deacons football history, throwing for 12,967 career passing yards?”**",
    "Not one response from the **guy** upstairs. Ever.",
    "I love my father. **That being said**, I fully **blame him** for the way I look. Could I **eat** better, **sleep** better, workout at least **once a week**, consider a hygiene routine that isn’t only **Suave Kids green apple 3 in 1**, and drink water instead of my daily intake of 8 cups **blueberry** faygo, and 2 cups **half n half**?",
    "**Sure.**",
    "I could change all of those things to look **slightly better**. But I won't because altering a routine is hard, and I like **blaming other people** for the actions that I cause for **myself**. My **dad** should look like the reincarnation of **Poseidon** mixed with Terry Crews, but instead he’s just a regular **Six-foot-four** white guy from DC.",
    "I’ll just wait for my **second puberty.** After my second puberty, I'll be six-foot-five, and look exactly like **Sam Hartman**.",
]
waiver_body = "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_paras)
waiver = f'''        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-blue" style="border:3px solid #00c6ff; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:12px;">
                    Waiver Wire Week Nine: Reality Television
                  </div>
                  <img src="{IMG}waiver-wire-bachelor.jpg" width="300" alt="The Bachelor: Sam Hartman" style="display:block; width:300px; max-width:100%; height:auto; margin:0 auto 18px; border-radius:8px;">
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
book_inner = (
    p("**Comfort.**", "margin:0 0 16px;")
    + p("The feeling of **safety**. I feel safe in most places, and in unsafe places, I do things that increase the safety of my surroundings.", "margin:0 0 16px;")
    + listtable([
        ("1.", "When on a **rollercoaster**, I put the harness on so I don’t **fall** off."),
        ("2.", "When at **Chipotle**, I order **sour cream** if I get the **hot red salsa**, so I don’t **die**."),
        ("3.", "When I go for my **nightly walk** around my **quiet suburban neighborhood** I bring my **12.25-inch chrome-lined barrel draco**, so I don’t engage in small talk with Mary Sue and her **white rat dog**."),
    ], YEL, bold=False)
    + "".join(p(t, "margin:0 0 16px;") for t in [
        "There is one thing that does absolutely nothing for me when I feel **unsafe**, suspended **30,000 feet** in the air, flying almost at the speed of sound.",
        "The safety booklet on an airplane.",
        "I was forced to read one of these **bad boys** this weekend, when my forty-five-minute flight was grounded on the tarmac for **five hours**. My phone died **two hours** into this sitting **marathon**, and during that time I was **forced** to read through a **safety-booklet** out of sheer boredom.",
        "I realized that airplane safety is straight up fucking **propaganda**. It’s just there to make passengers feel they have some control over their destiny, when in fact they have **none**. A flight is the one place where you’re furthest from control. My life is directly in the palm of this **drunk** pilot’s hand.",
        "Why do planes even offer a safety instructions booklet, other than the fact that the animated characters **sliding** down the slide, and breathing through the **oxygen masks** are kind of fun to look at.",
        "**Also,** why do flight attendants make it seem like the plane is going to nosedive into the side of a mountain if you don’t put up your **tray table**, and put your seat back to the **upright position**. I guess the **five degree difference** in the angle of a chair will in fact make this plane crash. I say all of this, but I still do what they say because I dislike confrontation, and I am a serial rule follower**/pushover**.",
        "**Doubly also**, what the fuck are seatbelts gonna do when the plane does decide to **crash**. I’m completely done for. When it does happen, my life flashes before my eyes, and I realize that every single decision I have made in this life led up to me choosing to write **a weekly satirical newsletter**.",
        "Yikes.",
        "All of my memories are flooding back, and my memories aren't even that cool. My biggest milestone growing up was pulling a **Most Feared Brian Dawkins** in a Madden Mobile **Pro Pack** during 7th grade lunch.",
        "When this hypothetical plane is crashing due to my phone not being on airplane mode, the last song I would be listening to would be **“Boston - Sped Up”** by Stella Lefty. It’s the only downloaded song on my phone, don’t ask.",
        "My last meal would be **gluten free pretzels, a biscoff cookie, and a diet coke**. Probably could've gone with the **regular coke**, and pretzels with **real flour**.",
        "The very last thing I do on this earth minus crash landing is win my **57th Retro Bowl Championship**, and scroll through the entirety of my camera roll.",
        "I really hope this never happens. It probably isn't. My uncle says you're more likely to get struck by **lightning three times**, and get eaten **by a shark** on the same day, than to die in a plane crash.",
        "**But that’s like the coolest way to die** that I have ever heard. I would definitely rather get struck by lightning three times and fight off a shark until the **bloody** end, then have my last meal be a **biscoff cookie** and a **diet coke**.",
    ])
    + p("**3/10 I like the blue gradient. Idk.**", "margin:0;")
)
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
                        <img src="{IMG}book-american-airlines-safety.jpg" width="220" alt="American Airlines safety instructions booklet" style="display:block; width:220px; max-width:100%; height:auto; border-radius:4px;">
                      </td>
                    </tr>
                    <tr>
                      <td align="center" style="padding-top:10px; font-family:Verdana, Geneva, sans-serif; font-size:13px; line-height:1.5; color:#ffffff;">
                        American Airlines Safety Instructions Booklet &middot; Rating: 3/10
                      </td>
                    </tr>
                  </table>
                  <div style="font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:{YEL};">
{book_inner}                  </div>
                  <img src="{IMG}book-week-nine-safety-pages.jpg" width="100%" alt="Inside the safety instructions booklet" style="display:block; max-width:548px; height:auto; margin:20px auto 0; border-radius:8px;">
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- OFF THE DOME ----------------
OTD = "#6ec6ff"
otd_paras = [
    "I am productive. I do my work on time, all the time. Because I am elite, and I am better than you.",
    "I also now have an Adderall prescription for my late-onset-post-college-ADHD. Not to scare you but this is the equivalent of giving Dwayne The Rock Johnson steroids.",
    "It’s probably actually more like giving Pete Davidson steroids, but he still just sits down on the couch all day and doesn’t work out.",
    "But.",
    "Nonetheless.",
    "That Adderall stuff gets me moving smoother than Will Smith in Hitch. I have a fully color-coded (blue and green) Google Calendar, I deep cleaned my car’s cupholders (those things can get dirty) and I made sure to open every single email on my email. 10,678 unanswered emails. It never bothered me until now, actually it didn’t even bother me but it bothered other people, who bother me.",
    "My life is now perfect with over-the-counter meth, but I have one problem. Adderall makes me continuously wired to the point where I cannot sleep.",
    "I hit the perfect presleep regimen: Brush teeth, Dude Perfect Basketball Stereotypes Video, eat copious amounts of peeps to hopefully put myself in a food coma, and then scroll on YouTube Shorts (I deleted Insta) before I hit the light and try to fall asleep in my racecar bed. But for some reason the adderall has been making it damn near impossible for this unequivocally impeccable strategy to work.",
    "I mean you would think that I have exhausted my dopamine receptors enough to where I wouldn’t have a damn thing to think about, forcing my body to just shut off and enter REM.",
    "But no.",
    "I have tried other strategies, such as listening to intense Carl Jung philosophy and doing military breathing techniques. To no avail. Carl Jung told me to confront my shadow self. My shadow self was also awake. We made eye contact and neither of us blinked, it was really freaky and I am thoroughly unsettled.",
    "This led me to fall back to the original method of getting some good solid shut eye.",
    "I have started to count sheep, and now I don’t think I can get them out of my head. I constantly see their faces. Sheep upon sheep upon sheep. Stacking on top of each other, watching me, staring at me, every time I close my eyes.",
    "Typing this now I am getting the shivers. I can’t seem to escape them, but it isn’t only the sheep that is driving me insane.",
    "Have you ever tried to see how high you could count up to?",
    "Like sure everyone knows what the really big numbers are, but have you ever actually counted them, and not only have you counted, but have you counted them as if they were sheep. Have you ever counted so many sheep that you couldn’t count anymore so you go back to the beginning and you count them with a name. Sheep 4,000 I have named Brenda, Sheep 4,001 is also named Brenda.",
    "That was an honest mistake but I couldn’t take it back because both Brendas really seemed to like their names. Once I got up to the 10,000s I started to give them job titles. Mike from HR is confused why he isn’t the top sales associate and Jim is just glad that he has a job, he’s the janitor. But he’s the janitor everyone likes and says what's up to. Not the one who gives you mean glances and makes you feel horrible, that would be Trisha. Stay away from Trisha.",
    "I can’t even tell you what number I got to because I was actually able to fall asleep, all I know is that I can see the sheep still, and they are haunting me. Not in a scary way. But more in a passive aggressive sneak diss type of way. I close my eyes and one of them says “per my last baaa.” Since when have the sheep gone corporate?",
    "But they shouldn’t be able to haunt me because I am the wolf among them. It’s on my lock screen. I didn’t even choose my lock screen. It chose me.",
    "Anyway, I slept four hours, took my Adderall, and answered all of my emails and completed my tasks for the day. It is 10am. And that is why I am writing this now.",
    "I am the Rock on roids. The sheep are watching. I must work hard for them. For Jim.",
]
otd = f'''        <!-- ================= SECTION: OFF THE DOME ESSAY ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-purple" style="border:3px solid #7a2bd0; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:28px 26px;">
                  <div class="glow-gold" style="color:#ffd700; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    This Is Off The Dome But I didn&rsquo;t know how high I could count until I tried to fall asleep after taking adderall.
                  </div>
                  <img src="{IMG}off-the-dome-week-nine.jpg" width="100%" alt="A wide-awake man in bed counting numbered sheep jumping a fence" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
                  <div class="glow-blue" style="color:{OTD}; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:15px; line-height:1.7;">
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
    "The year is 1665 and Sir Isaac Newton has been sent home due to the plague, here he developed the beginnings of calculus and created laws about how we move. Newton literally invented math out of spite. Some call him: the first white boy in motion, and according to the second law of thermodynamics, once a white boy is in motion, a white boy stays in motion.",
    "His motion crossed boundaries and transcended the standards that we are held to. In fact he created the standards of motion. He also got hit in the head with an apple and called it research. Legend.",
    "Now flash forward to music, April 1964. The Beatles held five top spots on the Billboard Hot 100 at once. Now I wasn’t alive, and only two of them still are, but their music has been passed down from generation to generation like russian nesting dolls. All that’s been passed down in my family for generations has been the inevitability of getting a massive widow's peak.",
    "They created the music that I can drunkenly sing into the face of the love of my life at my local Bdubs.",
    "“I WANT TO HOLD YOUR HAND”",
    "“No, I've seen you drink like 8 wild herds.”",
    "“THEY HAD A $3 DRAFT DEAL. LET IT BE! LET IT BE!”.",
    "Nonetheless, the Beatles? Still in motion.",
    "A year later. 1965, the godfather of all investing, the man who created the pipeline, the lax bro before lax bro’s and the pump and dumper who didn’t have to pump and dump: Warren Buffett gained control of Berkshire Hathaway and pivoted away from textiles into a massive multinational holding and investment conglomerate.",
    "He stayed in motion, and now has since retired, leaving space for one man to fill his void. One white boy whose motion must break the bounds of science, song, and compounding interest. Someone who can be a vampire, batman, wizard, backwards agent in an indescribable mind-fuck of a movie, bank robber, lighthouse keeper, space clone, preacher, heart throb, and an evil sci-fi villain all in one. I don't even think he is doing this for work, it seems more like he’s just making sure that he has enough costumes for Halloween.",
    "Pretty soon they’re gonna ask him to do the Denzel Washington biopic, and he’ll probably win an Oscar for it.",
    "And he does all of this whilst looking malnourished and like he hasn’t slept since 2008. He’s literally method acting by being alive.",
    "Newton had gravity. The Beatles had the charts. Buffett had compound interest. Robert Pattinson has all three, plus a jawline that could cut glass, and he still talks like he has no idea what he is doing anymore. It is so ridiculously cool.",
    "Robert, if you’re reading this: please stop. Leave some jobs for the rest of us. I really thought I was gonna be the next James Bond.",
])
fark = f'''        <!-- ================= SECTION: FARK OF THE WEEK ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box" style="border:3px solid #ff3b3b; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Fark of the week: Everyone who isn&rsquo;t Robert Pattinson
                  </div>
                  <img src="{IMG}fark-week-nine-pattinson.jpg" width="400" alt="Robert Pattinson in a tuxedo aiming a pistol" style="display:block; width:400px; max-width:100%; height:auto; border-radius:8px; margin:0 auto 20px;">
                  <div class="glow-gold" style="color:{GOLD}; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:15px; line-height:1.7;">
{fark_inner}                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''


# ---------------- VENUS ----------------
def venus_row(text, last=False):
    pad = "" if last else "padding-bottom:14px; "
    return f'''                    <tr>
                      <td style="{pad}font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:#e9d1ff;">
                        <span>{fmt(text)}</span>
                      </td>
                    </tr>
'''


venus_rows = [
    "**What was Venus Williams up to in 2024?**",
    "She started a Newsletter for her interior design company **V Starr Interiors**. She’s just like us!",
    "Almost.",
    "She stopped after **seven weeks**. V Starr only made **seven issues** 🤣.",
    "You are currently reading our **ninth issue**. We are currently beating her by **two issues**. Thank you by the way. We have no intention of stopping unlike our queen Venus.",
    "She’s probably too busy practicing for **Guangzhou** 2027 to be writing newsletters.",
    "Make sure to tune in next week to read more of our misinformed bullshit.",
    "Also we hit five hunnid weekly readers. What the fuck. V Starr probably, realistically has more but that’s not the point I was trying to make.",
    "**I love you. Yes. Specifically you. I love you so much. If you are reading this:**",
]
venus = venus_top
venus += '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">\n'
for txt in venus_rows:
    venus += venus_row(txt)
venus += '''                  </table>
'''
venus += listtable([
    ("1.", "Thank you, this week's newsletter was hella long. Our b."),
    ("2.", "Send this newsletter to more people so me and Gomas can get enough moola to start a family together"),
], "#e9d1ff", last=True)
venus += '''
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- PUBLIC DOME-AIN ----------------
subs = [
    ("Parker From Houston", "Nov 13, 2:45 AM", "“This is off the dome but I quit sports gambling so the biggest gamble in my life is whether or not i’ll be able to get it up.”"),
    ("Douglas From Baton Rouge", "Nov 13, 9:33 PM", "“This is off the dome but when girls go to the bathroom together do you think they ever go poop or just piss together?”"),
    ("Payton From New York", "Nov 14, 5:09 PM", "“This is off the dome but preparing for an all you can eat sushi is one of the most intense things in my life right now.”"),
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

# sign-off fix for this issue (the shared template says "Thx 4 for")
footer = footer.replace("Thx 4 for taking the time", "Thx 4 taking the time")
out = header + welcome + nfl_divider + waiver + d_book + book + d_otd + otd + d_fark + fark + d_venus + venus + d_pub + pubdome + footer
open(ROOT + "newsletter-9.html", "w", encoding="utf-8").write(out)
print("written", len(out))
