/* ============================================================================
   WRITTEN FROM THE HIP — site configuration
   ----------------------------------------------------------------------------
   THIS IS THE ONLY FILE YOU NEED TO EDIT.
   Change a planet's name, color, position, page text or links right here and
   every page of the site updates automatically. Save, refresh the browser.

   Rules of the road:
     - Keep the quote marks and the commas where they are.
     - "id" must stay lowercase-with-dashes and must be unique. It is what the
       page URL uses, so if you change an id, old links to that page break.
     - x and y are percentages of the star field: x 0 = far left, 100 = far
       right. y 0 = top, 100 = bottom. The moon sits at 50 / 47.
   ========================================================================== */

const SITE = {
  /* ---- the moon in the middle ------------------------------------------- */
  title: "Written From The Hip",
  issue: "I", // the small mark under the title on the moon. "" hides it.

  /* ---- the small red links under the star field on the home page -------- */
  footerLinks: [
    { label: "Subscribe", href: "page.html?p=subscribe" },
    { label: "Archive", href: "page.html?p=archive" },
    { label: "Contact", href: "mailto:hello@writtenfromthehip.com" },
  ],

  /* ---- the tiny print at the bottom of every page ----------------------- */
  legal:
    "WRITTEN FROM THE HIP, characters, names, and all related indicia are trademarks of the author. \u00A9 2026",

  /* ---- writer bios, opened by clicking a photo/name on a roster ----------
     "id" is what bio.html?b=<id> looks up. "stats" renders as a trading-
     card style list, in order.
  ------------------------------------------------------------------------ */
  bios: [
    {
      id: "george-denby",
      name: "George Denby",
      photo: "assets/images/george-denby.png",
      stats: [
        { label: "Team", value: "Shanghai Sharks" },
        { label: "Position", value: "Shooting Guard" },
        { label: "Height", value: "6' 1\"" },
        { label: "Weight", value: "180 lbs." },
        { label: "Born", value: "10/30/03, Atlanta, Georgia" },
        { label: "College", value: "Wake Forest" },
      ],
      statLine: {
        columns: ["Season", "G", "Min", "Beers", "FG", "3pt", "FT", "Reb", "Ast", "Stl", "Blk", "Tot", "PG"],
        rows: [
          ["25-26", "82", "3090", "1765", ".495", ".427", ".834", "543", "352", "180", "42", "2491", "30.4"],
          ["CAREER", "766", "29600", "48992", ".512", ".332", ".844", "4879", "4377", "2025", "739", "24489", "32.0"],
        ],
      },
    },
    {
      id: "thomas-bolt",
      name: "Thomas Bolt",
      photo: "assets/images/thomas-bolt.png",
      stats: [
        { label: "Team", value: "Guangdong Southern Tigers" },
        { label: "Position", value: "Power Forward" },
        { label: "Height", value: "6' 4\"" },
        { label: "Weight", value: "200+" },
        { label: "Born", value: "2/17/63, Brooklyn, New York" },
        { label: "College", value: "Wake Forest" },
      ],
      statLine: {
        columns: ["Season", "G", "Min", "Beers", "FG", "3pt", "FT", "Reb", "Ast", "Stl", "Blk", "Tot", "PG"],
        rows: [
          ["25-26", "61", "1850", "823", ".401", ".298", ".712", "210", "96", "54", "18", "1102", "18.1"],
          ["CAREER", "402", "14200", "21340", ".418", ".311", ".733", "1890", "1024", "512", "201", "9876", "19.6"],
        ],
      },
    },
  ],

  /* ---- full scripts, opened from a planet's page links -------------------
     "id" is what script.html?s=<id> looks up. "body" is plain text \u2014 line
     breaks are kept as-is, so paste the script in exactly how it should read.
  ------------------------------------------------------------------------ */
  scripts: [
    {
      id: "real-steele-cuck",
      title: "Real Steele Cuck",
      body: `INT. BAR NIGHT

Charlie and his robot Atom are at the bar drinking heavily,
this is five years after the championship bout against Zeus.

                    CHARLIE
          Can you make me two side walk
          slammers but just the beer.

                    BARTENDER
          So just the malt liquor no four
          loko.

                    CHARLIE
          Uh. Yea no duh. Geez, that is
          literally what I asked for.

The Bartender pours the drinks for Charlie and Atom. Like in
the movie, Charlie is wearing a glove that controls Atoms
moves.

The two get their malt liquor, and as Charlie takes a giant
swig of the drink, atom mimics him because he is controlled
by the glove.

                    CHARLIE (CONT'D)
          God, I love controlling you out in
          public. Having a drinking pal like
          you is all a man can ask for.

The man and the robot put both hands behind their head in a
cool way.

                    CHARLIE (CONT'D)
          Hey, bartender lady, do you think
          its cool that I can control my
          robot like this?

They do a sick connected arm wave and bow, as they bow they
both simultaneously take off there fedora, flip the hat over,
and ask for tips.

                    BARTENDER
          I mean, you come here every day,
          and show off that you can
          forcefully make your robot drink
          with you. It's kind of sad,
          everyone here thinks you have no
          friends.

                    CHARLIE
          One. That is a rude thing to say.
          Two. It's called a party trick,
          clearly you've never been to one.
          Have you not seen Real Steel, it
          has a 73% audience score on rotten
          tomatoes. Me and my robot Atom
          become the 'peoples champion' at
          the end of the movie.

                    BARTENDER
          You got beat by Zeus at the end of
          the movie.

                    CHARLIE
          Dude! spoilers. Bartender lady,
          When people see me they say,
          "yooooo, thats Hugh Jackman and the
          robot from that sick PG-13 movie
          from 2011"

                    BARTENDER
          Yea no one says that. You're known
          around here for being the cuck for
          your robot.

                    CHARLIE
          I thought I kept that a secret!

A lady enters the bar.

                    GISABELLE
          Oh my goodness it's the robot and
          its cuck, I've heard this robot
          gives us chicks the most normal
          missionary vanilla sex ever.

                    CHARLIE
          Can anyone give a cuck his credit!
          Im the one doing all the work!
          Geez!

As he says this line he flails his arms around and the robot
does the same.

                    CHARLIE (CONT'D)
          Wow! (sarcastically) I'm so sorry
          for realizing I could do more than
          just fighting with my robot. Also,
          our dicks are the same size!

The bartender peaks over the bar to look at the robot.

                    BARTENDER
          How his dick staying perched up on
          his balls like that?

                    CHARLIE
          Like the lil dicky song.

Gisabelle takes a gander.

                    GISABELLE
          Yea it looks like like a scared
          turtle.

                    CHARLIE
          Maybe because its nervous that two
          girls are talking to it right now!
          Maybe it's because our penises are
          pre destined to every male, and we
          have zero choice on how it looks.

                    BARTENDER
          You literally made this robot.

                    CHARLIE
          No. I found it abandoned in a
          garage. Then I added the penis.

A guy enters the bar.

                    DAVE
          Yo! It's Atom the fighting robot!
          That's si- why the fuck does atom
          the 'peoples champion' robot have a
          micro penis attached to his groin.

                    CHARLIE
          Okay, you know what. I'm leaving.
          This bar is full of people that do
          not respect me because of something
          I cannot control. Call me a banana
          cause imma split.

                    BARTENDER
          That was a sick outro bar, but You
          haven't paid for any of your
          drinks.

                    CHARLIE
          My presence is worth so much money
          that you can't even comprehend.

FIN`,
    },
    {
      id: "tush-push",
      title: "Tush Push",
      body: `INT. NBC NFL BROADCAST BOOTH

Two NFL commentators are talking about the game below. The
Eagles are playing the cowboys in this important NFC east
rivalry game. There is four minutes left in the fourth
quarter. The score is tied 21-21 and the eagles have the ball
on their own 45 yard line. It's 3rd and three and it looks
like they are going to do their famous tush push play in
order to get the first down.

                    MIKE
          Hello everyone tuning in from the
          Jaguars and Bills game. You came in
          just in time to see the ending of
          this thrilling match up between two
          bitter rivals The Philadelphia
          eagles and the Dallas Cowboys.

                    CHRIS
          It's tied up right now 21 a piece,
          and with four minutes left on the
          clock, the eagles could really use
          a score here.

                    MIKE
          That is true, but a big play can
          come a little later. The eagles
          have the ball on their own forty
          five. And its third and three, so
          we may be looking at their iconic
          tush push.

                    CHRIS
          God, the feeling of having two two
          hundred and fifty pound tight ends
          thrusting you up the right hole
          must be the best feeling in the
          world.

                    MIKE
          I'm gonna act like you didn't say
          that. Now, lets see this play in
          action.

The camera cuts to Jalen getting ready to say hut.

                    JALEN
          Hoooweeee. I cannot wait to get my
          ass rammed across that first down
          line. I HAVE THE BEST JOB IN THE
          WORLD!

Jalen signals and gets ready to say hut.

                    JALEN (CONT'D)
          White eighty. Blue forty two. Oh
          god I can't wait. Ready HUT!

The tush push commences and Jalen hits a little moan when he
gets pushed in his tush.

                    JALEN (CONT'D)
          Oh yea. Right there.

Jalen only gets two yards, so it's fourth and one. Camera
cuts back to Mike and Chris.

                    CHRIS
          Am I the only one to hear that moan
          coming from Jalen?

                    MIKE
          Yea, im not complaining, he cute as
          hell. Well they fell short of the
          first, but I think they are going
          to do the tush push once again on
          this fourth and inches play.

Camera cuts back to Jalen calling the play in the huddle.

                    JALEN
          This is why we fucking play! We are
          running the tush push again. This
          time I want four people getting
          behind me, and I want you guys to
          absolutely penetrate me across the
          first down line.

                    SAQUON
          Please! Please! Pick me I wanna get
          behind you so bad, and I never get
          picked.

                    JALEN
          Your time will come Saquon, but
          right now I need some absolute
          stallions to punish me. Maillata
          and The fridge William Perry are
          gonna be the other two to push me.

                    SAQUON
          Ugghhhh. No fair! The fridge
          retired like thirty years ago.

                    THE FRIDGE
          You would unretire too if you were
          able to get behind that frosted
          bear claw of an ass.

                    JALEN
          Okay lets do this!

The team lines up to do the tush push.

                    JALEN (CONT'D)
          Ready. Blue forty two. Ready hut!

As the bodies meet Jalen rips a massive moan, and scurries
his butt across the first down marker.

Camera cuts to the booth. The announcers are drooling.

                    MIKE
          Run that shit again!

Camera pans to Chris Collinsworth breaking down the play with
a yellow marker on the board.

The board is Jalen hurts with a huge ass (think bathroom ass
on counter selfie), and Jalen is looking back at it with a
finger shushing his soft lips.

                    CHRIS
          Well here's a guy.

He circles Jalen's butt. And runs an arrow to his lips.

                    CHRIS (CONT'D)
          I'm not gonna lie I can't
          concentrate. He's just too damn
          cute.

                    MIKE
          Well it's first and ten so they
          sadly aren't gonna run the tush
          push aga- holy shit they are doing
          the tush push but everyone is
          behind Jalen Hurts!

                    CHRIS
          Lets go to our sideline reporter
          Melissa Stark for a closer look at
          the action.

Camera cuts to the sideline. Both teams are behind Jalen
ready to run train on his ass.

                    MELISSA
          Guys I was on the sideline
          reporting for this game, but I
          could not handle myself, so I am
          currently behind Jalen Hurts also.

                    JALEN
          Blue forty two.

                    MIKE
          Oh stop playing games with us
          Jalen! Just say hut!

                    JALEN
          Ready.... Hut!

And it ends with it being a big jumble of grown men having
the time of there lives getting behind Jalen.

FIN`,
    },
    {
      id: "bad-ultra-sound",
      title: "Bad Ultra Sound",
      body: `INT. ULTRASOUND CLINIC - MORNING

A woman nurse and a woman Shelly are sitting together in the
ultrasound room. The nurse is big spooning shelly who is
pregnant with both of her hands going counter-clockwise over
her breasts. The nurse hums sweet nothings into Shelly's ear.

                    FEMALE NURSE
          Okay your heart rate is at 120 bpm.

                    SHELLY
          It's so crazy that this clinic
          tests the hear rate without a
          stethoscope.

                    FEMALE NURSE
          Oh. I was just guessing your heart
          rate because you weren't talking,
          and I was just breaking the
          silence.

                    SHELLY
          What?

                    FEMALE NURSE
          Yeah, I just wanted to hug you from
          behind, rub your nipples counter-
          clockwise, and whisper sweet
          nothings in to your ear.

The nurse gets up.

                    FEMALE NURSE (CONT'D)
          Doctor Patrice will be in here
          shortly.

The nurse leaves the room. Shelly who is now kind of shell
shocked checks her phone for a second as Doctor Patrice nocks
sporadically on the door.

                    DR. PATRICE
          (From outside the door) I COMING IN
          WHETHER YOU LIKE IT OR NOT!

Patrice opens the door and walks into the ultrasound room.

                    DR. PATRICE (CONT'D)
          Holy shit, you are fat.

                    SHELLY
          I'm pregnant.

                    DR. PATRICE
          Thank god, but I would still advise
          you lose a pound or two.

The doctor claps once.

                    DR. PATRICE (CONT'D)
          Okay! Lets put some jelly on your
          belly! How many weeks?

                    SHELLY
          27 weeks.

                    DR. PATRICE
          Nice. Have you done an ultrasound
          here before?

                    SHELLY
          This is my first time here, but
          this is my second ultrasound, I did
          one at six weeks, but I could not
          really see anything.

                    DR. PATRICE
          Yeah. At six weeks the baby is the
          size of a 99 bananas shooter.

The doctor pulls out three empty shooters from his pocket.

                    DR. PATRICE (CONT'D)
          At twenty-seven weeks you can
          definitely tell what the baby is
          going to look like. Right now, I
          bet it's the size of a fifth of
          Jack.

The doctor pulls out a half drank bottle of jack from his
pocket.

                    SHELLY
          Have you been drinking?

                    DR. PATRICE
          No. These are props to show you how
          big your baby is. That is totally
          disrespectful to me and my
          practice. One more ounce of
          disrespect, and I will enact the
          fear of god in you.

The doctor claps one more time, but when he claps a crack of
thunder occurs outside.

                    DR. PATRICE (CONT'D)
          Alrighty! Just lift up that there
          shirt, and let's get started.

Shelly pulls up her shirt and the doctor applies the jelly.

                    DR. PATRICE (CONT'D)
          The ultrasound jelly always reminds
          me of lube.

                    SHELLY
          Why would you say that?

                    DR. PATRICE
          I don't know. I usually say the
          lube line to cut the tension. Who
          knows your baby could be dead.

                    SHELLY
          Let's not hope that happens.

                    DR. PATRICE
          Sure.

The ultrasound starts, and the images of her belly and baby
are put on to the screen.

                    DR. PATRICE (CONT'D)
          Oh My God!

                    SHELLY
          What?

The doctor looks at the screen. Looks at shelly, then back at
the screen, and back at shelly.

                    DR. PATRICE
          Your baby is straight up ugly.

                    SHELLY
          What does that mean?

                    DR. PATRICE
          I don't think your baby is going to
          make it.

                    SHELLY
          No please don't say that.

                    DR. PATRICE
          Stop acting like your baby is going
          to die.

                    SHELLY
          You just told me my child was not
          going to make it.

                    DR. PATRICE
          Yea. Make it through middle school
          with that big ass forehead. Your
          child is going to be brutally made
          fun of because of its physical
          appearances.

                    SHELLY
          How can you tell?

                    DR. PATRICE
          Take a look right here. That's the
          (gulps) face. Wait no that's the
          butt, wow there is no difference
          between the face and the butt.

                    SHELLY
          Jesus christ. Its face really does
          look like a butt.

                    DR. PATRICE
          I mean, I can already tell. Your
          baby is going to grow a the worst
          mustache of all time in seventh
          grade.

                    SHELLY
          Wait. So, your telling me its a
          boy?

The doctor looks at her with a little disappointment.

                    SHELLY (CONT'D)
          It's a girl. Great. This is how I
          find out.

                    DR. PATRICE
          Hey look. I didn't tell you but,
          yeah. I mean look at the posture
          right there.

The doctor points to the screen.

                    DR. PATRICE (CONT'D)
          I can already tell that your baby
          is going to rip cart, and play
          Clash Royale at full volume during
          algebra. Like, she sucks.

                    SHELLY
          This doesn't sound like my baby.
          I'm leaving and I'm finding a new
          doctor.

Shelly starts to get up.

                    DR. PATRICE
          Wait! Don't leave, your baby has
          cancer!

                    SHELLY
          What!

Shelly sits back down.

                    DR. PATRICE
          No, I just said that so you
          wouldn't leave. The huge tumor on
          its chest is its softball sized
          nipple.

                    SHELLY
          It only has one nipple?

                    DR. PATRICE
          Yes. The one nipple is the size of
          four. Who impregnated you? Because
          from the ultrasound it looks like a
          warthog did.

There is a nock at the door.

                    SHELLY
          My husband impregnated me. He's at
          the door right now.

Jason Momoa walks in. Everyone starts clapping.

                    DR. PATRICE
          That's my male nurse.

                    SHELLY
          Okay fine. Tyga is the baby daddy.

                    DR. PATRICE
          Well, that makes sense. When should
          we schedule your next appointment?

                    SHELLY
          I am never coming back here.

                    DR. PATRICE
          All good.

Shelly leaves.

                    DR. PATRICE (CONT'D)
          Male Nurse Jason Momoa, can you
          check my heart rate?

                    JASON
          Of course.

Jason Momoa big spoons Dr. Patrice with both of his hands
caressing his breasts. The nurse hums sweet nothings into his
ear.

                    JASON (CONT'D)
          Your at 38 bpm right now, how are
          you so calm?

                    DR. PATRICE
          Because your here Jason. Because
          your here.

THE END`,
    },
    {
      id: "house-of-devon",
      title: "House of Devon",
      body: `INT. DINGY APARTMENT WITH A MASSIVE TABLE IN THE MIDDLE OF IT
WITH FOLDABLE CHAIRS ALONG THE SIDES AND A MASSIVE THRONE AT
THE HEAD OF THE TABLE.

The scene starts with a voice over for an
advertisement/trailer for Game of Thrones "The House of
Devon"

                    VOICE OVER GUY
          From the makers of Game of Thrones'
          House of the Dragon and Beat Bobby
          Flay we give you "The House of
          Devon" A story of the inner makings
          of a four person apartment in
          Chelsea with a guy named Devon as
          the friend group leader.

The people of the apartment are sitting around in small
foldable chairs at this massive table that is way to big for
the place, as everyone takes there place at the table they
put down their geek bar in their designated geek bar place
like the balls they have in the house of the dragon. Devon
sits at the head of the table in a massive reclinable lazy
boy. Devon has is hand of the king right next to him with a
bottle of lotion and kleenex to his side. There are cup
bearers walking around the table refilling everyones mugs
with grape four loko.

                    DEVON
          Sup. Everyone.

                    VOICE OVER GUY
          In this house there is only one
          king.

                    ADRIAN
          What is the plan for today King
          Devon?

                    DEVON
          Lowkey hung, but I was thinking we
          walk around outside and throw
          homeless people white bread like we
          are feeding pigeons at the park.
          Then after we can start a lemonade
          stand to get some bread, as in
          money so we can pay for more white
          bread, then, the cycle continues.

Everyone applauds King Devon for his stupendous idea.

                    MASTER OF COIN
          A lemonade stand is a brilliant
          idea!

                    DEVON
          Why, thank you master of coin.

                    VOICE OVER GUY
          Variety calls it "It's for viewers
          who liked New Girl but wished there
          was more incest."

                    DEVON
          Hand of the Devon come hither.

                    HAND
          Yes m'lord.

                    DEVON
          I believe we need have a private
          meeting in my shared bathroom.

                    HAND
          Of course m'lord right this way.

The two leave, 30 minutes later they comeback and Devon is
sweating.

                    TERRY
          Did your hand jerk you off again.

                    DEVON
          That is his job Trius, how else am
          I gonna think of sick ideas to do.

                    TERRY
          Also, Why are you sweating if he's
          the one jerking you off?

                    DEVON
          Silence from you! One more word and
          you will be banished from this here
          apartment for treason!

                    VOICE OVER GUY
          Barnes and Noble calls this
          television series "Sexual, in all
          of the worst ways"

                    DEVON
          Cup bearer I need some more grape
          four loko.

                    VOICE OVER GUY
          In The House of Devon, there is
          Love.

                    ADRIAN
          King Devon, you will need a Queen
          in the future to further your blood
          line. Shall we check your matches
          on hinge.

                    DEVON
          Why yes!

They check the matches on phone connected to screen.

                    ADRIAN
          Here, we have Shelly from House
          Daniels. Queen of Cincy and Smoker
          of Ketamine.

                    DEVON
          Cincy, as in Cincinnati. Throw up
          in my fucking mouth. Who else did I
          match with.

                    ADRIAN
          Stephanie Thunderclap of House
          Hailey. Princess of Darien. Breaker
          of chains, and mother of dog named
          Remy name most likely from film
          ratatouille.

                    DEVON
          Seems based send her "sup" then
          throw her an unsolicited dick pick.
          But make sure to take the photo
          with a point five lens so the shaft
          seems longer.

                    VOICE OVER GUY
          But hang weary. There is also
          strife in The House of Devon.

                    TERRY
          King Devon, we have three hours
          until we go to the bar Spring
          Lounge to drink draft Budweiser.
          What YouTube videos should we watch
          here while we drink canned
          Budweiser.

                    DEVON
          The decision is made! We will watch
          "These College Football Entrances
          Will Give You CHILLS" by
          bigfouredits

                    TERRY
          But we watched that yesterday!

                    DEVON
          Then we will watch "These College
          Football Entrances Will Give You
          CHILLS (part 2) by bigfouredits!

                    TERRY
          We watched that yesterday right
          after the first one.

                    DEVON
          Auuughhhh I can't think. HAND I
          need another private meeting to
          talk about what YouTube videos we
          should watch in the shared
          bathroom.

The room groans.

                    VOICE OVER GUY
          But most of all. The House of Devon
          has unadulterated heart.

Devon comes back sweating to sit at the table.

                    DEVON
          You know guys, from what I learned
          from my private meeting with the
          hand is that it's not about the
          type of YouTube video you watch
          before you go out. It's the people
          you watch the YouTube video with
          before you go out.

The camera pans around the room of everyone smiling and
nodding.

                    DEVON (CONT'D)
          YouTube player person. Play the Mr.
          Beast video titled "first to grab
          they ankles and shake it til the
          pennies fallout wins a birkin and a
          spirit flight to belize."

                    YOUTUBE PLAYER
          Will do!

Graphic of House of Devon blazes across of the screen.

                    VOICE OVER GUY
          Game of Throne's "House of the
          Devon" coming to television near
          you. Only streaming on Daily Wire!
          "The only streaming service that
          hasn't not condemned slavery yet"
          yes, that is our slogan.

FIN`,
    },
    {
      id: "milfs-ad",
      title: "MILFS AD",
      body: `INT. BEDROOM NIGHT

A guy is in his bedroom at around three in the morning is
getting all of his things together so he can jerk off. He
whistling and singing like sleeping beauty when she is
singing in the woods to all of the animals. Whenever he sings
a tune his lotion and other supplies respond with a whistle
of the same tune. They all gather together at his desk to
commence his jerk.

                    KENNETH
          (singing in the tune of
          the beginning of The
          Jakcson 5's ABC)
          It's time to jerk ooooffff.
          Baa-ba-ba-ba-ba-baaa!

The lotion whistles in the same Jackson 5 ABC tune and floats
over to the desk.

                    KENNETH (CONT'D)
          (singing)
          Baa-ba-ba-ba-ba-baaa!

His computer whistles in the same tune and flaps its wings to
his desk.

                    KENNETH (CONT'D)
          (singing)
          Baa-ba-ba-ba-ba-baaa!

His kleenex whistles in the same tune and flies over to his
desk.

Kenneth sits down at his desk whistles and sings some more to
his jerk off supplies.

                    KENNETH (CONT'D)
          (singing)
          Baa-ba-ba-ba-ba-baaa!

The supplies respond with a loving chorus of whistles that
harmonize with each other. This is such a cohesive unit.

Kenneth cracks his knuckles opens up an incognito tab,
searches for the right website and the right video, and
clicks play.

                    KENNETH (CONT'D)
          Here. We. Go.

An advertisement starts to play.

                    ADVERTISEMENT
          Tired of jerking off alone?
          Chatterbate can help you out.

                    KENNETH
          God. I hate these ads. You know
          what, I actually enjoy jerking off
          alone. Me, my lotion, my kleenex,
          and my computer work together
          harmoniously. Another person would
          straight up fuck everything up.

Kenneth clicks out of the ad and then another one pops up for
MILFS in his area.

                    ADVERTISEMENT
          There are currently over a hundred
          MILFS in your area ready to rock
          your world.

                    KENNETH
          Enough with these ads geez!

                    ADVERTISEMENT
          Stacy, 36, is just one click away.

                    KENNETH
          How about I click away from this
          freakin ad.

When he goes to click out of the ad he takes a look at
Stacy's eyes, it seems as if they are staring directly in to
his soul. She looks like she needs someone to save her.

                    KENNETH (CONT'D)
          You know what. I never click on any
          of these ads, but there is just
          something in those icy blue eyes
          from Stacy, 36. It looks like she
          needs someone to save her.

Kenneth clicks on the ad, and his whole screen starts glowing
blue.

                    KENNETH (CONT'D)
          Fuck, I'm so stupid. I knew it was
          a scam, why would anyone click on
          these ads.

His computer continues to glow brighter and brighter.

                    KENNETH (CONT'D)
          Uh oh.

The computer starts floating in the air, and Kenneth sees his
hands fusing with the screen.

                    KENNETH (CONT'D)
          Holy shit! Im getting sucked in to
          this porn ad.

His whole body is beginning to get sucked in.

                    KENNETH (CONT'D)
          I'm getting jumanjied right now!

Kenneth fully goes into to his computer, and the computer
falls back on his desk.

CUT TO:

INT. DUPLEX LIVING ROOM NIGHT

Kenneth wakes up slowly in a place that is not his bed room.
He's in a duplex of some sort.

                    KENNETH
          Where am I? Ugh what is that smell?
          Is that a crock pot dinner? GET ME
          THE FUCK OUTTA HERE.

Kenneth looks around and see something glowing in the corner,
he walks towards it.

                    KENNETH (CONT'D)
          Whoa. What is that.

He picks up a blanket that was draped over it, and it
uncovered an old timey book absolutely caked in dust.

                    KENNETH (CONT'D)
          A glowing book! With dust on it!
          I've always wanted to do this.

He goes to blow on it but there is too much dust and nothing
happens.

                    KENNETH (CONT'D)
          Oh.

He opens the book and it uncovers an ancient story like the
one shown in the beginning of Shrek.

                    KENNETH (CONT'D)
          A story! I love stories.

Kenneth begins to read the story.

                    KENNETH (CONT'D)
          Once upon a time a thirty six years
          ago in this very duplex a Plumber
          and a Music Teacher had a beautiful
          daughter named Stacy.

Kenneth realizes the situation he is in.

                    KENNETH (CONT'D)
          Wait. Stacy! Thirty Six! This story
          is about the lady in the MILFS near
          us ad. I think i'm in her duplex.

Kenneth begins to read some more.

                    KENNETH (CONT'D)
          But Stacy was possessed by a
          terrible curse. By day, a lovely
          local barista at dutch bros. By
          night, a hideous thirty six year
          old in a MILFs near you
          advertisement.

A thunder cracks outside. Kenneth continues to read.

                    KENNETH (CONT'D)
          Only a true love's kiss could lift
          her curse. And so, Stacy, 36,
          waited on the second floor of her
          duplex guarded by her weird
          seventeen year old son. Until the
          day when her true love would
          arrive.

Kenneth slams the book shut. Gets up on the coffee table and
puts his fist in the air.

                    KENNETH (CONT'D)
          I CAN BE HER TRUE LOVE!

A voice from up the stairs breaks his triumphant bout.

                    TOBY
          Dude. Who the fuck is yelling down
          stairs. Derrick is that you?

                    KENNETH
          (To himself)
          That must be her deadbeat son.

                    KENNETH (CONT'D)
          Yes! It is I! Derrick.

                    TOBY
          Not gonna lie. I'm way to high for
          this. Stop talking like your a
          knight.

                    KENNETH
          Yea sorry.

Toby starts walking down the stairs and Kenneth tries to
evade.

                    TOBY
          Im lowkey going in third person
          mode right now. I feel like-

Toby begins to snap his fingers almost as if if trying to
remember a name.

                    TOBY (CONT'D)
          Who is that turtle looking guy that
          talks about the Olympics?

                    KENNETH
          Mike Tirico?

                    TOBY
          That's exactly who i'm thinking
          about. I feel like Mike Tirico is
          announcing everything i'm doing in
          my head. I'm like buffering right
          now. He's telling me I shouldn't be
          running a slow mesh right now
          because my opponent is running a
          cover three zone. Wait. Im actually
          freaking out. Derrick can you help
          me breathe. Holy fuck I think i'm
          dying, can you like breathe in my
          mouth. I'm literally manually
          breathing right now. Oh god! If I
          fall asleep i'm going to die aren't
          I. Derrick please come here and
          breathe in my mouth!

Kenneth walks over to Toby.

                    KENNETH
          I will help you but if you die your
          blood will be on my heads.

                    TOBY
          What the fuck is that supposed to
          mean? Holy shit your not Derrick.
          Oh god. My life is crumbling like
          cookie. I honestly just need to be
          little spooned right now can you
          help me not Derrick.

                    KENNETH
          I can do that.

The two cuddle. Kenneth is the big spoon and Toby is the
little spoon. Kenneth is playing with Toby's chest hair while
reading him 'The Very Hungry Caterpillar.' Kenneth warms up
some milk and feeds it to Toby sip by sip as they watch an
episode of Entourage. As the episode hits the credits Kenneth
then leads Toby back up to his room, and tucks him under the
covers slowly and sensually. Kenneth gives Toby a back rub
until he hears a subtle snore from Toby.

                    KENNETH (CONT'D)
          My work here is done. Off to save
          Stacy, 36.

Kenneth walks across the hall, opens the door slowly, and
there she is.

                    KENNETH (CONT'D)
          It's Stacy, 36!

He walks quietly to her bed and gives her a kiss on her lips.
She wakes up in a panic.

                    STACY
          WHO THE FUCK ARE YOU?

                    KENNETH
          It's me Kenneth. I Have come to
          save yo-

She pulls out a gun under her pillow and shoots him in the
face.

                    STACY
          NO ONE MESSES WITH STACY. You god
          damned pervert!

CUT TO:

INT. BEDROOM MORNING

Kenneth wakes up screaming then stops and looks around.

                    KENNETH
          Ight, that was a dream. Probably
          should have known that when I was
          singing Jackson 5's ABC to my
          animatronic lotion and kleenex.

Kenneth looks around. Checks his phone. Puts his phone down.

                    KENNETH (CONT'D)
          I'm gonna jerk my shit right quick.

"The End" Swirls across the screen like at the end of
fairytale movies.

THE END`,
    },
    {
      id: "hostage-flextape",
      title: "Hostage FlexTape",
      body: `INT. PHIL SWIFT'S HOUSE - AFTERNOON

A filming of the world famous flex seal commercial commences
at Phil Swifts House. He has a huge fish tank like the one
you would see at a Bass Pro Shop and it's leaking everywhere.

                    PHIL
          Hi! Phil Swift here for flex tape
          the super strong water proof tape!
          Looky here at my fish tank full of
          endangered reptiles. There's a
          giant hole in the glass because I
          got drunk again!

Phil slams the tape on the leak on his fish tank. The leak
ceases to exist.

                    PHIL (CONT'D)
          Booyah. The leak stopped, and my
          albino crocodiles and amazonian
          piranhas can now live free. Bring
          me the goat.

A goat walks across the living room. The goat is yelling and
making noise.

                    PHIL (CONT'D)
          Ever need to feed your fish a goat,
          but the goat keeps making annoying
          ass noises?

Phil grabs some tape and slaps it on the goat's mouth, and
throws the goat like a strong man keg toss into the tank, and
the goat gets eviscerated by the piranhas.

                    PHIL (CONT'D)
          Flex tape! The instant patch, bond,
          seal, and repair. Flex tape is no
          regular adhesive. It virtually
          welds itself to the surface,
          literally stopping any type of leak
          or scream.

CUT TO:

INT. INDOOR GYM - AFTERNOON

Phil Swift deadlifts 315 with flex tape attached from his
nipples to the barbell and he reps the weight with ease.

                    PHIL
          Flex tape is super strong and when
          it's on-

Phil lifts the weight again.

                    PHIL (CONT'D)
          (grunting)
          It hold on tight!

CUT TO:

INT. PHIL SWIFT'S HOUSE

Phil Swift is standing there with a production assistant
named Richard.

                    PHIL
          To show you the power of flex tape
          I going to saw this production
          assistant in half, and repair him
          with only flex tape.

                    RICHARD
          Wait what?

                    PHIL
          Yup! Looks like someone forgot that
          I didn't like mustard on my
          sandwich! Here we go.

Phil saws Richard in half.

                    RICHARD
          AHHHH-

Phil slaps tape on his mouth.

                    PHIL
          Just cut, peel, stick, and tape.

Phil tapes body together, but the PA is clearly dead.

                    PHIL (CONT'D)
          Imagine everything you can do with
          the power of flex tape.

CUT TO:

An infomercial ad flashes across the screen. It shows Phil
doing various activities with flextape, sealing leaky holes
etc in the top left corner. The ad says 30 day money back
guarantee. Only $19.99 plus P&H, 2nd roll of tape free. There
is www.getflextape.com flashing at the bottom, with the 1-800-
709-6131 phone number. While this info graphic shows a voice
over to explain the info graphic plays quickly.

                    VOICE OVER
          (Quickly)
          Don't call a repair man to fix your
          holes and leaks that'll cost you
          thousands of dollars. You can get
          flex tape right now for just
          $19.99. But wait to make this the
          most amazing offer on television,
          were going to double your order and
          send you two large rolls of flex
          tape, just pay additional fees for
          process and handling. That's twice
          the sealing power for only 19.99!
          Here's how to order. To order flex
          tape call 1-800-709-6131 that's 1-
          800-709-6131 or order online at
          www.getflexseal.com call or click
          now.

CUT TO:

INT. PHIL SWIFT'S HOUSE

                    DIRECTOR
          That's a wrap! Everyone get home
          safe. Let's make sure to send out
          an ad out for an open production
          assistant role for tomorrow. We're
          lucky that we got it on the first
          take today.

                    PHIL
          Alrighty! I'll see you guys when I
          see you.

The camera crew and the director leave the premises only
leaving Phil and his tape alone in his house. You can hear
faint scream coming from Phil's basement.

                    PHIL (CONT'D)
          Yippee! I'm all alone now. So much
          time for activities.

Phil walks down to his basement where there are ten
production assistants all wearing the production assistant
garb. They are all taped together with tape on their mouths.
There is a lot of muffled screaming. There is also a camera
recording them in the corner, Phil walks by the camera,
stares directly into it, and starts another infomercial for
himself.

                    PHIL (CONT'D)
          Hey! Phil Swift here for hostage
          tape, the tape that you wan't if
          you have a shit ton of eighteen to
          twenty-two year olds that want to
          make it in the entertainment
          industry locked up in your
          basement.

Phil rips off the tape of one of the PA's

                    TIMMY
          Pick me! Please pick me. I want to
          be a production assistant for the
          next commercial. I'll do anything!

                    PHIL
          Can you work underwater?

                    TIMMY
          Yes! Well, what does that mea-

Phil tapes his mouth shut.

                    PHIL
          (Yelling) FLEX TAPE IS SO STRONG IT
          EVEN WORKS UNDER WATER!

Phil gets up and turns on a massive faucet. Water gushes in
filling up the cramped basement quickly.

                    PHIL (CONT'D)
          WHICH PA IS SO STRONG THAT THEY CAN
          WORK UNDERWATER!

The PAs are squirming, not knowing what to do under duress in
this circumstance.

                    PHIL (CONT'D)
          I guess no one yet.

Phil heads up stairs. While the water is still gushing. He
dials his phone for call.

                    PHIL (CONT'D)
          Director! I'm going to need like
          thirty PAs for the shoot tomorrow.

                    DIRECTOR
          (Through the phone) No problemo
          Phil!

                    PHIL
          Amazing! Phil Swift out!

FIN`,
    },
    {
      id: "therapist-breaks-fourth-wall",
      title: "Therapist Breaks Fourth Wall",
      body: `INT. THERAPISTS OFFICE - AFTERNOON

Terry lays on a sofa and he spouts his dumb feelings towards
the cool therapist.

                    TERRY
          I can't believe i'm at a therapists
          office. I feel like i've been
          holding in all of my emotions since
          the day I was born, and now I am
          finally allowed to get them out.

                    THERAPIST
          Enough with the sob story, spit it
          out.

                    TERRY
          Why would you say that?

                    THERAPIST
          I'm joking. Geez, Check the diploma
          next to the taxidermied gazelle
          that I stabbed with a boxcutter,
          i'm licensed to do whatever I want.

                    TERRY
          That's not even a diploma, it's a
          GED certificate from Miami Dade
          county jail. Why the hell did my
          mom recommend you as my therapist?

The therapist is pouring himself glass of just Aperol.

                    TERRY (CONT'D)
          Are you pouring a glass of Aperol?

                    THERAPIST
          No. It's V8. Look kid, Your mom is
          a wonderful woman. Let's start
          over.

                    TERRY
          Okay.

                    THERAPIST
          So, did you feel gay before or
          after your uncle took you to twin
          peaks?

                    TERRY
          What the fuck are you talking
          about.

                    THERAPIST
          Oops. Wrong patient, don't tell
          anyone I said that to you. It
          messes with HIPAA compliance or
          some shit.

                    TERRY
          Not gonna lie you're pretty
          terrible at your job.

                    THERAPIST
          Uh, buddy your the one needing help
          because your unable to keep your
          feelings inside like a man. Now
          tell me your story. Why are you the
          way that you are?

                    TERRY
          Oh okay, so were beginning now?

                    THERAPIST
          No shit, I mean we got like fifteen
          minutes left, because you can't
          help but to ask the worst
          questions. You may begin.

                    TERRY
          Okay. Well, Growing up was
          difficult.

The Therapist breaks the fourth wall, stares into the camera,
and whispers.

                    THERAPIST
          Pussy.

                    TERRY
          What was that?

                    THERAPIST
          Nothing. Continue.

                    TERRY
          As I was saying growing up was
          difficult.

The Therapist breaks the fourth wall, stares into the camera.

                    THERAPIST
          We heard you the first time.
          Amiright?

Therapist gives a palms up expression when he says 'amiright'
Terry gets up from the couch.

                    TERRY
          Who are you talking to?

                    THERAPIST
          To myself. Continue. PLEASE.

Terry lays back down.

                    TERRY
          I just feel lonely because I come
          from a single parent household and
          I never had siblings.

The Therapist breaks the fourth wall, stares into the camera.

                    THERAPIST
          This guy needs to get laid.

Terry looks at the Therapist staring off into the distance.

                    THERAPIST (CONT'D)
          Call the doctor. Get this man a
          prescription of bootie. Make sure
          to take it twice a day and always
          have a meal before. Hahaha. I love
          joking with myself.

                    TERRY
          WHO THE HELL ARE YOU TALKING TO?

                    THERAPIST
          Ight the jig is up. Camera crew
          come in. He found out.

Two guys holding cameras walk in. One is taking a video, and
the other is taking a video of the camera man in front of him
for a behind the scenes documentary they are filming on top
of The Office style documentary of this guys Therapists
office.

                    TERRY
          Have you been taking videos of me
          this entire time?

                    THERAPIST
          Short story, yes. Long story, I
          just watched Parks and Rec and
          thought that documentary was
          hilarious, and Amy Pholer has an
          ass that goes for miles. Anyways I
          decided to make my own documentary
          for my workplace the Therapist's
          office. I'm calling it

Therapists gets up and turns a whiteboard around which spells
out "The(rapists) Office."

                    THERAPIST (CONT'D)
          "The(rapists) Office". It's like
          The Office but its "The(rapists)
          Office". I've been taking videos of
          all of my clients, and I react and
          break the fourth wall like Jim
          Halpert when they tell me weird
          stories about their fucked up
          lives.

                    TERRY
          You've gotta be kidding me. Your
          mocumentary style show is called,
          The, parenthesis, rapists Office.

                    THERAPIST
          It's a play on words i'm a
          therapists. Check the credentials.

The Therapists shows his knuckles and they are tatooed
spelling out "The" on one fist and "Rapist" on the other
fist.

                    TERRY
          What words do those play on?

                    THERAPIST
          My words. Any who your episode is
          like the third to last of the
          season, and you can watch your
          episode in like four to six months.
          It's going to be streaming on the
          Daily Wire.

                    TERRY
          This breaks so many violations. You
          told me not to tell anyone about
          the Twin Peaks story because it's
          compliant to HIPPA.

                    THERAPIST
          Shhhh, be quiet the cameras are
          recording. I can't have that story
          go out.

                    TERRY
          Why is one camera recording the
          camera guy.

                    THERAPIST
          We're doing a behind the scenes doc
          too. I've heard it brings more bang
          to the buck.

                    TERRY
          Well I don't want people knowing
          that I feel lonely. I wan't you to
          cut everything that you have taken
          a video of.

                    THERAPIST
          When you signed your papers in the
          waiting room you signed off to
          being filmed, and a NDA, so you
          technically can never speak of
          this.

The Therapist pours himself a glass of bitters. He shakes the
bitters bottle violently in the glass of ice.

                    TERRY
          Again with the weird drinks. Why
          are you pouring yourself a glass
          with only orange bitters.

                    THERAPIST
          Because they don't ID you when you
          only get bitters at the CVS. I
          learned that during my time at the
          slammer.

                    TERRY
          Dude you're like fifty. No one is
          ID'ing you.

                    THERAPIST
          Well, i'll let you know that i'm
          fifty five, so That diss serves as
          a compliment.

                    TERRY
          I'm leaving.

                    THERAPIST
          Don't hit the door on the way out
          jack ass. Camera man follow him out
          to the car Jerry Springer style.
          Camera man for cameraman do the
          same.

The Therapist sees everyone leave, and walks to the window
and puts his foot at the edge of the window seal to evoke a
powerful stance. He takes a look out the window while sips on
his glass of bitters.

                    THERAPIST (CONT'D)
          Just another day at the the-rapists
          office.

The Office outro song begins to play and the final frame the
The Office Logo, but it reads "The(rapists) Office" and
instead of the white stick figures holding a briefcase and a
guy sitting at the desk. It's a person laying down on a couch
and another stick figure staring over them.

FIN`,
    },
    {
      id: "just-cracked-my-boy",
      title: "Just Cracked My Boy",
      body: `INT. MIKEY'S BEDROOM - NIGHT

JOHN and MIKEY are jumping up and down on a Tempur-Pedic
mattress like in the commercials, and they have glasses of
wine balancing on the other side of the bed. Party in the USA
plays in the background, and a fan in whirling just above
their heads.

                    MIKEY
          I'm so glad you could come over
          tonight and test out the Tempur-
          Pedic mattress with me.

                    JOHN
          Of course man! I've always wanted
          to know if the red wine would spill
          or not if you jump on the mattress
          on the other side of the bed.

                    MIKEY
          Yeah! And it's not! I don't really
          know what this means, but the
          marketing worked.

                    JOHN
          How much money did you spend on
          this mattress Mikey?

                    MIKEY
          Like seven grand, but it does pass
          the wine test so I guess it's a win-
          win.

                    JOHN
          More like Wine-Wine! Jumping up and
          down on this mattress, drinking red
          wine, and listening to Party in the
          USA is really a fun time.

                    MIKEY
          John! Our favorite part is about to
          come on!

                    JOHN
          "That's when the taximan turned on
          the radio!"

                    MIKEY
          "And a Jay-Z song was on!"

                    JOHN
          "And a Jay-Z song was on!"

                    MIKEY
          "And a Jay-Z song was on!"

John goes to put his hands up and jumps up extra high for the
next part of the song.

                    JOHN
          "So I put my hands u-

John hits fan, he flies back towards the edge of the bed and
cracks his head open. Mikey does not see this happen, and he
is still singing.

                    MIKEY
          "The butterflies fly away,
          Nodding my head like, yeah. Moving
          my hips like, yeah!" C'mon Johnny
          sing it.

Mikey turns his head to see John bleeding out, his head is
cracked open.

                    MIKEY (CONT'D)
          Holy shit! You're bleeding!

Mikey turns off the music, and gets his phone to dial 911.

                    MIKEY (CONT'D)
          Stay with me Johnny!

The phone gets answered by the 911 emergency operator.

CUT TO:

INT. POLICE STATION - NIGHT

                    OPERATOR
          Hello?

                    MIKEY
          Hello! Is this 911?

                    OPERATOR
          No, it's terry, but I work for 911,
          i'm the emergency operator.

                    MIKEY
          What?

                    OPERATOR
          Do you want me to say my line?

                    MIKEY
          What line? I need help!

                    OPERATOR
          911, what's your emergency? God
          Damn it. I'm good at what I do.

                    MIKEY
          My friend, Johnny and I were
          jumping up and down on a tempur-
          pedic mattress, and I cracked his
          head open!

                    OPERATOR
          You what?

                    MIKEY
          I don't know! We were singing Party
          in the USA. My thrust turned me
          around, and his head was absolutely
          cracked open.

                    OPERATOR
          You cracked your boy's head? How is
          that even-

                    MIKEY
          Yes! Oh my god, there's blood
          everywhere!

                    OPERATOR
          Ew! Like from his mouth, i'm
          assuming you cracked his mouth.

                    MIKEY
          What? No, he's like blooding from
          his temple.

                    OPERATOR
          You fucked his ear! Dear god what
          happened to normal sex.

                    MIKEY
          I didn't have sex with Johnny. We
          were just drinking wine, listening
          to Miley Cyrus, and breaking in the
          tempur-pedic mattress.

                    OPERATOR
          I'm not trying to yuck anyones yum,
          but your yum sucks. Do you still
          need an ambulance?

                    MIKEY
          Yes! I can't drive right now.

                    OPERATOR
          Because of the red wine.

                    MIKEY
          Yes, oh my god. We were doing the
          the red wine test.

                    OPERATOR
          I'm not even gonna guess what the
          fuck that could mean. You could be
          in big trouble, I mean big! Where
          is you address?

                    MIKEY
          3459 Mulberry Lane, please get here
          as soon as you can!

The phone call ends.

CUT TO:

INT. MIKEY'S BEDROOM

Mikey caresses John.

                    MIKEY
          You're gonna make it John I
          promise.

                    JOHN
          What happened? I don't remember
          anything.

                    MIKEY
          You're going to be fine, help is on
          its way, but I lowkey cracked you
          head open.

                    JOHN
          You what? Oh my god Mikey why would
          you do that, get the fuck off of
          me.

                    MIKEY
          It's going to be okay. We got a
          little wine drunk, testing out the
          Tempur-Pedic mattress and I cracked
          your head open.

                    JOHN
          I did not consent to that, why am I
          bleeding from my ear. Did you fuck
          my ear?

The police battering ram the door down.

                    MIKEY
          Why would you do that? My door was
          unlocked!

                    POLICE
          You would do the same if you had
          the power that we have. Now turn
          around your under arrest.

                    MIKEY
          For what?

                    JOHN
          Yes! Please arrest this fucking
          weirdo!

                    MIKEY
          What is happening, I called you
          guys to help my friend.

Mikey goes to grab the wine glass on the bed.

                    POLICE
          He's reaching for a gun!

The police shoot Mikey. He falls on the bed, the wine still
does not spill. A Tempur-Pedic ad begins to play while the
ensuing scene happens.

                    TEMPUR-PEDIC VO
          Tempur-Pedic! The memory foam bed
          that never spills red wine under
          any circumstance. Even through
          death!

FIN`,
    },
    {
      id: "grills",
      title: "Grills",
      body: `INT. SUBURBAN HOUSE - AFTERNOON

RICHARD is very stressed out sitting on one end his large L-
shaped couch. DAVE is sitting on the other end.

                    DAVE
          Richard. What's up dude you seem
          really stressed.

Richard has his face pressed against his palms.

                    RICHARD
          Life man. Lately it's been getting
          to me.

                    DAVE
          C'mon man life can't be that bad
          right now. We got the little league
          world series on the tele. Your mom
          made us jager bombs, and we got
          chips and guac on the coffee table.

                    RICHARD
          I can't keep doing this.

                    DAVE
          I'm sure what you're going through
          is like a wave. It crashes once and
          stops immediately.

                    RICHARD
          Dave, look at me.

Richard smiles showing off his diamond studded grills that
are wrapped around his teeth.

                    DAVE
          Holy shit man you got grills on.
          Whoa they actually sparkle. Not
          gonna lie this is like the first
          time i've ever seen them in person.

                    RICHARD
          Thanks for that glaze, but these
          diamond studded grills have been
          the bane of my existence ever since
          I put them on a couple of days ago.

                    DAVE
          Why? They honestly look sick on
          you.

                    RICHARD
          Stop it with the compliments!

Richard stands up from his large L shaped couch and gets on
his hoverboard. He does a three sixty with the hoverboard.

                    RICHARD (CONT'D)
          I'm sorry but I had to get up from
          the couch and get on my hoverboard,
          i'm stressed as fuck. You do not
          know the struggle with owning
          grills. Every time I eat something,
          I have to take them off.

                    DAVE
          Okay? That does not seem too bad.

                    RICHARD
          You didn't let me finish! You NEVER
          let me finish. Then I have to put
          them back on when I finish eating.
          Like what the fuck. Adding so much
          stress to my already stressful
          life.

Richard gets a spoon from his pocket puts crystal meth in it,
lights the bottom of the spoon with a lighter, and smokes the
meth.

                    DAVE
          Yo what the fuck. You started
          smoking meth? Because you're
          stressed?

                    RICHARD
          No, dumb fuck. It's to cut down on
          my appetite. If I don't eat, I
          don't have to take my grills on and
          off all the time.

                    DAVE
          When was the last time you ate?

                    RICHARD
          The meal after I had to take the
          grills off then put them back on.
          Like, what do you want me to do? I
          can't let these grills add
          unnecessary steps to my day to day
          life.

His mom yells from up the stairs.

                    MOM
          Honey! Dinners ready! I made your
          favorite chicken pot pie with the
          flakey puff pastry. Also, grandma is
          here for her ninety-second birthday.
          Why don't you say hi to sweet old
          mee-ma.

                    RICHARD
          Sweet old mee-ma can shove that
          chicken pot pie straight up her
          refrigerator of an ass. I'm too
          busy wearing grills and smoking
          meth.

                    MOM
          My little comedian. Okay! Have fun.

                    DAVE
          Dude you speak to your mouth with
          that mouth.

                    RICHARD
          A mouth full to the brim of vvs's.
          Also, she knows what I am going
          through. Her father was an
          alcoholic with major PTSD from the
          Vietnam war.

                    DAVE
          What?

                    RICHARD
          I don't know I made that up. She's
          been drinking a lot lately. Don't
          tell her said that to you.

                    DAVE
          I think you should just ditch the
          grills. It seems to be completely
          taking over your life.

Richard rips another hit of meth.

                    RICHARD
          I wan't to take them off. I really
          do, but I lowkey might not even
          have actual teeth left. Turns out
          meth fucks up the enamel. Also,
          instead of brushing my teeth, i've
          just been going crazy with the
          flossing and mouthwash.

                    DAVE
          How do you floss with grills?

                    RICHARD
          You technically can't. I just wrap
          the floss around my fingers, put
          the floss close to my mouth, and
          onomatopoeia the bitch.

                    DAVE
          What?

                    RICHARD
          Look.

Richard rolls up to a mirror with the hoverboard, takes floss
from his back pocket, wraps the floss around both of his
finger tips, opens his mouth and does little motions with the
floss.

                    RICHARD (CONT'D)
          Ee-ee-ee-ee, Then I get the bottom
          set. Ee-ee-ee-ee. I spit.

He spits on the ground, the color of his spit is brown.

                    DAVE
          Ew.

Richard lines up four shot glasses, and pours blue listerine
in all of them.

                    RICHARD
          Then I take four shots of
          listerine.

Richard takes the shots

                    DAVE
          You can't do that!

                    RICHARD
          Boo-hoo the Indians drink listerine
          all the time because alcohol is
          banned on some of the reservations.

                    DAVE
          That is quite honestly the worst
          piece of reasoning I have ever
          heard.

                    RICHARD
          Pretty wild for someone to talk
          like that without grills in their
          mouth.

                    DAVE
          Man you gotta just rip the bandaid
          off. These grills are ruining your
          life. Look at yourself.

Richard hit's a one-eighty with the hoverboard, and shows off
his Alec Monopoly Anti-Social-Social-Club shirt.

                    RICHARD
          Read the shirt.

FIN`,
    },
  ],

  /* ---- the planets ------------------------------------------------------
     art types you can use: "sphere", "ringed", "banded", "swirl", "marbled", "shorts", "earth", "basketball"
     panel.layout options:  "right", "left", "diagonal"
     page.ribbon: optional — shows in the top bar next to the corner moon
     instead of the usual blurb paragraph below the panel (see "lineup").
     Delete a whole { ... } block to remove a planet. Copy one to add a planet.
  ------------------------------------------------------------------------ */
  planets: [
    {
      id: "archive",
      name: "The Archive",
      orb: { label: "Subscribe", href: "page.html?p=subscribe" },
      x: 50.0,
      y: 14.1,
      size: 92,
      art: { type: "earth", color: "#1f6fb2", shade: "#08213a", light: "#eaf6ff" },
      page: {
        oval: { fill: "#6a2fa8", text: "#ffb02e" },
        panel: { from: "#1d6b7a", to: "#08252b", link: "#ffe14d", layout: "right" },
        blurb:
          "You've made it: the central depository for everything ever written from the hip. Every issue, every year, every regrettable opinion \u2014 all of it still sitting right where you left it.",
        links: [
          { label: "Every Issue", href: "#" },
          { label: "By Year", href: "#" },
          { label: "Greatest Hits", href: "#" },
          { label: "Search The Archive", href: "#" },
        ],
      },
    },
    {
      id: "latest-issue",
      name: "Latest Issue",
      orb: { label: "Subscribe", href: "page.html?p=subscribe" },
      x: 66.3,
      y: 23.8,
      size: 90,
      art: { type: "basketball", color: "#f5871f", shade: "#8a3a00", light: "#ffd28a" },
      page: {
        oval: { fill: "#1b7a2f", text: "#ffd21f" },
        panel: { from: "#2a6ea8", to: "#0c2438", link: "#ffe14d", layout: "right" },
        blurb:
          "Hot off the press and still smudging. The newest dispatch of Written From The Hip is live \u2014 read it here, or have the next one delivered straight to your inbox before anybody else gets a look at it.",
        links: [
          { label: "Read It Now", href: "#" },
          { label: "Issue Notes", href: "#" },
          { label: "Send It To A Friend", href: "#" },
        ],
      },
    },
    {
      id: "mailbag",
      name: "The Mailbag",
      x: 33.7,
      y: 23.8,
      size: 88,
      art: { type: "ringed", color: "#e03a3a", shade: "#5c0d0d", light: "#ffa3a3", ring: "#ffd21f" },
      page: {
        oval: { fill: "#b5121b", text: "#ffe14d" },
        panel: { from: "#3a5a20", to: "#101c08", link: "#ffe14d", layout: "left" },
        blurb:
          "You wrote in. Sometimes to argue, occasionally to correct the record, once to ask whether any of this is fact-checked. It is not. Read the replies, or add your own to the pile.",
        links: [
          { label: "Recent Replies", href: "#" },
          { label: "Write In", href: "#" },
          { label: "Corrections", href: "#" },
        ],
      },
    },
    {
      id: "subscribe",
      name: "Subscribe",
      x: 73.0,
      y: 47.0,
      size: 86,
      art: { type: "sphere", color: "#39d94a", shade: "#0d5c17", light: "#b6ffbc" },
      page: {
        oval: { fill: "#f08a1e", text: "#7a2bd0" },
        panel: { from: "#2f8f4e", to: "#0a2a16", link: "#ffe14d", layout: "right" },
        blurb:
          "Free, weekly, and roughly the length of a coffee. Put your email in and the next issue arrives on its own. No spam, no upsell, no newsletter about the newsletter.",
        links: [
          { label: "Sign Me Up", href: "#" },
          { label: "What You Get", href: "#" },
          { label: "Refer A Friend", href: "#" },
        ],
      },
    },
    {
      id: "lineup",
      name: "Starting Lineup",
      x: 27.0,
      y: 47.0,
      size: 92,
      art: { type: "ringed", color: "#e8365d", shade: "#5c0c22", light: "#ffb3c4", ring: "#3fe0d0" },
      page: {
        oval: { fill: "#d81b2a", text: "#ffe14d" },
        panel: { from: "#1565c0", to: "#0a1f38" },
        ribbon: "Welcome To The Writer's Room",
        roster: [
          {
            name: "George Denby",
            height: "6' 1\"",
            weight: "180 lbs.",
            photo: "assets/images/george-denby.png",
            href: "bio.html?b=george-denby",
          },
          {
            name: "Thomas Bolt",
            height: "6' 4\"",
            weight: "200+",
            photo: "assets/images/thomas-bolt.png",
            href: "bio.html?b=thomas-bolt",
          },
        ],
      },
    },
    {
      id: "off-the-dome",
      name: "Off The Dome",
      x: 66.3,
      y: 70.2,
      size: 94,
      art: { type: "marbled", color: "#7a2bd0", shade: "#2b0a52", light: "#f08a1e" },
      page: {
        oval: { fill: "#7a2bd0", text: "#ffb02e" },
        panel: { from: "#7a5a1a", to: "#241905", link: "#ffe14d", layout: "left" },
        ribbon: "On Planet Off The Dome, this is our stream of consciousness that we add to daily every day daily.",
        links: [
          {
            label: "Click here to view\nour current stream\nof consciousness",
            href: "stream.html",
            wrap: true,
          },
        ],
        pointer: { photo: "assets/images/pointer-guy.png", gap: 24 },
      },
    },
    {
      id: "denbys-shorts",
      name: "Denby's Shorts",
      x: 50.0,
      y: 79.9,
      size: 84,
      art: { type: "shorts", color: "#3a7bd5", shade: "#15314f", light: "#cfe8ff", ring: "#ffd21f" },
      page: {
        oval: { fill: "#0f9e8f", text: "#ffe14d" },
        panel: { from: "#3a6ea8", to: "#0c2438", link: "#ffe14d", layout: "left" },
        ribbon: "Denby's Short Scripts, enter to learn, go fourth to serve.",
        links: [
          { label: "Real Steele Cuck", href: "script.html?s=real-steele-cuck" },
          { label: "Tush Push", href: "script.html?s=tush-push" },
          { label: "Bad Ultra Sound", href: "script.html?s=bad-ultra-sound" },
          { label: "House of Devon", href: "script.html?s=house-of-devon" },
          { label: "MILFS AD", href: "script.html?s=milfs-ad" },
          { label: "Hostage FlexTape", href: "script.html?s=hostage-flextape" },
          { label: "Therapist Breaks Fourth Wall", href: "script.html?s=therapist-breaks-fourth-wall" },
          { label: "Just Cracked My Boy", href: "script.html?s=just-cracked-my-boy" },
          { label: "Grills", href: "script.html?s=grills" },
        ],
      },
    },
    {
      id: "site-map",
      name: "Site Map",
      x: 33.7,
      y: 70.2,
      size: 84,
      art: { type: "swirl", color: "#f5871f", shade: "#4a1500", light: "#ffe14d" },
      href: "sitemap.html", // goes to its own page instead of the standard one
    },
  ],
};
