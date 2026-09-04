# -*- coding: utf-8 -*-
"""Two shelves the term pages have no room for.

1. DO NOWS AND BONUS WORK -- the short skill tasks that open a session, plus
   the assignments that are not part of a project. In Classroom these are
   scattered across eighty weekly topics and titled by date, which makes them
   unfindable four months later. Grouped here by the skill they build, because
   that is how a student looks for them: "the one where we used Forma", not
   "the one from 21 November".

   Titles are harvested from Engineering III Class 27 and Engineering IV
   Class 26. Where a Do Now was titled only by date, it is not listed -- a row
   reading "Do Now! 12/2" helps nobody. Where the instructions live in a
   Classroom attachment, that is said rather than guessed at.

2. LINKS -- somewhere to keep the things that are worth a second look but are
   not a training platform and not a project. Seeded with what is already
   verified elsewhere in this project; built to be added to.
"""

# ------------------------------------------------- Do Nows and bonus work

GROUPS = [
    dict(
        key='cad',
        title='CAD and design tools',
        blurb='Short tasks that put a tool in your hands for one session. '
              'Most take less than a period.',
        items=[
            ('Forma #1 and Forma #2', 'Autodesk Forma',
             'Two sessions in Forma, the site and environmental analysis tool. '
             'The same tool the City Design project runs on, so these are '
             'worth doing before that project rather than during it.',
             '11', 'architecture'),
            ('New Forma design tools', 'Autodesk Forma',
             'A later session on features added to Forma. The whole brief is '
             '"when done, submit all images".',
             '11', 'architecture'),
            ('Recreate house plans', 'Fusion 360 / AutoCAD',
             'Rebuild an existing set of house plans. Good practice for '
             'reading a drawing rather than only producing one.',
             '11', 'architecture'),
            ('CorelDraw shop logo', 'CorelDraw',
             'Redraw the shop logo in CorelDraw. Vector practice with a result '
             'you can actually engrave.',
             '12', 'industrial'),
            ('Fusion review: drawings', 'Fusion 360',
             'A review of Fusion&rsquo;s drawing features. Attachment-only in '
             'Classroom.',
             '11', 'mechanical'),
            ('Fusion review: stress simulations', 'Fusion 360',
             'A review of simulation. Attachment-only in Classroom.',
             '11', 'mechanical'),
        ],
    ),
    dict(
        key='new',
        title='New tools worth trying',
        blurb='Sessions built around something none of us had used before. '
              'These date faster than the rest of the site.',
        items=[
            ('Adobe Neo', 'Adobe Neo',
             'A session on Adobe&rsquo;s 3D tool. Set in both Grade 11 and '
             'Grade 12 in the same term.',
             '11 &amp; 12', 'industrial'),
            ('Brilliant.org', 'Brilliant',
             'A session on Brilliant, with a reflection. Interactive problem '
             'sets in maths, physics and computer science.',
             '12', ''),
            ('AI help for capstone', 'Gemini',
             'One of the few Do Nows with a full page of written instructions '
             '&mdash; how to use AI on a capstone without letting it do the '
             'thinking for you.',
             '11', ''),
        ],
    ),
    dict(
        key='review',
        title='Reviews and check-ins',
        blurb='Short reflective tasks. They look like admin and they are '
              'actually where the grade comes from.',
        items=[
            ('Mid-capstone review', '',
             'A checkpoint partway through the Senior Capstone, so a project '
             'that has drifted gets caught in week three rather than week six.',
             '12', ''),
            ('Monday morning independent study log',
             '', 'The weekly restart on your independent study project.',
             '11', ''),
            ('Post-lecture reflection: theory of the week', '',
             'A written reflection on the week&rsquo;s theory lecture.',
             '12', ''),
        ],
    ),
    dict(
        key='bonus',
        title='Bonus and one-off builds',
        blurb='Assignments that sit outside the project spine. Short, and '
              'often the most fun thing in the term.',
        items=[
            ('Holiday ornament', '3D printing / laser engraver',
             'A short design-and-make with a hard deadline, because the '
             'holiday does not move.',
             '12', ''),
            ('Rube Goldberg machine', '',
             'The whole class building one chain reaction where every section '
             'has to hand off to the next. An interface problem disguised as a '
             'toy.',
             '12', 'mechanical'),
            ('Moon Base 2.0', '',
             'A second run at the moon base brief, knowing what went wrong the '
             'first time. "Try again" is a real engineering exercise.',
             '12', 'architecture'),
            ('LTT screwdriver research and analysis', '',
             'Pull apart the design decisions in one deliberately '
             'over-engineered consumer tool.',
             '12', 'industrial'),
            ('Vibecoding team challenge', 'Gemini',
             'Four days, a team, and an app or game with the AI writing the '
             'code while you own the vision and the pitch.',
             '11', 'software'),
        ],
    ),
]


# ------------------------------------------------------------------ links

LINKS = [
    dict(
        title='Reference you will keep coming back to',
        blurb='Not courses. The things you open for two minutes to check '
              'something, then close.',
        items=[
            ('Autodesk Knowledge Network',
             'https://www.autodesk.com/support',
             'The official documentation for Fusion, Inventor, AutoCAD, Revit '
             'and Forma. When a tool does something you did not expect, this '
             'is where the answer actually is.'),
            ('Engineering ToolBox',
             'https://www.engineeringtoolbox.com/',
             'Material properties, thread sizes, conversions, fits and '
             'tolerances. Plain, ugly, and correct.'),
            ('McMaster-Carr',
             'https://www.mcmaster.com/',
             'A parts catalogue that doubles as a reference: nearly every '
             'listing has a CAD model you can drop straight into an assembly.'),
            ('Arduino language reference',
             'https://docs.arduino.cc/language-reference/',
             'Every function, with an example for each. Faster than searching.'),
        ],
    ),
    dict(
        title='Worth watching',
        blurb='Channels that show the work rather than only the result.',
        items=[
            ('Practical Engineering',
             'https://www.youtube.com/@PracticalEngineeringChannel',
             'Civil and structural engineering explained with physical models '
             'built in a garage. The dam and foundation videos are the best '
             'introduction to loads anywhere.'),
            ('Real Engineering',
             'https://www.youtube.com/@RealEngineering',
             'Longer-form breakdowns of how real aircraft, bridges and '
             'machines were actually designed, and what constrained them.'),
            ('This Old Tony',
             'https://www.youtube.com/@ThisOldTony',
             'Machining and fabrication, with the mistakes left in. The dry '
             'commentary hides genuinely deep process knowledge.'),
            ('Stuff Made Here',
             'https://www.youtube.com/@StuffMadeHere',
             'What happens when mechanical design, electronics and software '
             'get pushed well past sensible. A good argument for why the '
             'pathways overlap.'),
        ],
    ),
    dict(
        title='Where the free CAD models live',
        blurb='For reference geometry, for parts you do not want to model, '
              'and for seeing how other people built something.',
        items=[
            ('Printables',
             'https://www.printables.com/',
             'Prusa&rsquo;s model library. Better moderated than most, and the '
             'print settings people post are usually honest.'),
            ('GrabCAD Library',
             'https://grabcad.com/library',
             'Engineering-grade models rather than printables &mdash; motors, '
             'bearings, gearboxes, whole machines, in real CAD formats.'),
            ('Thingiverse',
             'https://www.thingiverse.com/',
             'The oldest and largest. Quality varies wildly; check the '
             '"makes" before you trust a model.'),
        ],
    ),
    dict(
        title='Where engineering jobs actually are',
        blurb='Worth a look well before senior year, because what these ask '
              'for should shape what you learn now.',
        items=[
            ('ONET: Engineering Technologists and Technicians',
             'https://www.onetonline.org/find/family?f=17',
             'The US Department of Labor&rsquo;s occupation database. What the '
             'work involves, what it pays, and what it is projected to do.'),
            ('Bureau of Labor Statistics: Architecture and Engineering',
             'https://www.bls.gov/ooh/architecture-and-engineering/home.htm',
             'The official outlook for every engineering occupation, updated '
             'yearly.'),
            ('MassHire Career Centers',
             'https://www.mass.gov/info-details/masshire-career-center-locations',
             'Massachusetts career services. The South Shore centre is the '
             'closest one to Canton, and they run apprenticeship and '
             'job-placement help you can use before you graduate.'),
        ],
    ),
]
