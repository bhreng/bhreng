# -*- coding: utf-8 -*-
"""
Safety content for the shop section of the site.

MAKERSPACE_RULES is transcribed verbatim from
  "BHR Engineering Makerspace Rules.pdf" (Drive, 3 Sep 2024)
and only regrouped under its own three headings. Wording is not changed.

QUIZZES holds the mastery-style equipment checks. Each question must have
exactly one correct option, and EVERY option carries an explanation --
wrong ones say why they are wrong, the right one says why it is right.
That is the whole pedagogical point: nobody guesses their way through.

The Makerspace quiz below is drawn only from the rules document. It is a
worked example of the format. The per-machine quizzes need Dan's shop
safety Classroom before they can be written honestly.
"""

NURSE_EXT = '2230'
MAX_OCCUPANCY = '12'

# --------------------------------------------------------------------------
# There are TWO rules documents and they do different jobs.
#
#   "Primary Makerspace Rules"        -- the ten conditions of entry. This is
#                                        the door. It is what the shop safety
#                                        test actually asks about.
#   "BHR Engineering Makerspace Rules" -- the thirty-two working rules, in five
#                                        themes. This is how you behave once
#                                        you are inside.
#
# The site had only the second for most of this build, which is why three
# questions on the safety test looked unanswerable.
# --------------------------------------------------------------------------

PRIMARY_RULES = [
    'Access to the Makerspace must be granted by an instructor.',
    'Access may be revoked at any time at the discretion of an instructor.',
    'Report all injuries.',
    'Proper PPE is to be worn at all times. No safety glasses&hellip; No entry.',
    'Proper attire must be worn.',
    'Keep work areas as clean as possible before, during and after use.',
    'No unapproved foods or drinks.',
    'Only trained and authorized students are permitted to operate machinery '
    'and/or hand tools.',
    'Be prepared. If you do not know something&hellip; Ask.',
    'USE COMMON SENSE.',
]

# The two words rule 8 turns on, defined in the document itself.
TRAINED_AUTHORIZED = [
    ('Trained', 'You have completed all necessary provided training.'),
    ('Authorized', 'You have successfully passed the appropriate safety tests.'),
]

MAKERSPACE_RULES = [
    ('Report all injuries.', 'Before anything else', [
        'Do not attempt to remove foreign objects from the eye or body.',
        'If chemicals get in the eye(s), wash eye(s) for 15 minutes in an open flow '
        'of water before proceeding for medical treatment.',
    ]),
    ('Use protective gear. Dress right.', 'Every time, working or not', [
        'Wear eye protection: safety glasses with side shields, goggles, or face '
        'shields at all times, whether working or not.',
        'Do not wear loose-fitting clothing around moving or rotating machinery.',
        'Remove ties, jewelry, gloves, etc. especially around moving or rotating machinery.',
        'Tie back or cover long hair to keep it away from moving machinery.',
        'Wear only shoes that cover the entire foot, no open-toe shoes or sandals.',
        'Wear suitable gloves when handling hot objects, glass, or sharp-edged items.',
        'Wear appropriate clothing for the job (i.e., do not wear short sleeve shirts '
        'or short pants when welding).',
    ]),
    ('Prepare.', 'Before you touch a tool', [
        'Safety is your top priority when using the shop. If you are not sure what you '
        'are doing, ask.',
        'Know all the locations of all first aid, fire, and safety equipment.',
        'Never use a tool unless you have been trained to use it safely.',
        'Never work alone when using power tools. Two persons must be present and be '
        'able to see one another.',
        'Do not work in the shop if tired, or in a hurry.',
        'Do not fool around, startle, or distract anyone (not even with a conversation) '
        'while either one of you are using a tool.',
        'Think through the entire job before starting. Prepare prints or drawings with '
        'all dimensions and specifications prior to using machines.',
    ]),
    ('Use tools right.', 'While you work', [
        'Use tools only as they were designed to be used. (A wrench is not a hammer.)',
        'Never use a broken tool.',
        'Report any broken tools or machines immediately.',
        'Do not remove tools from the room.',
        'Never walk away from a tool that is still on.',
        'A hard hammer should not be used to strike a hardened tool or any machine part. '
        'Use a soft-faced hammer.',
        'Operate machines only with all required guards and shields in place.',
    ]),
    ('Clean up.', 'Every time you leave an area', [
        'Clean up every time whenever you leave an area, including sweeping the floor.',
        'Clean and return all tools to where you got them.',
        'Use compressed air sparingly; never aim it at another person or use it to clean '
        'hair or clothes.',
        'Shut off and unplug machines when cleaning, repairing, or oiling.',
        'Never use a rag near moving machinery.',
        'Use a brush, hook, or a special tool to remove chips, shavings, etc. from the '
        'work area. Never use the hands.',
        'Keep fingers clear of the point of operation of machines by using special tools '
        'or devices, such as push sticks, hooks, pliers, etc.',
        'Keep the floor around machines clean, dry, and free from trip hazards. Do not '
        'allow chips to accumulate.',
        'Mop up spills immediately and put a chair or cone over them if they are wet '
        'enough to cause someone to slip.',
    ]),
]

MAKERSPACE_QUIZ = [
    {
        'q': 'Who can give you access to the Makerspace?',
        'o': [
            ('An instructor', True,
             'Correct &mdash; rule 1, and rule 2 is its other half: access can be '
             'taken away again at any time, at an instructor\'s discretion. It is '
             'permission, not a right you keep once you have it.'),
            ('Any student who is already authorized', False,
             'No. A certified peer can supervise you on some machines once you '
             'have your own access, but only an instructor grants access in the '
             'first place.'),
            ('Nobody &mdash; it is open to anyone in the program', False,
             'It is not. Rule 1 exists because the room contains things that will '
             'injure someone who wandered in.'),
            ('Whoever is running the room that period', False,
             'Close, but the rule says an instructor specifically.'),
        ],
    },
    {
        'q': 'What does it take before you are allowed to operate machinery or '
             'hand tools?',
        'o': [
            ('Being both trained and authorized', True,
             'Correct, and they are two different things. Trained means you have '
             'completed the provided training. Authorized means you have passed '
             'the appropriate safety test. Doing the training is not enough on its '
             'own, and neither is being confident.'),
            ('Being trained', False,
             'Half of it. Training is the instruction; authorization is the check '
             'that you took it in. You need both.'),
            ('Being authorized', False,
             'You cannot be authorized without the training that comes first. The '
             'rule names both words deliberately.'),
            ('Having an instructor in the room', False,
             'Necessary but not sufficient. Supervision does not substitute for '
             'training and authorization on that specific machine.'),
        ],
    },
    {
        'q': 'The Makerspace has a maximum occupancy of twelve. The room has '
             'thirteen people in it.',
        'o': [
            ('It is the instructor\'s call whether that carries on', True,
             'Correct. Twelve is the stated maximum, but it is a judgement rather '
             'than a turnstile &mdash; if the room goes over, the instructor '
             'decides whether the work happening is safe at that number.'),
            ('Someone has to leave immediately, no exceptions', False,
             'Twelve is the number, but the rule is applied with judgement. What '
             'matters is whether the work in the room is safe at that count, and '
             'that is the instructor\'s decision.'),
            ('It does not matter, occupancy is only a fire rule', False,
             'It is a working limit for a room full of machines, not just a '
             'building code number.'),
            ('You should quietly carry on and say nothing', False,
             'Whether it continues is a decision for the instructor, which means '
             'they need to know.'),
        ],
    },
    {
        'q': 'You arrive at the Makerspace without safety glasses.',
        'o': [
            ('You do not go in', True,
             'Correct, and the rule is written to be memorable: &ldquo;No safety '
             'glasses&hellip; No entry.&rdquo; PPE is a condition of being in the '
             'room at all, not something you put on when you start working.'),
            ('Go in, but stay away from the machines', False,
             'The rule is about entry, not about what you plan to do. Other '
             "people's work can reach your eyes while you are standing still."),
            ('Go in and borrow a pair from someone', False,
             'Sort the glasses out first, then come in. That is the whole point of '
             'phrasing it as an entry condition.'),
            ('Go in if an instructor is present', False,
             'An instructor being there does not change what is flying through the '
             'air.'),
        ],
    },
    {
        'q': 'You get a chemical splash in your eye. What do you do first?',
        'o': [
            ('Go straight to the nurse',
             False,
             'Not first. Every second the chemical is in contact it keeps doing damage. '
             'Rinse first, then go for treatment — the nurse will ask whether you '
             'flushed, and the answer needs to be yes.'),
            ('Rinse the eye under open flowing water for 15 minutes, then seek treatment',
             True,
             'Correct, and the 15 minutes is not a rough figure — it is the rule. It '
             'will feel far longer than it sounds. Have someone else fetch help while '
             'you stay at the water.'),
            ('Rinse for a few seconds and see if it still hurts',
             False,
             'Pain is a bad gauge. Some chemicals numb the surface and some do their worst '
             'damage after the sting fades. The 15 minutes is the rule regardless of how '
             'it feels.'),
            ('Try to wipe it out with a clean cloth',
             False,
             'This grinds the chemical across the surface of the eye and can scratch it. '
             'Never put anything into your eye — water only, and never try to remove '
             'a foreign object yourself.'),
        ],
    },
    {
        'q': 'When is eye protection required in the Makerspace?',
        'o': [
            ('At all times, whether you are working or not',
             True,
             'Correct. This is the rule that most often gets bent, and the reason it is '
             'absolute is that you are not the only person in the room. Someone else\'s '
             'work can reach your eyes while you are just walking through.'),
            ('Only when you are operating a machine',
             False,
             'Not enough. The hazard in a shared space comes from other people\'s work as '
             'much as your own. The rule is "at all times, whether working or not."'),
            ('Only when using anything that makes chips or sparks',
             False,
             'Too narrow, and it puts you in the position of judging the hazard before you '
             'are protected from it. Glasses go on when you enter.'),
            ('Whenever the instructor says so',
             False,
             'The rule does not depend on being told. It is on you the moment you walk in.'),
        ],
    },
    {
        'q': 'You want to make one quick cut on a power tool. Nobody else is in the shop.',
        'o': [
            ('Make the cut — it is only one and you know how',
             False,
             'This is the single most dangerous habit in a shop, and "it was only going to '
             'take a second" is what people say afterwards. Never work alone with power '
             'tools.'),
            ('Wait until a second person is present and can see you',
             True,
             'Correct. Two people must be present and able to see one another. The point '
             'is not supervision — it is that if something goes wrong, someone knows '
             'immediately.'),
            ('Prop the door open so someone would hear you',
             False,
             'Hearing is not seeing. The rule specifically requires two people who can see '
             'each other, because the injuries that matter most can leave you unable to '
             'call out.'),
            ('Text a friend to say what you are doing',
             False,
             'A message is not a person in the room. The requirement is a second person '
             'present and in line of sight.'),
        ],
    },
    {
        'q': 'A machine is running and you need to step away for a moment.',
        'o': [
            ('Shut it off before you go',
             True,
             'Correct. Never walk away from a tool that is still on. A running machine with '
             'nobody at it is a hazard to whoever walks past next.'),
            ('Leave it — you will only be a few seconds',
             False,
             'This is exactly the case the rule exists for. A machine that is running and '
             'unattended is a hazard to everyone else in the room, and "a few seconds" has '
             'a way of becoming longer.'),
            ('Ask someone nearby to keep an eye on it',
             False,
             'You have now made your machine someone else\'s problem while they are doing '
             'their own work. Shut it off.'),
            ('Leave it if the guards are in place',
             False,
             'Guards protect the operator at the point of operation. They do not make an '
             'unattended running machine safe.'),
        ],
    },
    {
        'q': 'You need to clear metal chips and shavings off a machine bed.',
        'o': [
            ('Use a brush, hook, or the proper tool',
             True,
             'Correct — and shut the machine off and unplug it first. Chips are '
             'sharp, often hot, and hide edges you cannot see.'),
            ('Brush them off with your hand',
             False,
             'Never use your hands. Chips are razor-edged and frequently still hot; this '
             'is one of the most common shop injuries there is.'),
            ('Blow them off with compressed air',
             False,
             'Compressed air is to be used sparingly, and never for this — it fires '
             'chips across the room and into people\'s eyes, including your own.'),
            ('Wipe them off with a rag',
             False,
             'A rag near machinery can catch and pull your hand in. Never use a rag near '
             'moving machinery, and use the proper tool for chips.'),
        ],
    },
    {
        'q': 'A guard on a machine keeps getting in your way on an awkward cut.',
        'o': [
            ('Remove it for this one cut, then put it back',
             False,
             'No. Machines run only with all required guards and shields in place — '
             'there is no version of this rule with an exception for awkward cuts.'),
            ('Stop, and ask an instructor for a different approach',
             True,
             'Correct. If the guard is in the way, the setup is wrong, not the guard. There '
             'is almost always another way to hold the work or another machine for the job.'),
            ('Work around it as carefully as you can',
             False,
             'Better than removing it, but you are still fighting the setup, and careful is '
             'not a control. Stop and ask — the answer is usually a better fixture.'),
            ('Ask another student to hold the guard clear',
             False,
             'This puts a second pair of hands into the danger zone. Now two people are at '
             'risk instead of one.'),
        ],
    },
    {
        'q': 'You spot a tool with a cracked handle in the rack.',
        'o': [
            ('Report it immediately',
             True,
             'Correct. Report any broken tool or machine straight away. Leaving it in the '
             'rack means the next person finds it the hard way.'),
            ('Put it back and pick a different one',
             False,
             'You are safe, but the next person is not — and they may not notice the '
             'crack. A broken tool that stays in the rack will be used.'),
            ('Use it gently, it is only a small crack',
             False,
             'Never use a broken tool. A cracked handle fails suddenly and under load, '
             'which is the worst possible moment.'),
            ('Take it home to fix it',
             False,
             'Tools do not leave the room. Report it and let it be dealt with properly.'),
        ],
    },
    {
        'q': 'You are about to use a machine you have not been trained on, but you have '
             'watched a video and it looks straightforward.',
        'o': [
            ('Get trained on it first',
             True,
             'Correct. Never use a tool unless you have been trained to use it safely. A '
             'video cannot show you this machine\'s condition, quirks or setup.'),
            ('Try it — you understand how it works',
             False,
             'Understanding how a machine works and being able to run it safely are '
             'different things. Training exists for the gap between them.'),
            ('Try it while someone watches',
             False,
             'An untrained observer cannot catch a mistake they also would not recognise. '
             'Get trained.'),
            ('Try it on scrap material first',
             False,
             'The material does not change the hazard. The machine behaves the same way '
             'whether the piece matters or not.'),
        ],
    },
]

# machine key -> (display name, blurb, questions)
QUIZZES = {
    'makerspace': (
        'Makerspace general safety',
        'The rules that apply the moment you walk in, whatever you are working on.',
        MAKERSPACE_QUIZ,
    ),
}

# SDS library as it stands in Drive, June 2023. Counts are what was found.
SDS_FOLDERS = [
    ('Adhesive', '1TXAyGdhbRZwZM5iGfh08ortCw3_8BMLg',
     'Gorilla Glue and Tape, Krazy Glue, the Elmers range, Flex Seal, rubber cement, '
     'spray adhesive.'),
    ('3D Printing', '15bTMg1LBXBH6qtzTTuKtmOMxv8blZpNd',
     'PLA filament, plus the full Stratasys PolyJet resin set and its cleaning fluids.'),
    ('Paint', '1wSAI09fo9ak5wJLuzV46qzozWr3px8rL',
     'Acrylics, Arteza, Rust-Oleum filler primer, Dupli-Color clearcoat.'),
    ('Materials', '1ttB4qMdGDp5hPxfgnaTvJ4QyTM8JZWd4',
     'Lumber and plywood.'),
    ('Cleaning', '1y44QmnnMZ_mqOl7Q17LCixLexVF-mGHR',
     'Isopropyl alcohol, Goo Gone, whiteboard cleaner, wet wipes.'),
    ('MISC', '1cdRAiCEcBDnVVIS4QSrd4YLppdOaj3aw',
     'WD-40, air-hardening clay, alcohol prep pads, dry-erase markers, and others.'),
]

SDS_FOLDER_ROOT = '1d28zuw7UKzOz7l6mRSXC_d0XShvk9VY9'


# ---------------------------------------------------------------------------
# The "which theme" exercise, taken from Section 2 of the existing
# BHR Engineering Shop Safety Test (Google Form, 15 points, two sections).
# All ten rules below are quoted from that Form. The correct theme for each is
# derived from where that rule actually sits in the Makerspace Rules document,
# so nothing here is guessed.
#
# The Form asks students to answer with a number, 1-5. This version uses the
# theme names instead -- a student who has read the document knows the names,
# and the numbering is an artefact of the paper layout rather than anything
# worth memorising.
# ---------------------------------------------------------------------------

THEMES = [
    'Report all injuries',
    'Use protective gear. Dress right',
    'Prepare',
    'Use tools right',
    'Clean up',
]


def _t(correct, why):
    """Build a five-option theme question."""
    return [(name, name == correct, why if name == correct else _WRONG % name)
            for name in THEMES]


_WRONG = ('Not "%s". Go back to the rules document and find which heading this '
          'rule actually sits under &mdash; the grouping is the point of the '
          'exercise, because it tells you when to be thinking about it.')

_THEME_ITEMS = [
    ('Think through the entire job before starting. Prepare prints or drawings '
     'with all dimensions and specifications prior to using machines.',
     'Prepare',
     'Right. This is planning work you do before the machine is even on, which '
     'is what the whole Prepare group is about.'),
    ('Keep fingers clear of the point of operation of machines by using special '
     'tools or devices, such as push sticks, hooks, pliers, etc.',
     'Clean up',
     'Right, and it surprises people. It sits under Clean up because it lives '
     'alongside the other rules about getting material and debris away from a '
     'machine without putting your hands where the cutting happens.'),
    ('Wear only shoes that cover the entire foot, no open-toe shoes or sandals.',
     'Use protective gear. Dress right',
     'Right. Footwear is protective gear, the same as eye protection &mdash; it '
     'is what you are wearing rather than what you are doing.'),
    ('Never use a tool unless you have been trained to use it safely.',
     'Prepare',
     'Right. Training is something you have before you start, which puts it in '
     'Prepare rather than in the rules about using the tool itself.'),
    ('Do not fool around, startle, or distract anyone (not even with a '
     'conversation) while either one of you are using a tool.',
     'Prepare',
     'Right. This is about the state of the room and the people in it before and '
     'during work &mdash; the same readiness the rest of Prepare covers.'),
    ('Do not attempt to remove foreign objects from the eye or body.',
     'Report all injuries',
     'Right. It is one of the two rules attached to what happens after someone is '
     'hurt, which is why it sits with reporting rather than anywhere else.'),
    ('Never use a rag near moving machinery.',
     'Clean up',
     'Right. Cleaning is exactly when someone reaches for a rag, and it is exactly '
     'when a rag gets caught and takes a hand with it.'),
    ('Safety is your top priority when using the shop. If you are not sure what '
     'you are doing, ask.',
     'Prepare',
     'Right. Asking is something you do before you act, which is what Prepare '
     'is for.'),
    ('Wear eye protection: safety glasses with side shields, goggles, or face '
     'shields at all times, whether working or not.',
     'Use protective gear. Dress right',
     'Right &mdash; and note "whether working or not", which is what makes it '
     'about what you wear rather than about what you do.'),
    ('Know all the locations of all first aid, fire, and safety equipment.',
     'Prepare',
     'Right. Knowing where the extinguisher is only helps if you learned it '
     'beforehand. That is Prepare.'),
]

THEME_QUIZ = [{'q': 'Which theme does this rule fall under?<br><em>&ldquo;%s&rdquo;</em>'
                    % text,
               'o': _t(correct, why)}
              for text, correct, why in _THEME_ITEMS]

QUIZZES['themes'] = (
    'Rule themes',
    'Ten rules from the shop safety test. Say which of the five groups each one '
    'belongs to.',
    THEME_QUIZ,
)


# ---------------------------------------------------------------------------
# Safe and appropriate technology use. General section -- it applies to the
# scanner, the cameras, the computers, the AI tools and the printers alike.
# This is judgement rather than hazard, which is why it sits with the general
# rules rather than in the equipment checks.
# ---------------------------------------------------------------------------

TECH_QUIZ = [
    {
        'q': 'You want to 3D scan a classmate\'s head for a project.',
        'o': [
            ('Ask them first, and accept no for an answer', True,
             'Correct. A scan of a person is a record of their body, and it is '
             'theirs to agree to or refuse. Ask, say what it is for, and if they '
             'say no that is the end of it &mdash; not a negotiation.'),
            ('Just scan them, it is only a shape', False,
             'It is a shape that is unmistakably them, and it can be copied, '
             'shared and printed without their knowledge. Consent first.'),
            ('Scan them and ask afterwards', False,
             'Consent has to come before, or it is not consent. By then the file '
             'already exists.'),
            ('Ask the instructor instead of the person', False,
             'The instructor cannot give permission on someone else\'s behalf. '
             'The person whose face it is decides.'),
        ],
    },
    {
        'q': 'You find a great model online and want to print it and enter it in '
             'a competition as your design.',
        'o': [
            ('No &mdash; check the licence, and never present someone else\'s '
             'work as yours', True,
             'Correct on both halves. Most models carry a licence saying what you '
             'may do &mdash; personal use, attribution, no commercial use. And '
             'passing off someone else\'s design as your own is the one thing '
             'that will actually end a project, a grade, or later a job.'),
            ('Yes, if it is free to download', False,
             'Free to download is not the same as free to do anything with. '
             'Almost every model carries a licence, and most require attribution '
             'at minimum.'),
            ('Yes, if you change it a bit', False,
             'A derivative of someone\'s work is still based on their work. '
             'Check the licence, and say what you started from.'),
            ('Yes, if you do not sell it', False,
             'Non-commercial licences allow use, not misrepresentation. Entering '
             'it as your own design is the problem, regardless of money.'),
        ],
    },
    {
        'q': 'You used AI to generate part of your code, your report or your '
             'renders.',
        'o': [
            ('Say so, and check that it is actually right', True,
             'Correct, and both halves matter. Say what you used it for &mdash; '
             'that is normal professional practice now, not an admission. And '
             'verify it: AI produces confident, plausible, wrong answers, and '
             'the engineer who signs off on it owns the mistake.'),
            ('Say nothing &mdash; the output is what is graded', False,
             'What is graded is your engineering judgement, and hiding your '
             'method makes it impossible to assess. Undisclosed is the problem, '
             'not the tool.'),
            ('Only mention it if asked', False,
             'Waiting to be asked is a decision to conceal. Put it in the '
             'logbook and move on.'),
            ('Use it, but only for things you cannot check', False,
             'Exactly backwards. The things you cannot verify are the ones where '
             'a confident wrong answer does the most damage.'),
        ],
    },
    {
        'q': 'A machine has a software setting or a firmware tweak that would let '
             'you skip a safety feature and finish faster.',
        'o': [
            ('Do not touch it &mdash; a software bypass is a bypass', True,
             'Correct. Defeating an interlock in software is exactly the same act '
             'as taping the switch down; it just leaves less evidence. If a '
             'safety feature is genuinely in the way, that is a conversation with '
             'an instructor, not a settings change.'),
            ('It is fine if it is a setting the manufacturer provides', False,
             'A setting existing does not make it appropriate for a school shop. '
             'Ask before changing anything that touches a safety function.'),
            ('It is fine if you set it back afterwards', False,
             'The risk is while it is off, and people forget to set things back. '
             'And the next user has no idea.'),
            ('It is fine if you know what you are doing', False,
             'The people who defeat safety systems always believe this. It is not '
             'your call to make alone.'),
        ],
    },
    {
        'q': 'You take a photo in the shop that has other students in it.',
        'o': [
            ('Ask before posting it anywhere', True,
             'Correct. Your project photos are yours; other people\'s faces are '
             'not. Ask, or frame the shot so it is your work rather than the '
             'room. This applies to anything that leaves the building.'),
            ('Post it &mdash; it is a public space', False,
             'A classroom is not a public space, and photographs of students '
             'carry rules that apply to you as well as to the school.'),
            ('Post it if nobody is doing anything embarrassing', False,
             'That judgement is theirs, not yours. Ask.'),
            ('Post it if you do not tag anyone', False,
             'Being recognisable is enough. Not tagging does not make it '
             'anonymous.'),
        ],
    },
    {
        'q': 'Someone asks you to design or print something and you are not sure '
             'it is allowed.',
        'o': [
            ('Ask an instructor before you start', True,
             'Correct, and asking is not getting anyone in trouble &mdash; it is '
             'the normal way to resolve it. The shop makes a lot of things; there '
             'are a few it does not, and the fastest way to find the line is to '
             'ask where it is.'),
            ('Make it and see if anyone objects', False,
             'By then it exists, and you made it. Ask first; it takes a minute.'),
            ('Refuse and say nothing', False,
             'Refusing is fine. Saying nothing means that if it was genuinely a '
             'problem, nobody found out.'),
            ('Make it but do not put your name on it', False,
             'Anonymity is not a substitute for judgement, and it will be traced '
             'to the machine and the account anyway.'),
        ],
    },
    {
        'q': 'You are working on a shop computer signed in to your school '
             'account, and the bell goes.',
        'o': [
            ('Sign out before you leave', True,
             'Correct. A signed-in account is your name on whatever happens next '
             '&mdash; your files, your email, your submissions. Signing out takes '
             'a couple of seconds and is entirely your responsibility.'),
            ('Just lock the screen', False,
             'Better than nothing on your own machine. On a shared shop computer '
             'the next student needs it, and they will simply restart it &mdash; '
             'back into your session.'),
            ('Leave it, the next person will sign you out', False,
             'They might, or they might use it. Either way, anything done in that '
             'session is under your name.'),
            ('Leave it if you are coming back next period', False,
             'A whole period is plenty of time for it to matter.'),
        ],
    },
    {
        'q': 'Why is this in a safety test?',
        'o': [
            ('Because the tools here can affect other people, not just you', True,
             'Correct. A scanner records someone\'s body, a camera records their '
             'face, an account carries their name, a printer makes an object that '
             'leaves the room. Most shop safety is about not hurting yourself. '
             'This part is about not hurting anyone else.'),
            ('It is not really safety, just school rules', False,
             'Consent, privacy and honest attribution are not school etiquette '
             '&mdash; they are the parts of professional practice that get people '
             'fired rather than told off.'),
            ('To stop people misusing equipment', False,
             'Partly, but the framing matters: this is about the people affected '
             'by what you make, not about protecting the machines.'),
            ('Because of AI', False,
             'AI is one part of it. Scanning, photography, licensing and accounts '
             'were all here first.'),
        ],
    },
]

QUIZZES['tech'] = (
    'Safe and appropriate technology use',
    'Scanning, cameras, AI, licences and accounts &mdash; the part of shop '
    'practice that affects other people.',
    TECH_QUIZ,
)
