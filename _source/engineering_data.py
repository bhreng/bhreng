# -*- coding: utf-8 -*-
"""What engineering is, and the design process the shop actually uses.

This page exists because the phrase "the BHR Engineering Design Process" was
used nine times across the site and defined nowhere. A brief that says "use the
design process" is not an instruction unless the process is written down.

SOURCES, all from Dan's own material -- nothing here is generic textbook
content invented to fill a page:

  * The eight steps are quoted from the Grade 10 "Research & Analysis: The LTT
    Screwdriver" assignment, which asks students to walk a real product through
    each one.
  * The seven roles are from the Grade 11 "Roles of an Engineer" assignment and
    the Full Scope Project that follows it, including the deliverable each role
    is expected to produce.
  * The engineering-management tasks are from the same LTT Screwdriver brief.
"""

# --------------------------------------------------------- the design process

STEPS = [
    ('Identify the problem',
     'Say what is actually wrong, in one sentence, before you touch anything. '
     'Most bad projects are answers to a question nobody asked.',
     'A problem statement you could hand to a stranger.'),
    ('Research and brainstorm',
     'Find out who has solved this before and how. Then generate more ideas '
     'than you need, including the ones you think are stupid.',
     'Sources you actually read, and a spread of concepts &mdash; not one.'),
    ('Develop solutions',
     'Take the ideas seriously enough to draw them. Sketches, not paragraphs.',
     'At least two distinct concepts, far enough along to compare.'),
    ('Plan a solution',
     'Choose one and justify the choice against real criteria &mdash; cost, '
     'time, whether the shop can actually make it. This is where a decision '
     'matrix earns its keep.',
     'A chosen concept, and the reason it beat the others.'),
    ('Create',
     'Model it, then make it. The model is not the deliverable; the model is '
     'how you find out what you got wrong before you spend material.',
     'A CAD model, and a prototype you can hold.'),
    ('Test and evaluate',
     'Measure it against what you predicted. This is the step students skip, '
     'and it is the one that separates engineering from craft.',
     'Data. Numbers you took yourself, next to the numbers you expected.'),
    ('Improve and redesign',
     'Change the thing based on what the test told you, and record what you '
     'changed and why. A project with no second version has not been tested '
     'hard enough.',
     'A documented iteration &mdash; version two, and the reason for it.'),
    ('Present your solution',
     'Explain it to someone who was not there. If they cannot follow it, the '
     'work is not finished.',
     'A presentation, a drawing set, or both.'),
]

# ------------------------------------------------------------- the seven roles

ROLES = [
    ('Design Engineer',
     'Works out what the thing is and what it looks like, in enough detail '
     'that it could be built.',
     'A detailed design &mdash; a drawing set or a CAD model.'),
    ('Research Engineer',
     'Finds out what is already known, and predicts what would happen if you '
     'tried something new.',
     'Research and a prediction &mdash; a new use for an existing item, or a '
     'new way to do a task.'),
    ('Development Engineer',
     'Turns a design into something physical, and finds out where it fails.',
     'A model or a prototype.'),
    ('Production &amp; Construction Engineer',
     'Works out how it gets made, in what order, by whom, and by when.',
     'A work breakdown structure and a Gantt chart.'),
    ('Operations Engineer',
     'Thinks past the single object to the system that runs it.',
     'A large-scale system design, with operational notes.'),
    ('Sales Engineer',
     'Explains the engineering to people who are not engineers, convincingly '
     'and without lying about it.',
     'A marketing piece &mdash; an ad, a commercial, a brochure &mdash; that '
     'sells the engineering behind the product.'),
    ('Management Engineer',
     'Decides who does what, and carries the schedule.',
     'A team with tasks assigned to each person.'),
]

# --------------------------------------------------- what the job actually is

WHAT = [
    ('Engineering is not one job',
     'It is at least seven, and they suit very different people. Someone '
     'designs the part. Someone works out whether it will hold. Someone '
     'writes the code that moves it. Someone gets it manufactured. Someone '
     'carries the schedule so it ships. All of that is engineering.'),
    ('Engineering <em>technology</em> is the applied half',
     'An engineer is often asked to derive the theory. An engineering '
     'technologist is asked to make the thing work &mdash; the CAD, the '
     'drawings, the prototype, the test, the fix. Both are real careers. This '
     'shop teaches the second one, and it opens the door to the first.'),
    ('It is a trade and a degree path at the same time',
     'People leave here and go straight into work with certifications '
     'employers recognise. People also leave here and go to engineering '
     'school with four years of CAD, documentation and project work behind '
     'them. Neither route is the fallback.'),
    ('The work is making things that have to actually work',
     'Not models of things. A part that comes off the printer and fits. A '
     'circuit that does what you said it would. A drawing someone else can '
     'build from without asking you a single question.'),
    ('Testing tells you what to change next',
     'Every project here ends in testing, and testing is where the measured result meets the one you predicted. The gap between them is the useful part &mdash; it is what tells you which change to make. Engineers who get good are the ones who write that gap down and act on it.'),
    ('Documentation is not the paperwork after the work',
     'It is the evidence that the work was yours. Edison left roughly five '
     'million pages of notes. In 1943 the Supreme Court struck down '
     'Marconi&rsquo;s key radio claims because Tesla&rsquo;s earlier '
     'documented work came first. Your logbook is the same instrument, '
     'smaller.'),
]

# -------------------------------------------------- management, as a discipline

MANAGEMENT = [
    ('Design brief', 'What is being made, for whom, and against what limits.'),
    ('Work breakdown structure', 'The job, split until each piece is a task '
     'somebody could actually pick up.'),
    ('Timeline / Gantt chart', 'The order those tasks have to happen in, and '
     'what is waiting on what.'),
    ('Team members and roles', 'Who owns which piece. Ambiguity here is how '
     'group projects fail.'),
    ('Sub-contractors and suppliers', 'Who else you depend on, and what they '
     'owe you.'),
    ('Part list and costs', 'Every component, quantity, material and price. '
     'The document that turns a design into a decision.'),
]
