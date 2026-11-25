"""Builds Issue #10 (The FitnessGram Pacer Test): reads newsletter-6.html as a template,
keeps the shared header/dividers/footer, and regenerates each section from the
text defined below. (The unused Gmail dark-mode helpers live in
build_newsletter_7.py.)
WARNING: running this OVERWRITES newsletter-10.html.
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
header = header.replace("Written From The Hip &mdash; Bad Haircut", "Written From The Hip &mdash; The FitnessGram Pacer Test")
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
        f'                      <tr><td valign="top" style="padding:4px 0; width:34px; font-family:Verdana, Geneva, sans-serif; font-size:{size}px; color:{color};">{n}</td>'
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
    + wp("**Read** this **now**.")
    + wp("**But** tomorrow, on **Thanksgiving**, interrupt your parents' toast on what they are “**thankful**” for and read this newsletter **word for word**. I guarantee your loved ones will think of you **differently**.")
    + wp("That is a **good** thing.")
    + wp("This is issue number **10**. We are a **decade** old. At **issue 24** I'll get my **first kiss**. At **issue 25**, my brain will reach full development and **stop maturing**. In **30 issues** you, yes you, the reader reading this right now, will be **dead**. In **40 issues** I'm gonna **think** about starting a family. In **58 issues** I'll start the True Detective Season 1 rewatch. This newsletter will **end** when I stop **think**ing of new things. That number is un**think**able to think about at this moment with my underdeveloped decade old newsletter **brain**.")
    + wp("It’s the day before Thanksgiving. What have you done to prepare?")
    + wp("Me?")
    + wp("Literally nothing. This year is finished in thirty five days and I've accomplished **jack** shit.")
    + wp("It’s **10 am** Eastern Standard Time on a **Wednesday**. Welcome **Home**.")
    + wp("**Domo Arigato,**")
    + wp("**P.S.** If you forward this email to **three people** and those **three people** forward it to **three more people**, and so on/so forth. We could create our own **pyramid scheme**. You make **money**, we make **money**, we all make **money**. We would like for that to happen.")
    + wp("**Domo Arigato,**", "margin:0 0 10px;")
)
welcome = welcome[:a] + new_paras + welcome[b:]

# ---------------- WAIVER WIRE ----------------
waiver_paras = [
    "**This week** we are adding **cold plunges** to the **starting lineup**.",
    "Every **CEO** in the history of mankind **starts** their day with a **cold plunge**.",
    "I am also **one** of those **people**.",
    "For **two** entire days in a row I did a **cold plunge**. This is due to the fact that my new apartment has seemingly run out of **hot water**.",
    "I have been forced to take **a daily cold plunge everyday** first thing in the morning. This has also led me to wake up at **5 am** before all of my roommates. **Not** because I feel as if I am better than them, but because I need to wake up before them so I can score **the first hot shower**.",
    "It turns out that we **straight up** don't have hot water, so now I **technically** wake up at **5am** and do **cold plunges** which literally makes me a **CEO**.",
    "My New **CEO** morning routine:",
]
routine = [
    "**5:00 am**- Check to see if the **water** is **hot**, it isn't. **Guttural** scream.",
    "**5:05 am**- Go back to bed for a much needed **shut** of the eye.",
    "**5:05-8:00 am**- **Meditation**/Prayer/**Visualization**/Sleep.",
    "**8:00 am**- I wake up to the sound of my custom alarm “**Barking** Dogs and **Breaking** Glass.”",
    "**8:05-8:10 am**- **Hop** in the cold shower **plunge**. Feel the **divers' reflex**. Release the second **guttural** scream. **Dopamine** and serotonin course through my body.",
    "**8:10-8:50 am**- Kickstart the **circadian** rhythm by staring into the **naturally** occurring **blue light** of my phone, and I **ground** myself under my **sheets**.",
    "**8:55 am**- **I rise**. I commute to the desk in my room.",
    "**9:00 am**- Begin my highly **replaceable** job.",
]
waiver_after = [
    "This entire time **I am fasting**, and I don’t ingest coffee or any **caffeine**. This is due to the fact that I keep forgetting to buy groceries, and my Keurig is on the **fritz**.",
    "That’s **my 5-9 before my 9-5**. I also just found out that I was using my shower handle completely wrong. We had hot water the entire time.",
    "**Whoopsy**.",
    "At least I know exactly what a **CEO** does to start their morning.",
]
waiver_body = (
    "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_paras)
    + "\n                    <br><br>\n"
    + "\n                    <br>\n".join("                    " + fmt(t) for t in routine)
    + "\n                    <br><br>\n"
    + "\n                    <br><br>\n".join("                    " + fmt(t) for t in waiver_after)
)
waiver = f'''        <!-- ================= SECTION: FANTASY FOOTBALL WAIVER WIRE ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-blue" style="border:3px solid #00c6ff; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:19px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:12px;">
                    Waiver Wire Week 10: Cold Plunges
                  </div>
                  <img src="{IMG}waiver-wire-cold-plunges.jpg" width="400" alt="A man sitting in a cold plunge tub" style="display:block; width:400px; max-width:100%; height:auto; margin:0 auto 18px; border-radius:8px;">
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
    "I was looking around my **childhood** room for inspiration for this week and I found the book Moneyball sitting on my bedside table. The only thing I remember from **Moneyball** was that in the movie, **Brad Pitt** was talking with his mouth **full of food** in every single scene.",
    "This reminded me of a story of when I ventured off with my four closest friends to the new **gentrified food** spot in my **second-tier city.**",
    "We got the **twenty four-dollar** shareable fries with the **eight-dollar** truffle oil and parmesan cheese add-on. Our burgers arrived on **individual metal trays**, and we decided to order a **transfusion tower** that came out to three normal-sized transfusions for double the cost. When the waiter came with the bill, we all ended up paying **$87.34 each before tip**. **Walking back** to our shipping container apartment, we all realized we had spent almost a **hundred dollars** to be neither **full nor drunk**, and my friend looked into my **piercing blue** eyes and said, \"**That's Baseball**\", a quote from Yankees play-by-play legend **John Sterling**.",
    "That is in fact baseball. Akin to \"**That's life**,\" a quote from someone **less famous** and **less New York** than Yankees play-by-play man John Sterling, it's unexpected. Life, like baseball, is strange in many ways, but taking a step back, **I fucking hate baseball**. Try to describe baseball to someone who has never seen the sport. **You can't**. There is no time limit. They give **kids metal** bats, but when those kids grow up to play in the **MLB** they are forced to use **tree trunks** to swing at pitches that reach you faster than you can blink.",
    "The names of the pitches sound like **Kama Sutra** positions. Imagine hearing a **coach** tell your son that he needs to make contact on his **slurve ball**. This parent is also paying **three grand** for their little tyke to be **groomed** on this travel team.",
    "The best case scenario is for your kid to go pro for the **Savannah Bananas** or the Loco Beach Coconuts.",
    "**What game are we playing here?** Then, right when you are getting used to this weird, perverted sport, the **seventh-inning stretch** happens, and you are forced to stand up and sing \"Take Me Out to the Ball Game\" like it's some sort of forced **baseball propaganda**.",
    "\"Buy me some pea**nuts** and **Crack**er Jack, I don't care if I never get back.\" **Back to what**? Your life without baseball? Baseball is literally called \"**America's Pastime**,\" so the only other time in your life that isn't baseball is your job.",
    "Imagine you are **Adam Scott** in **Severance**, and every time you leave your job, your **outie** is at a **baseball game**. That is what **Rob Manfred** and **Big Baseball** want.",
    "Remember that the next time you are supporting your **second-tier city's** Triple-A team that is named after a **niche regional food**.",
]
book_inner = "".join(p(t, "margin:0 0 16px;") for t in book_paras) + p("**1/10 That's baseball.**", "margin:0;")
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
                        <img src="{IMG}book-moneyball.jpg" width="220" alt="Moneyball by Michael Lewis book cover" style="display:block; width:220px; max-width:100%; height:auto; border-radius:4px;">
                      </td>
                    </tr>
                    <tr>
                      <td align="center" style="padding-top:10px; font-family:Verdana, Geneva, sans-serif; font-size:13px; line-height:1.5; color:#ffffff;">
                        Moneyball by Michael Lewis &middot; Rating: 1/10
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
OTD = "#6ec6ff"
otd_paras = [
    "Endurance. Speed. Grit.",
    "Those three things all come from one aerobic fitness test that we were all forced to participate in every year.",
    "I woke up in a sweat. My heart was racing. I threw up in my bed. I went to my roommate's room to tell him that I threw up. He woke up in a scream. The scream scared me. I started to cry. He wiped the tears off my flushed red cheek. He changed my sheets, warmed me up some milk, flipped on some Workaholics and held me until I was able to fall asleep again.",
    "The only thing you’re wondering right now is what made me wake up with a racing heart, a sweaty forehead, and a slight cough from a dry throat that only comes from endurance activities inside of a cold indoor gym.",
    "I had a nightmare about the FitnessGram pacer test.",
    "I was having an amazing dream. I was in a rocketship with Ashley Tisdale, London Tipton, Moseby, and Tony the Tiger. We left Earth to start a new life on Mars.",
    "The next thing I know I was in P.E. in fifth grade. My stomach has an absolute brick in it due to the fact that I’m fresh off of a 10am lunch of pizza, 2% milk, and a Choco Taco. My stupid fucking P.E. coach tells us we have the pacer test today when he clearly said we were going to play Musical Hula-Hoops yesterday.",
    "“You’re a fucking bastard!” I yell directly at his face. What is he gonna do? Send me to the principal? He’s the P.E. teacher. He’s got skeletons in the closet for sure.",
    "Me and my fellow comrades line up in absolute fear. We then hear the overhead speakers.",
    "“The FitnessGram Pacer Test is a multi-stage aerobic capacity test that progressively gets more difficult as it continues.”",
    "Please god help me.",
    "“The 20 meter pacer test will begin in thirty seconds.”",
    "I look around at my competitors. Pull up my Nike elite socks to my kneecaps and get ready for the reckoning.",
    "“The running speed starts slowly but gets faster after you hear this signal, beeeep”",
    "My knees begin to buckle. The Nike elites are cutting off my much needed circulation.",
    "“The second time you fail to complete the lap before the sound…your test is over.”",
    "In other words if you stop running that literally means you’re fatter and slower than everyone else that is still running. This is practically the purge for fifth graders.",
    "“On your mark, get ready, start”",
    "I start slow. The last time I started in a full sprint, and absolutely got routed.",
    "“One”",
    "I’m gonna skip to ten to move this story forward.",
    "“Ten”",
    "I’ve run the equivalent to forty marathons in my brain. I look around, and no one has been eliminated except the rotund one.",
    "“Twenty”",
    "“Thirty”",
    "“Forty”",
    "At this point I'm sprinting back and forth, choking over my breath. I can’t take it anymore. Free me from these chains that I provided for myself. My social acceptability is based on how high my score is so I keep going.",
    "I never stop until the pacer test buzzer fills every second.",
    "Then I wake up screaming. It’s a pretty terrible nightmare.",
    "It happens to me every third week of November. It only occurs to me because my family forces me to the turkey trot with them, and waking up on that Thursday to run/walk three miles is the hardest thing I accomplish every year.",
    "I earned the turkey, mashed potatoes, ambrosia salad, and the pickled radicchio jello tower.",
    "But at what cost?",
    "I was coddled by my roommate because of my FitnessGram pacer test nightmare.",
    "It’s awkward now between me and the roommate.",
]
otd = f'''        <!-- ================= SECTION: OFF THE DOME ESSAY ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box glow-border-purple" style="border:3px solid #7a2bd0; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:28px 26px;">
                  <div class="glow-gold" style="color:#ffd700; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    This Is Off The Dome But I just had a nightmare about the FitnessGram Pacer Test
                  </div>
                  <img src="{IMG}off-the-dome-week-ten.jpg" width="100%" alt="A cartoon hand holding a page that reads: The FitnessGram pacer test is a multistage aerobic capacity test" style="display:block; max-width:548px; border-radius:8px; margin-bottom:20px;">
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
    "So the other day I was scrolling through Facebook marketplace on my computer, a great activity if bored on a Sunday afternoon, and all of a sudden I got an alert that a hot girl had requested to follow me. Fuck yeah… Fuck no. Who is a hot girl on Facebook Marketplace? What is she selling? Why does she want to follow a man looking through used couches and cars that I would never buy?",
    "My screen blew up like I was getting hacked by a Russian who lives 60 feet below ground. A robot lady started chanting out of my computer saying gibberish I couldn’t fathom before eventually stating that my computer was compromised.",
    "I haven't been compromised since that one time in middle school when I looked up something I shouldn’t have about Bella Thorne on my school-issued chromebook. The librarian never said anything but looked at me differently for years.",
    "Anyways, I did what any responsible adult does and I called my good friend Jensen Huang to help me save my computer.",
    "He told me he knew exactly how I felt. A woman said hi to him and things got romantic, and allegedly she was a Chinese spy (he allegedly had four other affairs, but who’s counting? Not us! Allegedly). I have to say allegedly because Nvidia has more lawyers than we have subscribers.",
    "Well the roleplay backfired because like me having my computer compromised, his job was compromised. Apparently sexy spy vs tech mogul with cool leather jacket was a little too intense and it ended up getting out in the news.",
    "Fucking so sick, but what could his wife possibly be thinking — I just looked it up and she wants to save their marriage.",
    "I mean what a fuckin keeper. Forty years of marriage (four alleged affairs) and she’s still in. I had a girl leave me because I ate too much yogurt and rotisserie chicken.",
    "Jensen, we at Written From The Hip would like to formally apologize for calling you a Fark. People fail, Chinese spy agencies will soon fail, computers do not and Jensen Huang is my hero.",
    "This leaves one Fark this week. Me. A man on Facebook Marketplace with a frozen computer and thoughts of Bella Thorne.",
])
fark = f'''        <!-- ================= SECTION: FARK OF THE WEEK ================= -->
        <tr>
          <td class="wfth-pad" style="padding:0 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="section-box" style="border:3px solid #ff3b3b; border-radius:10px; background-color:#050505;">
              <tr>
                <td style="padding:24px 26px;">
                  <div class="glow-red" style="color:#ff3b3b; font-family:Verdana, Geneva, sans-serif; font-weight:700; font-size:20px; text-transform:uppercase; letter-spacing:0.03em; text-align:center; margin-bottom:16px;">
                    Fark of the Week 10: ME&hellip; Gomas. lemme explain rq
                  </div>
                  <img src="{IMG}fark-week-ten-gomas.jpg" width="300" alt="Gomas in a firefighter helmet and sunglasses" style="display:block; width:300px; max-width:100%; height:auto; border-radius:8px; margin:0 auto 20px;">
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


venus = venus_top
venus += '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">\n'
venus += venus_row("**It’s issue #10**. Here are the **10 things** I will do this **Thanksgiving break** to support **Venus Williams** because of how thankful I am for her being the one shining light in my life:")
venus += '                  </table>\n'
venus += listtable([
    ("1.", "Since she is **vegan**, I will abstain from eating **Turkey**. My protein source will only come from her **Happy Viking Vegan protein powder** company."),
    ("2.", "I will **burn** my family's dining room table because it isn’t **The Melbourne 54” Round Wood Pedestal Dining Table** that Venus designed for **Crate & Barrel**."),
    ("3.", "While **my family** goes to the movie theatre together to watch the new **Hunger Games movie**, I will stay home and watch **King Richard**."),
    ("4.", "Instead of playing football with my cousins I will make them play in a tennis tournament and purposefully lose in the first round. **I will do this fifteen times in a row**."),
    ("5.", "The **2026 WTA Awards season** just started. I will force every single person in my extended family to **vote for Venus** to be the 2026 WTA Singles Fan Favorite."),
    ("6.", "I will lead my family’s prayer, and only pray to the **Jehovah god** because Venus is a registered Jehovah’s witness."),
    ("7.", "My mom said that I need to go to the DMV and renew my license. While I am there I will legally change my name to Venus’ full name: **Venus Ebony Starr Williams**."),
    ("8.", "When I go Black Friday shopping for **Venus Williams memorabilia** I will not use discount codes to make sure I pay **full price** so as much money as possible can go straight to Venus."),
    ("9.", "Instead of watching football I will watch Venus’ 2026 **Guangzhou** first round match against Lilli Tagger and take notes with a purple (**her favorite color**) crayon."),
    ("10.", "I will read the book cover of Venus’ New York Times Best Seller, **Strive: 8 Steps to Find Your Awesome.**"),
], "#e9d1ff", bold=False)
venus += '                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">\n'
venus += venus_row("How will you be **thankful** for Venus this **Thanksgiving**?", last=True)
venus += '''                  </table>

                </td>
              </tr>
            </table>
          </td>
        </tr>

'''

# ---------------- PUBLIC DOME-AIN ----------------
subs = [
    ("Collin From Dallas", "Nov 21, 4:45 PM", "“This is off the dome but nukes are such an insane thing to invent. Like what was Oppenheimer's end game?”"),
    ("Derek From Ann Arbor", "Nov 22, 9:21 PM", "“This is off the dome but who the fuck still uses airplane pillows. It’s lowkey psychopathic behavior to have one clipped to your backpack at the airport.”"),
    ("Chris From New York", "Nov 23, 3:29 PM", "“This is off the dome but why did Instagram add the reposting feature. I’ve accidentally reposted some of the most insane shit publicly without me even noticing.”"),
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

# sign-off fix (the shared template says "Thx 4 for")
footer = footer.replace("Thx 4 for taking the time", "Thx 4 taking the time")
out = header + welcome + nfl_divider + waiver + d_book + book + d_otd + otd + d_fark + fark + d_venus + venus + d_pub + pubdome + footer
open(ROOT + "newsletter-10.html", "w", encoding="utf-8").write(out)
print("written", len(out))
