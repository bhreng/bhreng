# -*- coding: utf-8 -*-
"""Projects this shop has actually run, offered in the hubs as optional work.

Every entry below was harvested from a real Google Classroom class, not
invented. They sit under "Find a Project" in each pathway as a second list:
the first list is project *seeds*, these are briefs that have already been set,
built and marked.

Why they belong in the hubs rather than on a grade page: most of them ran in a
year a given student has already passed, or has not reached. A junior who wants
another mechanical project should be able to pick up the Grade 10 pullback car
redesign without being told it is not their year. The point of the hubs is that
a student can choose more work; this is a shelf of work that is known to be
good, because it has been run.

  y   the class it ran in, as a short label
  t   title
  d   what you would actually build

Sources: HARVEST-grade9-Eng-I.md, HARVEST-grade10-Eng-II.md,
PROJECT-INSTRUCTIONS-class27.md, PROJECT-INSTRUCTIONS-class26.md.
"""

RUNS = {
    'architecture': [
        ('Gr 9', 'City section around transit stops',
         'Design four distinct transit stop areas, each with a featured '
         'building. A 2D site map in AutoCAD, 3D models of the featured '
         'buildings, one area modelled in full, then the map re-presented in '
         'CorelDraw with colour, labels and a legend.'),
        ('Gr 10', 'Architectural research and rebuild',
         'Pick an iconic structure. Research it properly &mdash; architect, '
         'date, purpose, features, cultural context. Then a full day of '
         'sketching with no CAD at all, and only then three days rebuilding it '
         'in Revit, SketchUp or Fusion.'),
        ('Gr 10', 'Office shed, recreated exactly',
         'Recreate a 10&times;12 lean-to office shed from a supplied document '
         'in AutoCAD: architectural units, separate layers per element, real '
         'line weights, dimensions matching the source, elevations of all four '
         'sides, and a title block on every sheet.'),
        ('Gr 10', 'Your own house in Revit',
         'No tutorial. Recreate a floor of your own home from memory and '
         'estimate. All floors and the roof if you are feeling ambitious.'),
    ],
    'mechanical': [
        ('Gr 9', 'Take-apart toy car, reverse engineered',
         'Disassemble a toy car, measure every part with calipers, model each '
         'one as its own file, then assemble with joints so it works like the '
         'real thing. Orthographic drawings, renders, a part list, and an '
         'exploded animation as a bonus.'),
        ('Gr 10', 'Pullback car redesign, measured',
         'Redesign a pullback car for a <em>measurable</em> improvement. '
         'Baseline test it first, identify one or two real limitations, run a '
         'decision matrix over two concepts, build the prototype, then test '
         'against the baseline and account for the difference.'),
        ('Gr 10', 'CrunchLabs kit re-engineering',
         'Take the components out of old kits and build something with a new '
         'or much better function. Every part modelled in its own Fusion file, '
         'assembled into one, with an explanation of how new parts integrate '
         'with old ones.'),
        ('Gr 9', 'ANW obstacle',
         'Design an obstacle to the American Ninja Warrior Obstacle Design '
         'Challenge rules. Open-ended: sketches then a Fusion model is the '
         'suggested route, but the approach is yours.'),
        ('Gr 9', 'Rapid prototype: engraved and printed',
         'One object, multiple parts, made using both the laser engraver and '
         'the 3D printer. Original design only, with every trial print and '
         'redesign documented.'),
    ],
    'industrial': [
        ('Gr 10', 'Furniture in a box',
         'Model a piece of furniture down to the hardware, design the box it '
         'ships in, and produce two exploded animations &mdash; one coming out '
         'of the box, one from assembled to unassembled. Every part its own '
         'file.'),
        ('Gr 10', 'A table for eight that hides',
         'Seating for eight, plus configurations for four and six, and it has '
         'to disappear when not in use because the apartment is small. Screw '
         'and hardware placement must be accounted for. Sketch, 3-view '
         'AutoCAD, Fusion model, then a physical scale model.'),
        ('Gr 9', 'A product re-imagined with AI in it',
         'Take the industrial designer&rsquo;s approach &mdash; form and '
         'function first. Orthographic drawings with dimensions, a Fusion '
         'model, renders, and a promo piece. Packaging if there is time.'),
        ('Gr 10', 'Re-pitch an invention',
         'Choose an existing invention and pitch it Shark Tank style: '
         'research the inventor and the original context, analyse the market, '
         'build real financial projections, then an annotated sketch and a 3D '
         'model of the original.'),
        ('Gr 10', 'Kitchen product redesign',
         'Sketches, a 3D model, renders, orthographics and a presentation or '
         'poster. Short, and a good first industrial design brief.'),
    ],
    'automation': [
        ('Gr 10', 'Lego SumoBot',
         'Design, build and program a bot to fight in the ring. Sensors and '
         'code for movement and reaction, then a documented design rationale '
         'and either a coloured 2D drawing set or a Fusion model.'),
        ('Gr 10', 'SumoBot trials, done properly',
         'An experimental design sheet for three trials: can it stay in the '
         'circle, can it push an object out, and how heavy an object can it '
         'push. The experiment is the assignment, not the robot.'),
        ('Gr 10', 'Lego Week',
         'Six tutorial activities in Spike, then two unit plans, then find a '
         'project worth recreating. Log everything, dated, with photos.'),
        ('Gr 9', 'fischertechnik',
         'The museum manuals and the spare parts list, and permission to '
         'enjoy yourself.'),
    ],
    'project': [
        ('Gr 9', 'Two projects, three days, one clock',
         'A large-scale moonbase layout and a detailed grocery store '
         'floorplan, both in 2D AutoCAD, both due together. One needs a broad '
         'conceptual approach and the other needs dimensional accuracy '
         '&mdash; the assignment is really about allocating your time.'),
        ('Gr 9', 'Redesign this shop',
         'Measure every room, every piece of furniture, every door, window and '
         'outlet. Draw the existing layout to scale in AutoCAD, then propose a '
         'redesign in Fusion &mdash; including modelling the furniture. One '
         'constraint: one classroom loses its computers.'),
        ('Gr 10', 'The full documentation set',
         'Design brief, part list, decision matrix and Gantt chart for one '
         'project. Every form of shop documentation in one place, which is '
         'what the capstone will expect of you later.'),
        ('Gr 10', 'Compare four programs and present',
         'Pick four of the programs you have used. Usage, features, samples, '
         'product information and your professional opinion &mdash; built to '
         'be presented to the class.'),
    ],
    'software': [
        ('Gr 9', '3ds Max against Maya, in three days',
         'Learn enough of each to judge them. One simple object built in each, '
         'then a recommendation for which suits a specific kind of shop work '
         'and why. A software evaluation, written as an engineer would.'),
        ('Gr 10', 'Program the SumoBot',
         'Sensors, reactions and strategy in Spike. The mechanical build is '
         'only half of it.'),
    ],
    'electrical': [
        ('Gr 12', 'Reverse engineer a breadboard circuit',
         'Take a working circuit apart to understand it, then rebuild it and '
         'reflect on what you learned in the taking apart.'),
        ('Gr 11', 'Arduino Education Starter, all ten lessons',
         'Each lesson builds on the last, with its own logbook to fill in as '
         'you go. The most structured electronics route in the shop.'),
    ],
}


# --------------------------------------------- grade 9's exploratory visitors

EXPLORATORY = dict(
    title='Exploratory week',
    lede='Before you join a shop you spend one week in each of nine of them. '
         'If this is your exploratory week, this section is for you &mdash; '
         'the rest of the page is what the year looks like if you choose us.',
    what=[
        ('Engineering technology is not one job',
         'It is at least seven. Someone designs the part, someone works out '
         'whether it will hold, someone writes the code that moves it, '
         'someone gets it manufactured, someone manages the schedule so it '
         'ships. All of those are engineering, and they suit very different '
         'people.'),
        ('It is a trade and a degree path at the same time',
         'People leave this shop and go straight into work with certifications '
         'that employers recognise. People also leave it and go to '
         'engineering school with four years of CAD, documentation and '
         'project work behind them. Neither route is the fallback.'),
        ('The work is making things that have to actually work',
         'Not models of things. A part that comes off the printer and fits. A '
         'circuit that does what you said it would. A drawing someone else '
         'can build from without asking you a question.'),
        ('You will be wrong in public, constantly',
         'Every project here ends with testing, and testing is where you find '
         'out your prediction was off. The engineers who get good are the ones '
         'who write down the difference instead of hiding it.'),
    ],
    ask=[
        'Ask a senior what they are building for their capstone, and why they '
        'chose it.',
        'Ask what the worst thing they ever printed was, and what they '
        'changed.',
        'Look at the seven pathways and see which one you keep coming back to.',
    ],
)
