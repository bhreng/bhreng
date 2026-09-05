# -*- coding: utf-8 -*-
"""Assignments by term, for the two grades Mr. Frank delivers.

Organised by TERM, not by week. Dan's Classroom is week-by-week because that is
how it is taught; a student looking something up months later does not remember
which week it was in, and the weekly framing makes the year look like eighty
separate things instead of a dozen real projects.

Every entry is condensed from the assignment's own instruction text, harvested
from Google Classroom on 4 September 2026. Where a brief is thin in Classroom,
the entry here is thin too, and says so rather than padding it out.

Multi-week projects are ONE entry, not one per week, and a project's
mid-project review and its reflection are folded into it. Where a deliverable
was clearly implied by the original post but never stated, it is written out;
every such addition is recorded in the teacher notes at the foot of the
matching harvest file, so it is always possible to tell what Classroom said
from what was added.

DELIBERATELY OMITTED, and they must stay omitted:
  * the Arduino class and activation codes (Term 2 Wk 2)
  * the Gmetrix class join code
Both are live and belong in Classroom, not on a public page.

Fields:
  t     term, 1-4, or 'eoy' / 'always'
  w     week label as Classroom has it, for cross-reference
  title
  kind  project | skills | course | reflection | admin
  hook  one sentence: what you actually make
  body  paragraphs of what the assignment asks for
  gives list of deliverables
  tool  software and hardware it runs on
  path  pathway page key this belongs to, or ''
  note  a line worth knowing that is not in the brief itself
  links (optional) [(label, url, what it is)] -- the meaningful attachments and
        references for this assignment

The full instruction text is NOT stored here. It lives in the harvest files and
is parsed by brief_text.py at build time, so there is exactly one copy of every
brief and re-harvesting updates the site automatically.

ADDING A LINK TO AN ASSIGNMENT
------------------------------
Add a links=[...] entry to that assignment. Each item is
(label, url, what it is):

    links=[('VEX V5 STEM Labs', 'https://education.vex.com/stemlabs/v5',
            'The Play / Apply / Rethink / Know activities the brief sends '
            'you to.')],

A Drive file works the same way. Set the file to "anyone with the link --
viewer" first; a link nobody can open is worse than no link. For a template
each student should get their own copy of, replace everything from /edit
onward in the URL with /copy.
"""

# --------------------------------------------------------------- grade eleven

G11 = [
    dict(t=1, w='Wk 1', title='Speaker Design', kind='project',
         hook='A custom casing for a Bluetooth speaker, designed around the '
              'components that have to fit inside it.',
         body=['The first project of the year, and it is a warm-up on purpose '
               '&mdash; it puts the whole design process back in your hands '
               'after the summer.',
               'It is not just a nice-looking box. You are designing for the '
               'components: how the speaker, the battery and the circuit board '
               'are held, and how the whole thing goes together.'],
         gives=['At least two distinct concepts, sketched on paper first',
                'A Fusion 360 model of the concept you chose',
                'A parts list of the reference components &mdash; speakers, '
                'power connectors, PCB',
                'The voltage requirement of your speaker, and a battery that '
                'matches it',
                'A prototype, if there is time and the design is approved',
                'A short reflection: what changed between your first '
                'sketch and the final model, and why'],
         tool='Fusion 360, 3D printing', path='mechanical',
         note='The safety test and acknowledgement are in this same week. '
              'Nothing gets built before they are done.'),

    dict(t=1, w='Wk 2', title='Roles of an Engineer', kind='skills',
         hook='Short written descriptions of all seven engineering roles.',
         body=['Write a short description of each of the seven Roles of an '
               'Engineer in a Google Doc, using the slide deck as your base. '
               'Chapter 2 of the Engineering Fundamentals book covers the same '
               'ground.'],
         gives=['One Google Doc, seven roles described'],
         tool='', path='project',
         note='This is the setup for the Full Scope Project. Those seven roles '
              'are the roles you then have to work in.'),

    dict(t=1, w='Wk 2&ndash;4', title='Full Scope Project',
         kind='project',
         hook='Three weeks working as a different kind of engineer each week, '
              'with a real deliverable for each role.',
         body=['It starts with a vision statement for a theme park of your own '
               '&mdash; its theme, the experience you want visitors to have, '
               'what makes it different, and who it is for. That gives the '
               'seven engineering roles something concrete to act on.',
               'You then choose a new role &mdash; or more than one &mdash; '
               'each week and produce what a professional in that field would '
               'actually produce. Some weeks you will have to take two roles, '
               'so think about which ones pair well.',
               'Monday: submit your Weekly Planner. Friday: submit your '
               'Project Reflection with all project files.'],
         gives=['A vision statement for the park',
                '<b>Design Engineer</b> &mdash; a drawing set or a CAD model',
                '<b>Research Engineer</b> &mdash; research and a prediction '
                'about a new use for an existing item',
                '<b>Development Engineer</b> &mdash; a model or a prototype',
                '<b>Production &amp; Construction</b> &mdash; a Work Breakdown '
                'Structure and a Gantt chart',
                '<b>Operations Engineer</b> &mdash; a large-scale system '
                'design with operational notes',
                '<b>Sales Engineer</b> &mdash; a marketing piece that sells '
                'the engineering behind the product',
                '<b>Management Engineer</b> &mdash; an imaginary team with '
                'tasks assigned to each person'],
         tool='Fusion 360, AutoCAD, Google Docs, Gantt chart template',
         path='project',
         note='Each of the three weeks carries the same instructions. Only '
              'the role you pick changes.'),

    dict(t=1, w='Wk 3', title='Tiny House', kind='project',
         hook='A detailed tiny house in Fusion 360 &mdash; 400 sq ft or less, '
              'so every space has to do more than one job.',
         body=['The first large project of junior year. Think less about '
               '&ldquo;rooms&rdquo; and more about &ldquo;spaces&rdquo;: how '
               'they blend into each other, and how one space can serve more '
               'than one purpose.',
               'You can either convert an existing structure into a tiny '
               'house, or frame a design built from scratch.'],
         gives=['A design brief',
                'The Fusion 360 model, every item its own <b>named</b> '
                'component',
                '2D floor plans and elevations',
                '3D renderings',
                'At least one animated item &mdash; a door counts, but a '
                'space-saving feature is a better answer',
                'A Google Doc listing anything you borrowed, from a classmate '
                'or from online'],
         tool='Fusion 360', path='architecture',
         note='Work in multiple files if it suits you &mdash; a project folder '
              'with each part as its own file. Include the tables you built '
              'last year, and make some of the furniture yourself rather than '
              'pulling all of it from GrabCAD.'),

    dict(t=2, w='Wk 1', title='ADU Design Project', kind='project',
         hook='A 3D model of an Accessory Dwelling Unit, under the '
              'Massachusetts Affordable Homes Act.',
         body=['Massachusetts now lets homeowners in single-family zones build '
               'one ADU by right. That is a real market for small, affordable '
               'housing, and you are the design engineer for one.',
               '<b>Phase 1 &mdash; ideation and research.</b> Define your ADU, '
               'then sketch several conceptual floor plans (studio, '
               'one-bedroom, lofted) and pick one on space use, rough material '
               'cost, and MA ADU compliance.',
               '<b>Phase 2 &mdash; modelling and documentation.</b> Build the '
               'full model, then generate the drawings from it.',
               '<b>Phase 3 &mdash; reflection.</b> Keep the Daily Journal Log '
               'running the whole way, including what went wrong in Fusion and '
               'how you got out of it.'],
         gives=['<b>ADU type</b> &mdash; detached new build, garage '
                'conversion, or attached addition',
                '<b>Target size</b> &mdash; the exact square footage, which '
                'must be 900 sq ft or under',
                '<b>Target user</b> &mdash; who actually lives in it',
                'A complete Fusion 360 model showing kitchen, bath, sleeping '
                'area, walls, roof, windows and doors',
                'A dimensioned <b>floor plan</b>, labelled, with the separate '
                'entrance shown',
                'An <b>elevation view</b> of one exterior side',
                'The mid-project feasibility check',
                'The completed Daily Journal Log'],
         tool='Fusion 360', path='architecture',
         note='The Mid-Project Design Review and Feasibility Check is part of '
              'this project, not a separate assignment. Partway through, '
              'stop and check the square footage, the layout, and whether '
              'anything in the model would be impossible to build.'),

    dict(t=2, w='Wk 2', title='Intro to ESEC: Arduino', kind='course',
         hook='The Arduino Education Starter course &mdash; ten lessons that '
              'build from nothing to working circuits and code.',
         body=['Each lesson builds on the one before and gives you a chance to '
               'apply what the last one taught. The course has its own '
               'logbook, which you fill in as you go and submit at the end.',
               'Sign up through the under-18 route at '
               '<code>app.arduino.cc/minors</code>. The class code and '
               'activation code are in Classroom &mdash; they are not '
               'published here.'],
         gives=['The completed student logbook, filled in as you go',
                'A written reflection on the course: hardest lesson, what '
                'you could now build alone, what you would still need help '
                'with'],
         tool='Arduino Education Starter kit',
         links=[
             ('Arduino under-18 signup', 'https://app.arduino.cc/minors',
              'The signup route for students under eighteen. Not the generic '
              'Arduino signup &mdash; use this one.')],
         path='electrical', note=''),

    dict(t=2, w='Wk 3', title='VEX V5 Clawbot Project', kind='project',
         hook='Build the Clawbot, program it, then document the whole thing '
              'as one professional project record.',
         body=['Build the VEX V5 Clawbot from the provided guides. Once it '
               'works, go through the Play, Apply, Rethink and Know sections '
               'on the VEX site, documenting everything as you go.',
               'This one is explicitly about proving Documentation, Technical '
               'Knowledge and Analysis &mdash; three of the shop’s core '
               'concepts &mdash; not just about getting a robot moving.'],
         gives=['<b>Log book</b> &mdash; the build, the problems, and the '
                'fixes you actually applied',
                '<b>Major part list (BOM)</b> &mdash; a real table with port '
                'numbers and a function for every part',
                '<b>Code and annotations</b> &mdash; screenshots of your VEX '
                'code, annotated to explain what each block and variable is for',
                '<b>Modification justification</b> &mdash; what you changed, '
                'tied to a specific weakness you saw during testing'],
         tool='VEX V5, VEXcode, Google Slides',
         links=[
             ('VEX V5 STEM Labs', 'https://education.vex.com/stemlabs/v5',
              'The Play / Apply / Rethink / Know activities the brief sends '
              'you to. Free and open, no account needed.')],
         path='automation', note=''),

    dict(t=2, w='Wk 3', title='Intro to CorelDraw', kind='skills',
         hook='A day of teaching yourself CorelDraw, with something to show '
              'for it.',
         body=['A short intro, then independent learning. Work with '
               'classmates and get their feedback. By the end of the day, '
               'upload whatever shows you got there &mdash; files, images, '
               'screenshots, written descriptions.'],
         gives=['A beginner tutorial, completed',
                'A full walkthrough of making something, completed',
                'Something of your own, built around a new skill from a video',
                'Whatever else you make with the time left'],
         tool='CorelDraw, laser engraver', path='industrial', note=''),

    dict(t=2, w='Wk 4', title='Simple Machines to Functional Mechanisms',
         kind='project',
         hook='A handheld mechanism that comes off the printer already moving.',
         body=['You move from digital designer to mechanical engineer here. '
               'The real test is the <b>physical gap</b>: the tolerance that '
               'lets printed plastic parts move against each other instead of '
               'fusing solid.',
               '<b>Part 1 &mdash; the digital foundation.</b> Model and '
               'animate two different simple machines of your choice, each '
               'with working joints (revolute, slider, and so on).',
               '<b>Part 2 &mdash; the mechanism.</b> Design one mechanical '
               'fidget or mechanism sandbox: something you hold and interact '
               'with, using at least two simple machines together. A coin '
               'vending fidget or a rack-and-pinion slider are the kind of '
               'thing.'],
         gives=['Three renders &mdash; one per simple machine, one for the '
                'mechanism',
                'Animation exports showing all three in motion',
                'A motion link, so moving the input moves the outputs',
                'A printed prototype that moves freely without being forced'],
         tool='Fusion 360, 3D printing', path='mechanical',
         note='Leave a tolerance gap between all moving parts &mdash; 0.3 mm '
              'is the suggested figure. If the parts touch in Fusion, they '
              'come off the printer stuck together permanently.'),

    dict(t=2, w='Wk 5', title='Robotic Arm Build', kind='project',
         hook='A robotic arm cut on the engraver, prototyped in cardboard '
              'first.',
         body=['Follow the video to design the arm. Start with a cardboard '
               'prototype; the finished product is wood. The engraver needs 2D '
               'drawings of the parts.'],
         gives=['A cardboard prototype',
                '2D part drawings for the engraver',
                'The finished arm in wood',
                'Orthographic drawings of the final product'],
         tool='Laser engraver, CorelDraw', path='mechanical', note=''),

    dict(t=2, w='Wk 5', title='Elegoo Uno Project Kit', kind='course',
         hook='Every tutorial in the kit, worked through as a class.',
         body=['Document the project in a Google Doc as you go &mdash; '
               'pictures, screenshots, and writing about what you did.'],
         gives=['One documented Google Doc'],
         tool='Elegoo Uno kit', path='electrical', note=''),

    dict(t=3, w='Wk 2', title='Creative Concept Design', kind='project',
         hook='One day, no constraints, and a high bar.',
         body=['You have the floor, the tools and total creative freedom. '
               'Design, model and refine anything you can think of in a '
               'professional CAD program.',
               'There are no requirements for <i>what</i> you build. There are '
               'expectations for <i>how</i> you build it: intricate detail, '
               'moving parts, or structure that would actually stand up.'],
         gives=['One model that genuinely filled the day'],
         tool='Fusion 360, Revit, AutoCAD', path='mechanical',
         note='Use the advanced tools &mdash; lofts, sweeps, patterns, '
              'parameters, architectural families. Not Lego-style building. '
              'If it looks like twenty minutes of work, it was.'),

    dict(t=3, w='Wk 3&ndash;4', title='City Design', kind='project',
         hook='The whole class as one firm, designing and printing a modern '
              'city that has to fit together.',
         body=['<b>Phase 1 &mdash; the master plan.</b> The class acts as the '
               'urban planning board. Pick a real or fictional site in '
               'Autodesk Forma, run its analysis for sun hours, wind and '
               'noise, and let that data decide where green space goes and '
               'where the high-rises go. Then zone the city and assign each '
               'student a zone.',
               '<b>Phase 2 &mdash; the infrastructure standard.</b> The class '
               'agrees one connection standard so a building designed by one '
               'student fits the road designed by another: block size, the '
               'four-sided connection system, and the exact sidewalk height '
               'and road width.',
               '<b>Phase 3 &mdash; architecture.</b> Each student models onto '
               'a copy of the master base tile, using the Forma data to '
               'justify the design, and builds at least one high-detail '
               'featured building.',
               '<b>Phase 4 &mdash; production.</b> Simple massing prints for '
               'the background, high detail for the featured buildings, all '
               'clicked into the master layout on the classroom table.'],
         gives=['One digital master site plan',
                'One physical scale model',
                'Named roles: <b>Project Manager</b> holds the Forma master '
                'file and the deadlines; <b>Infrastructure Lead</b> prints the '
                'road and park tiles everyone connects to; <b>Zoning Leads</b> '
                'for residential, commercial and industrial',
                'A written reflection: your role, where the interface '
                'standard held and where it failed, and what you would set '
                'differently next time'],
         tool='Autodesk Forma, Fusion 360, 3D printing',
         links=[
             ('Autodesk Forma', 'https://www.autodesk.com/products/forma',
              'The site and environmental analysis tool Phase 1 runs on.')],
         path='project',
         note='This is the closest thing in the course to how a real firm '
              'works &mdash; one shared master file, an agreed interface '
              'standard, and named responsibility.'),

    dict(t=3, w='Wk 4', title='Learning Revit!', kind='course',
         hook='The Revit certification-prep course on the Autodesk Learning '
              'Portal, at your own pace, logged as you go.',
         body=['This moves you into BIM &mdash; Building Information Modeling '
               '&mdash; through the <i>Revit for Architectural Design '
               'Professional Certification Prep</i> course.',
               'You manage your own pace. Credit comes from the progress log, '
               'not from finishing fast.'],
         gives=['<b>Module title</b> for every lesson or exercise completed',
                '<b>Evidence</b> &mdash; a screenshot of the finished model, '
                'the lesson-complete check, or your quiz result',
                '<b>Technical reflection</b> &mdash; the tool you used and how '
                'it applies to a real building project'],
         tool='Revit, Autodesk Learning Portal',
         links=[
             ('Autodesk Learning Portal', 'https://www.autodesk.com/learning',
              'Where the Revit certification-prep course lives. Free with '
              'your Autodesk education account.')],
         path='architecture', note=''),

    dict(t=4, w='Wk 1', title='Famous Architect Presentation', kind='project',
         hook='A three to five minute presentation on one architect.',
         body=['Pick an architect and present their life and work. Show both '
               'conceptual and detail design work alongside real photographs, '
               'and include biographical information.'],
         gives=['A 3&ndash;5 minute presentation'],
         tool='', path='architecture', note=''),

    dict(t=4, w='Wk 3', title='Fusion Review: Drawings and Stress Simulations',
         kind='skills',
         hook='Two review sessions on the Fusion features that matter most '
              'for the capstone.',
         body=['The drawings environment, and stress simulation. The material '
               'is in the Classroom attachments.'],
         gives=[], tool='Fusion 360', path='mechanical',
         note='Nothing is submitted separately. You are expected to use both '
              'in the capstone.'),

    dict(t=4, w='Wk 5', title='The End-of-Year Vibecoding Team Challenge',
         kind='project',
         hook='Four days for a team to design, build and pitch an app or game, '
              'with the AI writing the code.',
         body=['You are Tech Directors and Creative Founders for a week. '
               'Gemini does the syntax; your team owns the vision, the user '
               'experience, the logic and the pitch. Pick something you '
               'actually want to use or play.',
               '<b>Days 1&ndash;2 &mdash; vision and business strategy.</b> '
               'Establish the product identity and draft a one-page business '
               'plan: audience, features, marketing angle.',
               '<b>Days 3&ndash;4 &mdash; the hackathon.</b> Generate the '
               'prototype, piece it together, test it, direct the changes. '
               'When it breaks, paste the error back in and say where it '
               'broke.',
               '<b>Day 5 &mdash; the pitch.</b> Business plan and code demo, '
               'in one punchy deck.'],
         gives=['<b>Product Owner</b> &mdash; directs the AI on the core '
                'vision and owns the user experience',
                '<b>Lead Systems Engineer</b> &mdash; takes and refines the '
                'generated code',
                '<b>Go-To-Market Specialist</b> &mdash; strategy, marketing, '
                'financial feasibility',
                '<b>Creative Director</b> &mdash; visual design and the pitch '
                'deck',
                'Submitted as one launch package: a working prototype, a '
                'one-page business summary, and the slide deck'],
         tool='Google Gemini, HTML/JavaScript or Python',
         links=[
             ('Google Gemini', 'https://gemini.google.com/',
              'Where the code, the business plan and the pitch '
              'material get generated.')],
         path='software',
         note='The prototype only has to work at a basic level. The grade is '
              'in the thinking and the pitch, not the syntax.'),

    dict(t='eoy', w='Capstone', title='Grade 11 Capstone', kind='project',
         hook='Two projects at once: one that proves engineering logic, one '
              'that sells a professional vision.',
         body=['The capstone asks you to show what you understand about civil '
               'engineering and architecture by running two distinct projects '
               'simultaneously.',
               '<b>Project 1 &mdash; a unique concept.</b> Develop an original '
               'structure that stretches traditional design &mdash; an '
               'upside-down building, an integrated vertical ecosystem &mdash; '
               'and then prove it is physically and logically viable. Look at '
               'your own design through an engineer’s eyes and justify '
               'why it works.'],
         gives=['<b>Engineering Logic Report</b> &mdash; documented research '
                'on similar structures or the scientific principles that '
                'support your concept',
                '<b>Structural Analysis</b> &mdash; simulation and test '
                'methods, in Fusion 360 or equivalent',
                'The presentation package for the second project &mdash; '
                'the design as a firm would present it to a client',
                'A weekly journal across all four weeks'],
         tool='Fusion 360, Revit', path='architecture',
         note='Runs over four weeks: conceptual design, detailed design, then '
              'two weeks of proof.'),

    dict(t='eoy', w='Final', title='Reflection Portfolio Presentation',
         kind='reflection',
         hook='Your whole year, compiled into one presentation.',
         body=['Compile your assignments from the year into a single Google '
               'Slides presentation. Take screenshots from the assignments and '
               'your daily journals, and put them next to a reflection on what '
               'you got out of them.',
               'You are not expected to reflect on every single assignment. '
               'Pick several for real depth, or group them &mdash; all the Do '
               'Nows together, say &mdash; and reflect on the group. Finish '
               'with a reflection on the whole year.'],
         gives=['One professional, clean, templated deck',
                'Last year’s presentation, found and uploaded alongside '
                'it'],
         tool='Google Slides', path='',
         note='"Go back and find last year’s presentation" is only a '
              'reasonable instruction if last year’s work is still '
              'somewhere you can find it. Keep your portfolio where you can '
              'get at it.'),

    dict(t='eoy', w='Final', title='Gmetrix', kind='admin',
         hook='Certification practice, ahead of the real exam.',
         body=['Create an account and join the class. The join code is in '
               'Classroom.'],
         gives=[], tool='Gmetrix', path='', note=''),

    dict(t='always', w='All year', title='Independent Study Project',
         kind='project',
         hook='A year-long project in whatever part of engineering actually '
              'interests you.',
         body=['This is the one you run at your own pace, treated like a '
               'personal engineering hobby. It breaks into three areas, which '
               'can all serve one big idea or stay completely separate.',
               '<b>Research</b> &mdash; a deep dive into a concept, theory or '
               'process that sparks your curiosity, using reputable sources, '
               'ending in its real-world applications.',
               '<b>Design</b> &mdash; a new product or solution, standalone or '
               'part of something bigger. An ergonomic desk organiser, a '
               'custom phone case.',
               '<b>Development</b> &mdash; take something that already exists '
               'and fix, modify or improve it.'],
         gives=['A weekly journal &mdash; findings, learnings, problems. '
                'Sketches, notes and video logs all count',
                'Mid-year and end-of-year reflections for each project'],
         tool='', path='',
         note='If you have no idea yet, build a skill tree in these areas so '
              'you are ready when an idea does strike. That is exactly what '
              'the seven pathway guides are for.'),
]


# --------------------------------------------------------------- grade twelve

G12 = [
    dict(t=1, w='Wk 1', title='Design a Laptop', kind='project',
         hook='A laptop, designed from the outside in.',
         body=['The opening project of senior year. The brief lives in '
               'Classroom.'],
         gives=[], tool='Fusion 360', path='industrial',
         note='The school-wide safety test, the shop safety test and the '
              'acknowledgement form are all in this same week.'),

    dict(t=1, w='Wk 2&ndash;5', title='Shop Equipment Project', kind='project',
         hook='Four weeks, four separate projects, each built on a different '
              'piece of shop equipment.',
         body=['You pick from the equipment available &mdash; engraver, VEX, '
               'Shaper Origin and power tools, Arduinos, 3D printers &mdash; '
               'and build something with it. Each week stands alone; you are '
               'not continuing the previous project.',
               'Some weeks you will need to pair equipment together. The '
               'Shaper Origin can make a wooden base for an Arduino project, '
               'for instance.'],
         gives=['A <b>Potential Ideas</b> document up front, weighing ideas '
                'for each piece of equipment',
                'The <b>Weekly Planner</b>, Monday morning',
                'The <b>Project Reflection</b>, Friday',
                'The <b>Engineering Daily Journal</b>, every day',
                'The finished project itself, documented'],
         tool='Engraver, VEX, Shaper Origin, Arduino, 3D printers',
         path='mechanical', note=''),

    dict(t=1, w='Wk 2', title='Festo MecLabs: Exploring Mechatronics',
         kind='course',
         hook='The Festo mechatronics course, on the licensed platform.',
         body=['Runs on Festo LX, which the shop pays for. See the training '
               'page for how to get in.'],
         gives=[], tool='Festo LX, MecLabs', path='automation', note=''),

    dict(t=1, w='Wk 2', title='Reverse Engineering: Breadboard Circuit '
                              'Practice', kind='skills',
         hook='Take a circuit apart to understand it, then rebuild it.',
         body=['Paired with its own reflection.'],
         gives=[], tool='Breadboard, components', path='electrical', note=''),

    dict(t=1, w='Wk 5', title='Post-Lecture Reflection: Theory of the Week',
         kind='reflection',
         hook='A written reflection on the week’s theory lecture.',
         body=[], gives=[], tool='', path='', note=''),

    dict(t=2, w='Wk 1', title='Industrial Design Challenge: The LED Desk Lamp',
         kind='project',
         hook='A desk lamp, judged as an industrial design object rather than '
              'a mechanism.',
         body=['The brief lives in Classroom.'],
         gives=[], tool='Fusion 360, 3D printing', path='industrial', note=''),

    dict(t=2, w='Wk 2', title='Holiday Collaborative Rube Goldberg Machine',
         kind='project',
         hook='The whole class building one absurd chain reaction that has to '
              'work end to end.',
         body=['The second annual. Every section has to hand off to the next '
               'one, which makes it a genuine interface problem as much as a '
               'mechanism problem.'],
         gives=[], tool='', path='mechanical', note=''),

    dict(t=2, w='Wk 2', title='Skills Revisited: AutoCAD Drawings and Title '
                              'Blocks', kind='skills',
         hook='Back to the drawing set, at senior standard.',
         body=['The CAD file library has the shop’s Architectural and '
               'Mechanical AutoCAD templates &mdash; use those title blocks '
               'rather than making your own.'],
         gives=[], tool='AutoCAD', path='architecture', note=''),

    dict(t=2, w='Wk 2', title='Research &amp; Analysis: LTT Screwdriver',
         kind='skills',
         hook='Pull apart the design decisions in one deliberately '
              'over-engineered consumer tool.',
         body=[], gives=[], tool='', path='industrial', note=''),

    dict(t=2, w='Wk 2', title='Try Again! Moon Base 2.0', kind='project',
         hook='A second run at the moon base, knowing what went wrong the '
              'first time.',
         body=[], gives=[], tool='', path='architecture', note=''),

    dict(t=2, w='Wk 3', title='Intro to CorelDraw', kind='skills',
         hook='A day of teaching yourself CorelDraw, with something to show '
              'for it.',
         body=['Paired with a Do Now that has you design the shop logo in it.'],
         gives=[], tool='CorelDraw, laser engraver', path='industrial',
         note=''),

    dict(t=2, w='Wk 3', title='VEX Robotics', kind='project',
         hook='VEX build and programming, day two onward.',
         body=[], gives=[], tool='VEX V5', path='automation', note=''),

    dict(t=2, w='Wk 4', title='Holiday Ornament', kind='project',
         hook='A short, sharp design-and-make with a hard deadline.',
         body=[], gives=[], tool='3D printing, laser engraver', path='',
         note=''),

    dict(t=2, w='Wk 5', title='Mars Colony Design', kind='project',
         hook='A colony designed for somewhere the environment is trying to '
              'kill you.',
         body=[], gives=[], tool='Fusion 360, Autodesk Forma',
         links=[
             ('Google Gemini', 'https://gemini.google.com/',
              'Where the code, the business plan and the pitch material get '
              'generated.')],
         path='architecture', note=''),

    dict(t=2, w='Wk 5', title='Bunker House Design', kind='project',
         hook='A house built for a hostile environment, on Earth this time.',
         body=[], gives=[], tool='Fusion 360', path='architecture', note=''),

    dict(t=3, w='Term 2 Wk 5 &rarr; Term 4', title='Senior Capstone',
         kind='project',
         hook='One open-ended project, chosen by you and run by you, from the '
              'end of Term 2 to the final defence.',
         body=['Research, design and development of an original solution that '
               'shows what you learned in four years here. It does not fit '
               'inside a term, so it is not filed under one.',
               '<b>Choosing it.</b> At the end of Term 2 you develop initial '
               'planning and concepts for <b>three different</b> potential '
               'ideas &mdash; or three different approaches to the same idea '
               'if you already have a strong one.',
               '<b>Running it.</b> The weekly documents are not paperwork '
               'around the project; they are the evidence your final defence '
               'is built from.',
               '<b>Defending it.</b> The Term 4 presentation is not show and '
               'tell. You prove the why with patent and market research, the '
               'how with your technical tools, and the proof with raw test '
               'data and the redesigns your failures forced.'],
         gives=['Three initial project concepts, before the work starts',
                '<b>Design brief</b>, kept current',
                '<b>Daily journal</b>, every session',
                '<b>Weekly planner</b> on Mondays, <b>weekly reflection</b> '
                'on Fridays',
                '<b>Meeting notes</b> after every instructor meeting',
                '<b>Research log</b> &mdash; aim for one new source a day',
                '<b>Order request forms</b> for materials and parts',
                'The functional prototype',
                'The final slide deck, with high-resolution as-built photos'],
         tool='', path='',
         note='Stratasys Academy online learning, KeyShot and Fusion&rsquo;s '
              'Texture Extrude land in capstone week 5 &mdash; the resin '
              'printing and rendering skills, right when projects need them.'),

    dict(t='always', w='All year', title='Independent Study', kind='project',
         hook='The parallel track: your own project in research, design '
              'and/or development, running alongside everything else.',
         body=['It feeds directly into the capstone concept, so what you '
               'choose here matters more than it looks.',
               'The Term 1 reflection is where you stop, assess your progress '
               'and set your strategy for the rest of the year. Plans '
               'evolving is normal &mdash; the purpose is growth and '
               'exploration, not sticking to a proposal you have outgrown.'],
         gives=['A design proposal for each project',
                'The Term 1 reflection, on the Research, Design and '
                'Development reflection documents',
                'End-of-year reflections'],
         tool='', path='', note=''),

    dict(t='always', w='All year', title='Platform training', kind='course',
         hook='Three external courses that unlock equipment and go on your '
              'record.',
         body=['<b>VEX AIM Bot</b> &mdash; the AIM Intro Course STEM Lab, in '
               'teams.',
               '<b>Universal Robots e-Learning</b> &mdash; the e-Series Core '
               'Track first, then the Pro and Application Tracks, finishing '
               'with a unique program of your own on one of the two URbots.',
               '<b>Bambu Lab Academy</b> &mdash; the 3D printer certification '
               'ladder. Beginner lets you print with an instructor, '
               'Intermediate with an approved peer, Advanced on your own. '
               'Machines unlock in order: A1 Mini, then X1C, then H2D.'],
         gives=['The VEX AIM STEM Lab, completed as a team',
                'A Universal Robots progress document, and one unique URbot '
                'program',
                'Your Bambu Lab certifications, at whatever level you reach'],
         tool='', path='automation',
         note='Every print job still needs instructor approval at every '
              'level. Advanced means you may run the machine alone, not that '
              'you may print whatever you like.'),
]


TERMS = [
    (1, 'Term 1'), (2, 'Term 2'), (3, 'Term 3'), (4, 'Term 4'),
    ('eoy', 'End of year'), ('always', 'Running all year'),
]

WORK = {'11': G11, '12': G12}
