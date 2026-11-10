"""Builds Issue #8 (Papa's Pizzeria): reads newsletter-6.html as a template,
keeps the shared header/dividers/footer, and regenerates each section from the
text defined below. (The unused Gmail dark-mode helpers live in
build_newsletter_7.py.)
WARNING: running this OVERWRITES newsletter-8.html.
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
header = header.replace("Written From The Hip &mdash; Bad Haircut", "Written From The Hip &mdash; Papa&rsquo;s Pizzeria")
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
WRECK = "https://www.youtube.com/watch?v=Vf2szOus-pU&t=522s"
welcome = cut("        <!-- ================= SECTION 1: WELCOME", "        <!-- ================= DIVIDER: NFL")
a = welcome.index('                    <p style="margin:0 0 16px;"><strong>Yo,</strong></p>')
b = welcome.index('                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">')
open_paras = [
    ("margin:0 0 16px;", "**Yo,**"),
    ("margin:0 0 16px;", "It turns out some **people** are getting these emails in their **spam** because in the **P.S**. section we talk about you guys joining our **pyramid scheme** every week. That can’t be the **case**. If this is in your **spam** that means **we** personally don’t **fuck** with you in the **slightest**. **If this is in your** regular **inbox** we personally find you **attractive**."),
    ("margin:0 0 16px;", "**Also**… this week's newsletter is dedicated to the **29 lives** that were **lost** on the S.S. **Edmund Fitzgerald** on November 10th, 1975. **51 years** and a day **ago**. I suggest listening to the “Wreck of the Edmund Fitzgerald” by Gordon Lightfoot in remembrance. The **GoFundMe** link below goes straight to **my Venmo**. All the proceeds will go to my **TouchTunes** account, so I can play nonstop **Gordon Lightfoot** this weekend at my local bar."),
    ("margin:0 0 16px;", f"**[Teorge GoFundMe for Playing the Wreck nonstop via TouchTunes at my local bar]({WRECK})**"),
    ("margin:0 0 16px;", "It’s **10 am** Eastern Standard Time on a **Wednesday**. Welcome **Home**."),
    ("margin:0 0 16px;", "**Domo Arigato,**"),
    ("margin:0 0 16px;", "**P.S.** If you forward this email to **three people** and those **three people** forward it to **three more people**, and so on/so forth. We could create our own **pyramid scheme**. You make **money**, we make **money**, we all make **money**. We would like for that to happen."),
    ("margin:0 0 10px;", "**Domo Arigato,**"),
]
new_paras = "\n".join(f'                    <p style="{st}">{fmt(t)}</p>\n' for st, t in open_paras)
# the TouchTunes/GoFundMe link is blue instead of the surrounding yellow
new_paras = new_paras.replace('style="color:inherit; text-decoration:underline;">Teorge GoFundMe',
                              'style="color:#00c6ff; -webkit-text-fill-color:#00c6ff; text-decoration:underline;">Teorge GoFundMe')
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
    "**This week** we are adding **podcasts** to the **starting lineup**.",
    "As someone who hasn’t read a book since **To Kill A Mockingbird** in the **8th grade** (I still haven’t finished the book so don’t spoil it). **Podcasts** are pretty much the **exact same** thing as **reading**.",
    "**Podcasts** are also a great way for me to **listen** to something, **misinterpret** it entirely and **spread** that **misinformation** to the people I **love** the most everyday.",
    "I used to feel like **Boo Radley**, but after podcasts, I'm moving like **Atticus Finch** defending **Tom Robinson** in the courtroom. If you don’t get that reference you’re not smart and clearly don’t read enough **books**.",
    "**I’ve been trying out talking recently**. It turns out everything you say is true if you speak with enough confidence, and start every sentence with “I listened to this **NPR** podcast the other day and [**insert lie**].” It **literally** works every time. To be fair, I've only been talking with my **eight year old nephew** recently, but it works wonders on him.",
    "The only problem with podcasts is that they last an hour, and sound nothing like **prime 2006 Gucci Mane**.",
    "If I were to start a **podcast** with my boys I would make every episode **two minutes and thirty seconds**, start with a simple **piano** melody, then slowly build the **crescendo** into a catchy chorus, and have the background sound be a **Young Nudy x Lucki type beat** with heavy 808s, a snapping trap snare, and rolling hi-hats.",
    "That would make **podcasts** actually fun to listen to.",
]
waiver_body = "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_paras)
waiver = f'''        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-blue" style="border:3px solid #00c6ff; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:12px;">
                    Waiver Wire Week Eight: Podcasts
                  </div>
                  <img src="{IMG}waiver-wire-podcasts.jpg" width="100%" alt="Joe Rogan at The Joe Rogan Experience studio" style="display:block; max-width:548px; height:auto; margin:0 auto 18px; border-radius:8px;">
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
    "**Dreams**. If I can **recommend** one thing. It is to have a **dream journal**. Over the last week I decided to jot down what I can remember from my nightly free mind movie, and it makes the first five minutes of my day **way more entertaining** than any **AM reels scroll sesh**.",
    "I started this journey of recording my dreams because I had the amazing idea to rewatch **Sharkboy and Lavagirl** on a random **Tuesday** night, as one **does**.",
    "This movie is **absolutely ridiculously** insane in the best ways. I totally forgot that the whole movie revolves around Max’s **schizophrenic** dream journal. If I had the same **dreams** as Max, I would never want to wake up.",
    "Also.",
    "If I told my therapist that I dreamed about **riding on a banana split boat on an island made of ice cream with Shark Boy and Lava Girl in order to escape George Lopez**, I would be put into a mental institution.",
    "I fully recommend a Shark Boy and Lava Girl **rewatch**. AI wishes it could think of the things that were displayed for the **ninety-three** minute runtime.",
    "If you want to know what happened in my dreams you’d have to kill me. Just know that my dreams over the last week are a **coughing baby** to Max’s **hydrogen bomb** dreams.",
    "8/10- I like a good solid leatherbound journal",
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
                        <img src="{IMG}book-max-dream-journal.jpg" width="240" alt="Max’s Journal from The Adventures of Sharkboy and Lavagirl" style="display:block; width:240px; max-width:100%; height:auto; border-radius:4px;">
                      </td>
                    </tr>
                    <tr>
                      <td align="center" style="padding-top:10px; font-family:Verdana, Geneva, sans-serif; font-size:13px; line-height:1.5; color:#ffffff;">
                        Max&rsquo;s Dream Journal in Sharkboy and Lavagirl &middot; Rating: 8/10
                      </td>
                    </tr>
                  </table>
                  <div style="font-family:Verdana, Geneva, sans-serif; font-size:15px; line-height:1.6; color:{YEL};">
{book_inner}                  </div>
                  <img src="{IMG}book-week-eight-journal-pages.jpg" width="300" alt="Pages from Max’s dream journal" style="display:block; width:300px; max-width:100%; height:auto; margin:20px auto 0; border-radius:8px;">
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- OFF THE DOME ----------------
OTD = "#6ec6ff"
otd_intro = [
    "Education. School. Learning.",
    "These three pillars in our society are crucial for the benefits of our future. How we teach children in school creates a compounding effect on how productive our society can become. Weirdly though, grades don’t count in middle school. I mean, we get report cards to show our parents, but these fake grades do not dictate our future. My older siblings taught me this sentiment when I was in sixth grade, and it led me down an interesting path in middle school.",
    "I didn’t necessarily learn a single thing, education wise, in middle school.",
    "Instead of education, school, and learning, these were my three pillars:",
]
otd_list = [
    ("1.", "There is no better feeling than eating cafeteria pizza, TruMoo chocolate milk, and loose corn at 10:30 AM every single day."),
    ("2.", "Getting the air knocked out of you while playing two-hand-touch football is the closest thing to what death feels like."),
    ("3.", "When the teacher brings out the chromebook cart, you will play Papa’s Pizzeria/Cupcakeria/Freezeria/Burgeria. You will feel more stress than a single mother with three jobs and a mortgage to pay."),
]
otd_rest = [
    "Comfort, death, and stress. My three pillars of middle school. These are the pillars that have molded me into the man-child I am today.",
    "When my dad tries to talk to me about how stressful the \"recession\" was or whatever happened in 2008.",
    "I start by laughing in his direction.",
    "Then I describe to him the stress I had to deal with in Papa’s Pizzeria on my fifth day on the job. I had five pizzas firing, seven people waiting on pies, getting more pissed off by the second, and a line out the fucking door.",
    "You don’t know what the fuck I’ve been through… dad.",
    "Have you ever over filled the batter in Papa’s Cupcakeria, and the customer gives you a five cent tip? I’ve got a fake family to feed and fake rent. How is a five cent tip going to make a dent in my fake student loan debt?",
    "Like I'm sorry you were dealing with the “housing crisis”, but I once jammed my finger trying to get a perfect icing swirl on my cupcake, on the smallest Chromebook mousepad imaginable.",
    "All of this was happening while my world geo teacher was trying to tell me Sacramento was California’s state capital. Like no it isn’t doofus, it has to be Los Angeles.",
    "I would obtain the biggest cortisol spike imaginable while maintaining five different fully functioning restaurants. All owned by Papa. Pretty sure it was all a money laundering scheme, but I digress. Then, I would clock in to my mandatory state funded school lunch at 10:30 in the morning, where I would consume three different types of dairy. I would digest the food for a solid three minutes and have to play the most important football game of my life at recess.",
    "I’d come home from school everyday going through every single emotion this life can give you. How the fuck was I supposed to learn what a fraction is?",
    "Also, when grades started to count in High School, I used the tactics I learned from the Papa’s Restaurant games, and got serviceable grades.",
    "I know shit like Pythagoras's theorem, and I know that the Mitochondria is the powerhouse of the cell. All because I clocked into the most stressful virtual work every single day of middle school.",
    "I can fully deal with the pressures of life after college only because [coolmathgames.com](http://coolmathgames.com) existed.",
    "Shoutout Run 3 and Cookie Clicker.",
]
otd_inner = "".join(p(t) for t in otd_intro) + listtable(otd_list, OTD) + ps(otd_rest)
otd = f'''        <!-- ================= SECTION: OFF THE DOME ESSAY ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-purple" style="border:3px solid #7a2bd0; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:28px 26px;">
                  <div class="glow-gold" style="color:#ffd700; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    This Is Off The Dome But Papa&rsquo;s Pizzeria created generational stress for me when I was supposed to be learning about state capitals
                  </div>
                  <img src="{IMG}off-the-dome-week-eight.png" width="100%" alt="A line of customers waiting in Papa’s Pizzeria" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
                  <div class="glow-blue" style="color:{OTD}; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:15px; line-height:1.7;">
{otd_inner}                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- FARK ----------------
GOLD = "#ffd700"
fark_inner = ps([
    "The founder and CEO of NVIDIA, Jensen Huang, had an affair with a Chinese spy. I am entirely against having an affair, but having an affair with a super secret Chinese AI agent might be the coolest thing I have ever seen.",
    "I honestly bet Jensen fully knew that he was hooking up with a spy, and the secret agent kink thing just added to the mystique of the whole situation.",
    "The water cooler talk at NVIDIA is probably unbelievable right now. I would be so excited to go to work on Monday, and act like I knew nothing, so Janice from HR can spill this scalding hot Tea for me.",
    "“Big J did what? OMG I had NO IDEA!”",
    "NVIDIA’s stock has fallen 15% over the last five days just because Jensen was horny. That’s not right. If my CEO always wore a leather jacket and hooked up with international spies I would work so much harder, so that maybe one day, I can be just like him.",
    "Okay. Maybe not just like him. Jensen also has no prenup so the divorce means that he could lose up to 81 billion dollars. Fark! Yikes!",
    "This is a total win for Lori, his wife.",
    "I listened to this NPR podcast the other day, and they said that Alice (the secret Chinese agent) hooked up with Jensen to influence NVIDIA to channel advanced AI chips to China. That is literally a logline for the coolest Rom-Com movie of all time.",
])
fark = f'''        <!-- ================= SECTION: FARK OF THE WEEK ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box" style="border:3px solid #ff3b3b; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Fark of the week: Jensen Huang
                  </div>
                  <img src="{IMG}fark-week-eight-jensen.jpg" width="320" alt="Jensen Huang and his wife Lori on the big screen" style="display:block; width:320px; max-width:100%; height:auto; border-radius:8px; margin:0 auto 20px;">
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
    "**This week in Venus Williams history**: She made her **WTA pro debut** in the **Bank of the West** Classic at the age of 14. Kind of a **wild name** for a tournament, but I digress once more.",
    "At **14** I was **a 4’7” 8th grader** scamming my friends out of their hard earned **Madden Mobile coins**. I’m pretty sure I was still using the **“L” trick** on my hands to know the difference of my **left from right**.",
    "The **14** year old Venus beat NCAA champion **Shaun Stafford** in straight sets in the first round, and barely lost to the world number one player, **Arantxa Sanchez Vicario** in the second round.",
    "At **14** I was **technically** playing sports. I guess. **I was a third string wide-out** on my middle school tackle football **C-team**. If I were to catch a ball over the middle and the world number one line backer, **Ray Lewis**, tackled me. **I wouldn’t be here today**. Luckily, my parents made me quit football in high school due to my short stature, so I could play a real sport, **Lacrosse**.",
    "Being a pro at **14** is crazy. **Kudos** to my girl **Venus**. This is why Venus is my **goat**. She also went pro before her sister Serena which means that she is better than her in every way.",
]
venus = venus_top
venus += f'''                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">
                    <tr>
                      <td width="50%" valign="middle" style="padding-right:6px;">
                        <img src="{IMG}venus-week-eight.jpg" width="100%" alt="A young Venus Williams hitting a backhand" style="display:block; width:100%; height:auto; border-radius:8px;">
                      </td>
                      <td width="50%" valign="middle" style="padding-left:6px;">
                        <img src="{IMG}venus-week-eight-me.jpg" width="100%" alt="Me at 14 holding a lacrosse trophy" style="display:block; width:100%; height:auto; border-radius:8px;">
                      </td>
                    </tr>
                  </table>
'''
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
    ("Sarah From Charlotte", "Nov 7, 9:56 PM", "“This is off the dome but why is the balloon emoji 🎈 lowkey sad as fuck. Like it’s a balloon you give to someone who is about to die. 🎈”"),
    ("Dom From Charleston", "Nov 8, 2:33 AM", "“This is off the dome but sometimes I stare into onions I'm cutting to remember what a tear down my cheek feels like.”"),
    ("Ben From Spartanburg", "Nov 9, 7:39 AM", "“This is off the dome but if you leave someone a voicemail it better be good cus what if you die and that’s all they have to remember you by.”"),
]
EDITOR_NOTE = "WFTH Editors note: these are all sad as fuck, I hope you guys are all good. Please submit happier ones this week."
sub_rows = ""
for i, (n, t, q) in enumerate(subs):
    last = i == len(subs) - 1
    border = "" if last else " border-bottom:1px dashed #6b2222;"
    note = (f'\n                        <div style="font-family:\'Courier New\', Courier, monospace; font-weight:700; font-style:italic; font-size:13px; line-height:1.4; color:#ffff33; margin-top:14px;">{e(EDITOR_NOTE)}</div>'
            if last else "")
    sub_rows += f'''                    <tr>
                      <td style="padding:12px 0;{border}">
                        <div style="font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:#ffff33; margin-bottom:4px;">{e(n)} on {e(t)}</div>
                        <div style="font-family:'Courier New', Courier, monospace; font-weight:700; font-size:16px; line-height:1.5; color:#ff0000;">{e(q)}</div>{note}
                      </td>
                    </tr>
'''
open_tag = '                      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="left">\n'
i0 = pub_section.index(open_tag) + len(open_tag)
j0 = pub_section.index("                      </table>\n                    </td></tr>")
pubdome = pub_section[:i0] + sub_rows + pub_section[j0:]

out = header + welcome + nfl_divider + waiver + d_book + book + d_otd + otd + d_fark + fark + d_venus + venus + d_pub + pubdome + footer
open(ROOT + "newsletter-8.html", "w", encoding="utf-8").write(out)
print("written", len(out))
