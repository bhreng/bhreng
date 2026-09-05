#!/usr/bin/env python3
"""Builds the seven E.E.P. pathway hub guides as one HTML artifact."""

import shop_projects as SP   # briefs the shop has really run, per pathway

# ---------------------------------------------------------------- content
# Each pathway: key, short nav label, standard, full title, lead, one-line
# pitch, then the five topics.

P = []

P.append(dict(
    key='industrial', nav='Industrial Design', std='S8',
    title='Industrial Design',
    lead='Mr. Frank',
    tag='How a thing looks, feels in the hand, and can actually be made.',
    intro="You take an idea that only exists as a sketch and turn it into an object "
          "somebody would pick up and use. That means caring about the shape and the "
          "feel of it, and caring just as much about whether a machine in this building "
          "can produce it.",
    field=dict(
        blurb="Industrial designers sit between the people who want a product and the "
              "machines that make it. The job is to make something that works, that "
              "people want to hold, and that can be manufactured without costing a fortune.",
        roles=[('Product designer', 'Shapes the object around the person using it — size, grip, weight, how obvious it is to operate.'),
               ('Manufacturing engineer', 'Works out how to actually produce it, at what cost, at what rate, with what waste.'),
               ('Technical drafter', 'Produces the drawings a shop builds from, using GD&amp;T so there is no room to guess.'),
               ('Research engineer', 'Digs into materials and geometry to find out what is possible before anyone commits.'),
               ('Development engineer', 'Carries a concept through prototypes into something that can be produced.')],
        note="Your Career Vision Summary asks for working conditions, education, and pay. "
             "Look up current figures yourself — the Bureau of Labor Statistics "
             "Occupational Outlook Handbook is the source to use, and it is regional."),
    learn=dict(
        blurb="Two ideas run through everything in this pathway: design decisions have to "
              "be justified by physics, and geometry has to be designed for the process "
              "that will produce it.",
        items=[('Engineering accounting',
                'From Holtzapple &amp; Reece, <em>Foundations of Engineering</em>. Treats mass, energy and '
                'momentum like a ledger: input minus output plus generation minus consumption equals '
                'accumulation. It is how you check that a design is physically possible before you build it.'),
               ('Design for manufacturing',
                'Additive geometry for 3D printing — overhangs, wall thickness, orientation. Subtractive '
                'geometry for laser and CNC — tool access, kerf, fixturing. The same part is drawn '
                'differently depending on how it will be made.'),
               ('User-centered design',
                'Ergonomics and human factors. Form follows function, but function includes "a person '
                'can figure this out without instructions."'),
               ('Visual communication',
                'Drafting standards that let a drawing say exactly one thing. Wallach, <em>Modern Drafting</em>, '
                'for descriptive geometry and ASME conventions; Madsen, <em>Engineering Drawing and Design</em>, '
                'for visualization and CAD practice.')]),
    skills=dict(
        cred='Autodesk Certified User — Fusion 360',
        blurb="Fusion 360 is the core tool here. You need both modeling styles, not just one.",
        items=['Parametric modeling — history-driven, so changing one dimension updates everything downstream.',
               'Direct modeling — for fast iteration when you are still deciding what the thing is.',
               'Rendering, animation and exploded views, so someone who has never seen the part understands it.',
               'GD&amp;T on drawings — tolerances that say what actually matters on the part.',
               '3D scanners for reverse engineering an existing object.',
               '3D printers — additive protocols, material choice, print orientation.',
               'Laser engravers and CNC — subtractive setup and safety.']),
    build=dict(
        blurb="Start from one of these or bring your own. Every one of them runs the same "
              "loop: identify and research, sketch and mass out, model and prototype, test "
              "and redesign.",
        items=[('Desk organizer', 'Constrained, fast, and unforgiving about ergonomics. Everyone thinks it is easy until they hold the first print.'),
               ('Kids toy', 'Adds safety constraints, durability and a user who cannot read instructions.'),
               ('Reverse-engineer and improve', 'Scan or measure an existing product, rebuild it in CAD, then change one thing and prove the change is better.'),
               ('Before-and-after case study', 'Take something badly designed and redesign it. The deliverable is the visual story — renders and photographs that make the improvement obvious without a paragraph of explanation.')]),
    files=['Logbook template — three intervals, daily.',
           'Bill of Materials worksheet — every part, material, quantity, unit cost.',
           '&ldquo;Do Now!&rdquo; reflection.',
           'E.E.P. term-end reflection.',
           'Makerspace safety rules.',
           'Design brief template.'],
))

P.append(dict(
    key='architecture', nav='Architecture &amp; Civil', std='S10',
    title='Architecture and Civil Engineering',
    lead='Mr. Frank',
    tag='Buildings, sites, and the loads that hold them up.',
    intro="Everything in this pathway has to stand up, drain, and be legal. You work at a "
          "scale where a mistake is expensive and permanent, which is why the documentation "
          "in this pathway is the most demanding in the program.",
    field=dict(
        blurb="Architecture and civil engineering cover the built environment — how a "
              "structure carries load, how a site handles water and traffic, and how the "
              "whole thing gets documented so a contractor can build it.",
        roles=[('Structural engineer', 'Proves the building will not fall down, and shows the math.'),
               ('Architectural designer', 'Resolves how a space is used into a form that can be built.'),
               ('Civil / site engineer', 'Grading, drainage, circulation, and how the site meets the road.'),
               ('BIM coordinator', 'Keeps the model coordinated across disciplines and catches clashes before they reach the field.'),
               ('Construction manager', 'Runs the build — sequence, safety, and compliance on site.')],
        note="Ask Mr. Dryer instead when your building gets smart — automated facades, "
             "sensors, controlled systems. The structure is here; the intelligence is over there."),
    learn=dict(
        blurb="You are learning to see a building as a set of forces travelling to the ground.",
        items=[('Structural systems',
                'Steel frames, concrete frames, and foundations. Model forces, moments and stability in '
                'MD Solids or equivalent. Trace how gravity load moves from the roof to the earth.'),
               ('Material behavior',
                'Steel, concrete and timber under load. Moment of inertia calculations to evaluate '
                'resistance to bending; stress-strain diagrams to predict what a material does before '
                'it fails.'),
               ('Sustainable and regenerative design',
                'Sustainable design reduces harm — energy efficiency, less waste. Regenerative design '
                'goes further and tries to leave the site and community better than it found them. '
                'Know which one you are claiming.'),
               ('Drafting standards',
                'Madsen, <em>Engineering Drawing and Design</em>, is the reference for this pathway — '
                'ANSI/ASME standards, visualization, and descriptive geometry.')]),
    skills=dict(
        cred='Autodesk Certified User — Revit Architecture',
        blurb="Revit for the building, Fusion 360 for the components you fabricate.",
        items=['Coordinated 3D modeling — walls, floors, roofs that update together.',
               'Clash detection — finding where the ductwork runs through a beam before anyone builds it.',
               'Schedules and interoperability — door and window schedules, IFC and DWG export.',
               'Sheet sets — title blocks, section cuts, a construction document set someone could build from.',
               'Total station — angle and distance measurement.',
               'Levels — elevation and grading.',
               'GPS — site mapping.']),
    build=dict(
        blurb="Two briefs, both of which end in a pitch to people who are not engineers.",
        items=[('The unique structure', 'Design an original structure with a gravity-defying or unusual structural element — then prove it works, with MD Solids simulation or physical load testing. The proof is the assignment; the shape is the easy part.'),
               ('The revitalization pitch', 'Pick a real existing building and bring it back. Branding, usability, aesthetics, and a before-and-after that convinces a town board.'),
               ('Site design set', 'A complete professional site plan: soil testing results, cut and fill volume calculations, engineered drainage, parking, roads, and ADA circulation.')]),
    files=['Logbook template.',
           'Site design checklist — soil, cut and fill, drainage, circulation.',
           'Bill of Materials worksheet.',
           'Sheet set title block template.',
           '&ldquo;Do Now!&rdquo; reflection and E.E.P. term-end reflection.',
           'Makerspace safety rules.'],
))

P.append(dict(
    key='mechanical', nav='Mechanical', std='S7',
    title='Mechanical Engineering',
    lead='Mr. Frank',
    tag='Forces, motion, materials, and whether the part survives.',
    intro="This is the pathway where you predict what will happen and then find out whether "
          "you were right. Calculate the load, simulate it, print it, break it, and account "
          "for the difference between the three numbers.",
    field=dict(
        blurb="Mechanical engineering is the physics of things that move and things that "
              "carry load. It is the broadest of the pathways and it underlies most of the "
              "others.",
        roles=[('Design engineer', 'Turns a requirement into a mechanism, with the calculations to back it.'),
               ('Test engineer', 'Designs the experiment that proves whether the design works, and measures honestly.'),
               ('Materials engineer', 'Selects material for the job and predicts how it behaves over its life.'),
               ('Manufacturing engineer', 'Gets it built at quality and at rate.'),
               ('Simulation / FEA analyst', 'Predicts failure on a computer so it does not happen in the field.')]),
    learn=dict(
        blurb="Nothing here is optional background. Every one of these shows up in a project.",
        items=[('Engineering accounting',
                'Holtzapple &amp; Reece, <em>Foundations of Engineering</em>. Input &minus; output + generation '
                '&minus; consumption = accumulation. Mass, energy and momentum all balance, and if your '
                'design does not balance, it does not work.'),
               ('Newton, applied',
                'Inertia is the basis of statics and structural equilibrium. F&nbsp;=&nbsp;ma predicts '
                'velocity and displacement in moving assemblies. Action and reaction resolves forces in '
                'joints, fasteners and supports.'),
               ('Statics and kinematics',
                'Vector resolution into x, y and z components. Free body diagrams. Kinematic equations for '
                'displacement, velocity and acceleration. Stress and strain analysis for internal forces '
                'and deformation.'),
               ('FEA, and what it is doing',
                'The manual vector calculations you do by hand are the same mathematics the solver runs at '
                'every mesh node. Understand the hand method first — otherwise a wrong simulation looks '
                'exactly like a right one.'),
               ('Materials and reliability',
                'Classify materials — organics, metals, polymers, ceramics, composites — and connect '
                'micro-structure to performance. Mean time between failure as a way to think about '
                'design life rather than a single test.')]),
    skills=dict(
        cred='Autodesk Certified User — Inventor',
        blurb="Inventor for parametric assemblies, Fusion 360 for simulation and fabrication. "
              "Everything in this shop is Autodesk.",
        items=['Parametric modeling — sketches, constraints, dimensions, extrusions.',
               'History-driven assemblies where changing a driving dimension updates the whole model.',
               'Assembly management and GD&amp;T on technical drawings.',
               'FEA setup — loads, constraints, mesh, and reading the result critically.',
               'Calipers and micrometers for precision measurement.',
               'Multimeters and oscilloscopes where a mechanism has electronics in it.',
               'Calibration — every instrument checked against a known standard before it produces data you will rely on.']),
    build=dict(
        blurb="All three of these are about the gap between prediction and reality.",
        items=[('Parametric optimization', 'Build a smart assembly where changing one driving dimension correctly updates every related component without breaking design intent. Harder than it sounds, and the failures are instructive.'),
               ('Simulate, print, break', 'Design a bracket. Use FEA to predict where and at what load it fails. 3D print it, test it to destruction, and account for the difference between the two numbers. The analysis of the gap is the deliverable.'),
               ('Three simple machines', 'Design a system integrating at least three simple machines — gears, pulleys, levers. Calculate the mechanical advantage as output force over input force, then measure it and explain the loss.')]),
    files=['Logbook template.',
           'FEA report template.',
           'Test data log.',
           'Bill of Materials worksheet.',
           'Decision matrix template.',
           '&ldquo;Do Now!&rdquo; reflection and E.E.P. term-end reflection.',
           'Makerspace safety rules.'],
))

P.append(dict(
    key='electrical', nav='Electrical', std='S5',
    title='Electrical Engineering',
    lead='Mr. Dryer',
    tag='Circuits, power, and measuring what you cannot see.',
    intro="You cannot look at a circuit and tell whether it is working. Everything in this "
          "pathway depends on measuring properly and trusting the instrument — which means "
          "knowing how to calibrate it.",
    field=dict(
        blurb="Electrical engineering is the design and troubleshooting of the systems that "
              "move power and signal. It sits underneath robotics, software and anything "
              "with a sensor in it.",
        roles=[('Electrical engineer', 'Designs power distribution and hardware architecture.'),
               ('Robotics engineer', 'Puts intelligence and motion into a system that has to act on the world.'),
               ('Systems integrator', 'Makes components from different disciplines work as one unit.'),
               ('Test technician', 'Finds the fault, with instruments, methodically, instead of by swapping parts.')]),
    learn=dict(
        blurb="Circuit theory is small in volume and unforgiving in application.",
        items=[('What materials do',
                'Atomic structure and why it governs electrical behavior. Conductors let charge move, '
                'insulators contain it, semiconductors do either depending on conditions — which is what '
                'makes solid-state electronics possible.'),
               ('The four parts of any circuit',
                'Source provides energy — a battery, a PV cell. Load consumes it — a motor, a resistor. '
                'Control regulates flow — a switch, a transistor. Conductors carry it — trace or wire. '
                'Every circuit you will ever draw is those four things.'),
               ('Ohm and Kirchhoff',
                'V&nbsp;=&nbsp;IR for the relationship between voltage, current and resistance. '
                'Kirchhoff&rsquo;s current law for junctions and voltage law for loops, which is how you '
                'analyze anything more complicated than one path.'),
               ('Series, parallel, and both',
                'Series: one path, resistances add. Parallel: multiple paths, voltage constant across '
                'branches. Series-parallel: what real systems actually look like.'),
               ('AC and DC',
                'Direct current for microcontrollers and logic. Alternating current for power distribution. '
                'Know which one you are working with before you connect anything.'),
               ('Reference',
                'Tokheim, <em>Digital Electronics</em>, for logic design, integrated circuits and systematic '
                'troubleshooting. Khan Academy and Brilliant for the supporting mathematics.')]),
    skills=dict(
        cred='Multimeter and oscilloscope proficiency',
        blurb="This pathway&rsquo;s credential is demonstrated instrument skill rather than "
              "a software certificate. It is assessed by whether your measurements can be trusted.",
        items=['Multimeter — voltage, current, resistance, capacitance, and continuity.',
               'Oscilloscope — drawing and interpreting square, sawtooth and sine waveforms; determining time, fall time, frequency and amplitude.',
               'Calibration and self-test before any measurement you will report.',
               'Resistor color codes — reading value and tolerance without an instrument.',
               'Breadboarding: read the schematic, place components observing polarity on diodes and electrolytics, connect source, control and load with the right gauge, verify continuity and node voltage before full power-on.',
               'Arduino for firmware and digital logic.',
               'Festo LX for industrial automation and mechatronics tasks.']),
    build=dict(
        blurb="Both of these end with data, not with a working demo.",
        items=[('Sensor and actuator integration', 'Build a system that senses something in the environment and produces a mechanical response. The engineering is in the threshold and the timing, not the wiring.'),
               ('Diagnostic challenge', 'Take a system with a fault in it and find the fault methodically — measurement, not part-swapping. Document the sequence of measurements that isolated it.'),
               ('Renewable energy analysis', 'Evaluate conversion efficiency and integration for a solar or wind setup. Measure real output against rated output and explain the difference.')]),
    files=['Logbook template.',
           'Schematic template.',
           'As-built drawing set — the final state of the system, not the plan.',
           'Test and measurement log.',
           '&ldquo;Do Now!&rdquo; reflection and E.E.P. term-end reflection.',
           'Electrical safety rules — GFCI use, lockout/tagout, reporting frayed wiring.'],
))

P.append(dict(
    key='software', nav='Software', std='S6',
    title='Software Engineering',
    lead='Mr. Dryer',
    tag='Logic, code, and making a machine decide something.',
    intro="Code in this shop is not an end in itself — it controls something physical, and "
          "physical things have voltage and torque and consequences. You write logic, then "
          "you prove on an oscilloscope that the logic is doing what you think.",
    field=dict(
        blurb="Software engineering here is about the intelligence layer: the logic that "
              "makes a system respond, decide, and report.",
        roles=[('Software engineer', 'Designs the architecture of an application — how the pieces are organized and talk to each other.'),
               ('Computer engineer', 'Works where hardware and firmware meet.'),
               ('Robotics engineer', 'Writes control algorithms for autonomous motion.'),
               ('Systems integrator', 'Connects digital and mechanical subsystems into one working whole.'),
               ('Controls programmer', 'Programs the PLCs that run industrial equipment.')]),
    learn=dict(
        blurb="Logic first, syntax second. Every one of these is testable on paper before "
              "you touch a keyboard.",
        items=[('Boolean algebra',
                'Build expressions and verify them with truth tables. This is how you check a circuit or '
                'a conditional is correct rather than hoping.'),
               ('Logic simplification',
                'De Morgan&rsquo;s theorem and simplification to reduce an expression to its minimum form. '
                'Fewer gates, fewer branches, faster response.'),
               ('Flowcharting',
                'Map the logic before writing syntax. A flowchart catches the error that would otherwise '
                'take an hour of debugging to find.'),
               ('Number systems',
                'Binary, decimal and hexadecimal conversion, and why hex is how memory gets discussed.'),
               ('Reference',
                'Brilliant for logic and computer science reasoning; Khan Academy for the supporting math.')]),
    skills=dict(
        cred='Demonstrated proficiency in Python, Arduino C, and PLC ladder logic',
        blurb="Three environments, because the job moves between them.",
        items=['Python — algorithmic logic and data analysis with NumPy and Pandas; setting up an environment and managing dependencies.',
               'Arduino — firmware in C, I2C and SPI sensor communication, serial monitor debugging.',
               'PLC ladder logic through Festo LX — industrial control and computer integrated manufacturing.',
               'Pulse width modulation to control hardware torque and speed.',
               'Sensor calibration — a reading is worthless until the sensor is calibrated.',
               'Step-through debugging rather than guessing at a fix.',
               'Oscilloscope for signal timing and frequency analysis — how you verify PWM is actually doing what your code says.']),
    build=dict(
        blurb="Pick one and document the optimization, not just the working version.",
        items=[('Robotic arm control', 'Program an arm with an end effector to solve a real materials-handling problem. The constraint is the work envelope and the gripper, not the code.'),
               ('Automated feed system', 'Sensors plus decision logic managing autonomous material flow. Decide what happens when the sensor is ambiguous — that case is the whole assignment.'),
               ('Data analyzer', 'Build something in Python that inspects and evaluates system parameters and recommends a change based on the data.')],
        extra="Every project needs a before-and-after on your own code: show a logic "
              "simplification or algorithmic change, and give the measured improvement in "
              "response time. &ldquo;It felt faster&rdquo; is not a result."),
    files=['Logbook template.',
           'Iterative prototype log — versions, what changed, what it measured.',
           'Flowchart and truth table templates.',
           'Code comment and documentation standard.',
           '&ldquo;Do Now!&rdquo; reflection and E.E.P. term-end reflection.',
           'Electrical and machine safety rules — power down and unplug before cleaning or repairing.'],
))

P.append(dict(
    key='automation', nav='Automation &amp; Robotics', std='S9',
    title='Automation and Robotics',
    lead='Mr. Frank and Mr. Dryer',
    tag='Where the mechanical, the electrical and the code have to work as one system.',
    intro="This is the pathway that pulls the others together. A robot is a mechanism that "
          "has to be built, a circuit that has to be powered and sensed, and a program that "
          "has to decide — and it fails at whichever of the three you neglected. It is the "
          "only pathway with two instructors, because it genuinely needs both.",
    field=dict(
        blurb="Automation and robotics is mechatronics and computer integrated "
              "manufacturing: physical systems that sense, decide and act without a person "
              "driving them moment to moment.",
        roles=[('Robotics engineer', 'Designs the whole system — mechanism, sensing, control — and owns the integration.'),
               ('Controls engineer', 'Programs and tunes the PLCs and controllers that run production equipment.'),
               ('Automation technician', 'Installs, commissions and troubleshoots automated cells on a live floor.'),
               ('Mechatronics engineer', 'Works deliberately across mechanical, electrical and software rather than specializing in one.'),
               ('CIM specialist', 'Coordinates CNC equipment, robots and material handling into one production system.')],
        note="Ask Mr. Frank for the physical side — chassis, drive systems, work envelope, "
             "manufacturability of the parts. Ask Mr. Dryer for the intelligence — control "
             "code, circuit troubleshooting, validation of the control loop."),
    learn=dict(
        blurb="This pathway draws on four standards at once, which is the point of it. "
              "You need enough of each to make the system work.",
        items=[('From electrical (S5)',
                'Analog circuit requirements, power distribution, and how sensors are wired and powered. '
                'A robot that browns out under load is an electrical problem, not a code problem.'),
               ('From digital and software (S6)',
                'Boolean design, logic frameworks, and PLC programming. This is where the system&rsquo;s '
                'decisions live.'),
               ('From mechanical (S7)',
                'Drive system design and assembly, kinematics of the work envelope, and fabricating a '
                'chassis that stays rigid. Backlash and flex show up as control problems and get blamed '
                'on the code.'),
               ('Automated systems (S9) &mdash; the anchor',
                'CIM system components, robotic controllers, end-of-arm tooling, and the working '
                'relationship between CNC equipment and robotics.'),
               ('Feedback, specifically',
                'Open loop means the system acts and hopes. Closed loop means it measures the result and '
                'corrects. Know which one you have built and be able to say why that was the right choice.')]),
    skills=dict(
        cred='Universal Robots Academy',
        blurb="Both platforms are self-paced and run in simulation, so you can get a long "
              "way before you touch a robot. Universal Robots issues a completion record; "
              "Festo LX is training only.",
        items=['Festo LX — industrial automation, mechatronics and ladder logic modules.',
               'Universal Robots Academy — collaborative robot programming, free and online.',
               'PLC programming — ladder logic, inputs and outputs, timers and counters.',
               'Robot controller setup — teaching positions, defining a work envelope, setting safe speeds.',
               'End-of-arm tooling — selecting or designing the gripper for the part being handled.',
               'Sensor and actuator loops — limit switches, proximity, encoders, and acting on what they report.',
               'CAD and fabrication of the mechanism itself, in Inventor or Fusion 360.',
               'Systematic commissioning — power, then I/O verification, then motion at reduced speed, then full rate.']),
    build=dict(
        blurb="Pick something with a real cycle to it. A demo that runs once is not an "
              "automated system.",
        items=[('Automated sorting cell', 'Sense a property of an incoming part — color, height, weight, material — and route it. Report the throughput and the error rate over a run of at least fifty parts.'),
               ('Pick and place with custom tooling', 'Design and fabricate the end effector yourself for a specific awkward part, then program the arm to handle it reliably. The gripper is the engineering.'),
               ('Machine tending', 'Use a robot to load and unload a piece of shop equipment. Cycle time and safe interaction are the constraints, and the safety interlock is not optional.'),
               ('Closed-loop control demo', 'Build something that holds a target — position, speed, level, temperature. Show the response with and without feedback and explain the difference in the data.')]),
    files=['Logbook template.',
           'I/O map — every input and output, what it is wired to, and what it means.',
           'Commissioning checklist.',
           'Cycle time and error rate log.',
           'Bill of Materials worksheet.',
           '&ldquo;Do Now!&rdquo; reflection and E.E.P. term-end reflection.',
           'Machine safety rules — guarding, lockout/tagout, and safe interaction distances.'],
    isnew=True,
))

P.append(dict(
    key='project', nav='Project Management', std='S4',
    title='Project Management',
    lead='Mr. Frank and Mr. Dryer',
    tag='Making a project finish on time, with the parts you actually ordered.',
    intro="This pathway is unusual: the technical work happens in the other six, and what "
          "you own here is whether it gets done. It is the pathway for people who want to "
          "run the project rather than build one part of it.",
    field=dict(
        blurb="Project management in engineering is scope, schedule, resources and risk. "
              "The engineering judgment is in deciding what to cut when something slips.",
        roles=[('Project manager', 'Owns scope, schedule and budget, and makes the call when they conflict.'),
               ('Construction manager', 'Runs a build on site — sequence, safety, subcontractors, compliance.'),
               ('Systems integrator', 'Coordinates hardware and software work across teams that do not naturally talk.'),
               ('Quality engineer', 'Defines what &ldquo;acceptable&rdquo; means and builds the inspection that checks it.')],
        note="This pathway is co-led. Take the physical and fabrication side to Mr. Frank "
             "and the systems and software side to Mr. Dryer &mdash; but the schedule is yours."),
    learn=dict(
        blurb="Four tools, all of which you will use on your capstone whether or not you "
              "choose this pathway.",
        items=[('Work breakdown structure',
                'Decompose the whole scope into deliverables small enough to estimate. If a task cannot '
                'be estimated, it has not been broken down far enough.'),
               ('Gantt charts and the critical path',
                'Map the breakdown onto a timeline, then find the sequence where any delay pushes the '
                'end date. Tasks off the critical path have slack; tasks on it do not. Track lead time '
                'for material procurement as its own task — parts that have not arrived are the most '
                'common reason a project misses.'),
               ('Decision matrices',
                'Score competing solutions against weighted criteria. Its real value is that it forces '
                'you to write down what you are optimizing for before you know which option wins.'),
               ('Requirements analysis',
                'Separate user needs — what the customer wants — from functional specifications — the '
                'measurable technical targets. Confusing the two is how projects deliver the wrong thing '
                'on time.')],
        extra=('Agile and the design process', 'Software teams often work in sprints rather '
               'than one long plan. A sprint backlog is the same idea as planning a solution; '
               'the daily loop is improve and redesign; the sprint review is test and evaluate. '
               'Different vocabulary, same cycle, shorter turns.')),
    skills=dict(
        cred='Demonstrated work breakdown structure and Gantt chart mastery',
        blurb="Assessed on real project documents from your own capstone, not on an exam.",
        items=['Build a work breakdown structure for a real project and decompose to estimable tasks.',
               'Produce a Gantt chart and identify the critical path.',
               'Track lead times and dependencies in a Bill of Materials.',
               'Run a decision matrix with weighted criteria and defend the weights.',
               'Write functional specifications that are measurable.',
               'Maintain a weekly milestone plan and update it when reality disagrees.',
               'Brilliant for the logic and mathematics behind critical path analysis.']),
    build=dict(
        blurb="Manage a real project — ideally somebody else&rsquo;s as well as your own.",
        items=[('Full capstone plan', 'Take a junior or senior capstone and produce the complete management set: breakdown structure, Gantt with critical path, Bill of Materials with lead times, and a risk list. Then run it and record where the plan was wrong.'),
               ('The revitalization pitch', 'Act as lead developer for a proposal to transform an existing space, and pitch it to stakeholders. Before-and-after visuals, technical justification for every change, and a schedule and budget that hold up to questions.'),
               ('Post-mortem', 'Take a finished project — yours or a documented one — and analyze what drove the schedule. What was on the critical path, what slipped, and what would you have done differently at week one.')]),
    files=['Logbook template.',
           'Weekly planner — milestones, dates, resources.',
           'Work breakdown structure template.',
           'Gantt chart template.',
           'Bill of Materials worksheet with lead time and unit cost.',
           'Decision matrix template.',
           'E.E.P. term-end reflection.'],
))

# ---------------------------------------------------------------- render

TOPICS = [('field', 'Explore the Field', 'Would this help someone decide whether to pick this pathway?'),
          ('learn', 'Learn the Concepts', 'Is this something you study to understand how the work works?'),
          ('skills', 'Build Your Skills', 'Is this a procedure you practice until you can do it?'),
          ('build', 'Find a Project', 'Is this something you could go build?'),
          ('files', 'Get the Files', 'Would you open this while working, rather than read start to finish?')]


def esc(s):
    return s


def render_pathway(p):
    o = []
    o.append('<section class="view" id="v-%s">' % p['key'])
    o.append('<div class="ph">')
    o.append('<p class="eyebrow">Standard %s &middot; %s</p>' % (p['std'], p['lead']))
    # h1, not h2: this is the page's own title. Eleven pages had no h1 at
    # all, which leaves a screen reader with no heading to land on.
    o.append('<h1>%s</h1>' % p['title'])
    o.append('<p class="tag">%s</p>' % p['tag'])
    o.append('<p class="intro">%s</p>' % p['intro'])
    if p.get('isnew'):
        o.append('<p class="newflag">New guide &mdash; this hub had no written guide before. '
                 'Built from the standards crosswalk and the Grade&nbsp;11 and 12 unit maps.</p>')
    o.append('</div>')

    # 1 Explore the Field
    f = p['field']
    o.append('<div class="topic"><div class="th"><span class="tn">1</span>'
             '<div><h3>Explore the Field</h3><p class="tq">%s</p></div></div>' % TOPICS[0][2])
    o.append('<p class="blurb">%s</p>' % f['blurb'])
    o.append('<div class="roles">')
    for r, d in f['roles']:
        o.append('<div><b>%s</b><span>%s</span></div>' % (r, d))
    o.append('</div>')
    if f.get('note'):
        o.append('<p class="note">%s</p>' % f['note'])
    o.append('</div>')

    # 2 Learn the Concepts
    l = p['learn']
    o.append('<div class="topic"><div class="th"><span class="tn">2</span>'
             '<div><h3>Learn the Concepts</h3><p class="tq">%s</p></div></div>' % TOPICS[1][2])
    o.append('<p class="blurb">%s</p>' % l['blurb'])
    o.append('<dl class="defs">')
    for t, d in l['items']:
        o.append('<dt>%s</dt><dd>%s</dd>' % (t, d))
    o.append('</dl>')
    if l.get('extra'):
        o.append('<div class="pullout"><b>%s</b><p>%s</p></div>' % l['extra'])
    o.append('</div>')

    # 3 Build Your Skills
    s = p['skills']
    o.append('<div class="topic"><div class="th"><span class="tn">3</span>'
             '<div><h3>Build Your Skills</h3><p class="tq">%s</p></div></div>' % TOPICS[2][2])
    o.append('<div class="cred"><span>Credential of value</span><b>%s</b>'
             '<em>Base requirement for every pathway: OSHA&nbsp;10 &mdash; Construction</em></div>' % s['cred'])
    o.append('<p class="blurb">%s</p>' % s['blurb'])
    o.append('<ul class="ticks">')
    for i in s['items']:
        o.append('<li>%s</li>' % i)
    o.append('</ul></div>')

    # 4 Find a Project
    b = p['build']
    o.append('<div class="topic"><div class="th"><span class="tn">4</span>'
             '<div><h3>Find a Project</h3><p class="tq">%s</p></div></div>' % TOPICS[3][2])
    o.append('<p class="blurb">%s</p>' % b['blurb'])
    o.append('<div class="briefs">')
    for t, d in b['items']:
        o.append('<article><b>%s</b><p>%s</p></article>' % (t, d))
    o.append('</div>')
    if b.get('extra'):
        o.append('<p class="note">%s</p>' % b['extra'])

    # Briefs this shop has actually set, harvested from the real classes. Kept
    # separate from the seeds above because these have been built and marked --
    # a student picking one knows it works as a project.
    runs = SP.RUNS.get(p['key']) or []
    if runs:
        o.append('<h4 class="runsh">Projects this shop has already run</h4>')
        o.append('<p class="blurb">Real briefs from other years, offered here '
                 'as optional work. You do not have to be in that grade to '
                 'take one on &mdash; ask first, then build it.</p>')
        o.append('<div class="runs">')
        for y, t, d in runs:
            o.append('<article><span class="ry">%s</span><b>%s</b><p>%s</p>'
                     '</article>' % (y, t, d))
        o.append('</div>')
    o.append('</div>')

    # 5 Get the Files
    o.append('<div class="topic"><div class="th"><span class="tn">5</span>'
             '<div><h3>Get the Files</h3><p class="tq">%s</p></div></div>' % TOPICS[4][2])
    o.append('<ul class="files">')
    for i in p['files']:
        o.append('<li>%s</li>' % i)
    o.append('</ul>')
    o.append('<p class="note">Logbook rules are the same in every pathway &mdash; see '
             '<em>Your Engineering Logbook</em>. Anything you read in an older hub guide '
             'about notebook rules is superseded by it.</p>')
    o.append('</div>')

    o.append('</section>')
    return '\n'.join(o)


overview = '''
<section class="view on" id="v-overview">
  <div class="ph">
    <p class="eyebrow">Elective Engineering Pathway &middot; BHR Engineering Technology</p>
    <h2>Pick a pathway, then use this</h2>
    <p class="tag">Seven hubs. One structure. Each one is a place to go deep on a field for a term.</p>
    <p class="intro">The E.E.P. is self-directed work in an emerging engineering field, for
      juniors and seniors. You anchor in one pathway, but you pull from the others when
      your project needs it &mdash; almost every good project does.</p>
  </div>

  <div class="topic">
    <div class="th"><span class="tn">&mdash;</span><div><h3>The seven pathways</h3>
      <p class="tq">Each one is the home of one state technical standard.</p></div></div>
    <p class="blurb">Standards 4 through 10 are the seven technical DESE standards, and they
      map one to one onto the seven pathways. Pick by what you want to spend a term doing,
      not by which sounds most impressive.</p>
    <div class="tw"><table>
      <thead><tr><th>Pathway</th><th>Standard</th><th>Ask</th><th>You spend the term on</th></tr></thead>
      <tbody>
        <tr><td class="k">Industrial Design</td><td class="s">8</td><td>Mr. Frank</td><td>Form, ergonomics, and designing for the machine that will make it</td></tr>
        <tr><td class="k">Architecture &amp; Civil</td><td class="s">10</td><td>Mr. Frank</td><td>Structures, sites, drainage, and construction documents</td></tr>
        <tr><td class="k">Mechanical</td><td class="s">7</td><td>Mr. Frank</td><td>Forces, motion, materials, and testing to failure</td></tr>
        <tr><td class="k">Electrical</td><td class="s">5</td><td>Mr. Dryer</td><td>Circuits, power, and instrument measurement</td></tr>
        <tr><td class="k">Software</td><td class="s">6</td><td>Mr. Dryer</td><td>Logic, code, and controlling physical hardware</td></tr>
        <tr><td class="k">Automation &amp; Robotics</td><td class="s">9</td><td>Both</td><td>Mechatronics &mdash; all three of the above at once</td></tr>
        <tr><td class="k">Project Management</td><td class="s">4</td><td>Both</td><td>Scope, schedule, resources, and getting it finished</td></tr>
      </tbody>
    </table></div>
  </div>

  <div class="topic">
    <div class="th"><span class="tn">&mdash;</span><div><h3>Every hub has the same five topics</h3>
      <p class="tq">If you cannot answer the sorting question, the resource belongs somewhere else.</p></div></div>
    <div class="tw"><table>
      <thead><tr><th>Topic</th><th>Sorting question</th><th>What belongs there</th></tr></thead>
      <tbody>
        <tr><td class="k">Explore the Field</td><td>Would this help someone decide whether to pick this pathway?</td><td>Careers, roles, what practitioners actually do</td></tr>
        <tr><td class="k">Learn the Concepts</td><td>Is this something you study to understand how the work works?</td><td>Texts, theory, the science behind the decisions</td></tr>
        <tr><td class="k">Build Your Skills</td><td>Is this a procedure you practice until you can do it?</td><td>Software walkthroughs, equipment training, technique</td></tr>
        <tr><td class="k">Find a Project</td><td>Is this something you could go build?</td><td>Design briefs, challenges, project seeds</td></tr>
        <tr><td class="k">Get the Files</td><td>Would you open this while working, rather than read start to finish?</td><td>Templates, forms, rubrics, safety rules</td></tr>
      </tbody>
    </table></div>
  </div>

  <div class="topic">
    <div class="th"><span class="tn">&mdash;</span><div><h3>True in every pathway</h3>
      <p class="tq">You do not need to read this seven times.</p></div></div>
    <dl class="defs">
      <dt>OSHA 10 &mdash; Construction</dt>
      <dd>The base credential for every pathway. Nothing in a hub happens without it on file.</dd>
      <dt>The logbook</dt>
      <dd>One set of rules, program-wide, in <em>Your Engineering Logbook</em>. Older hub guides
        carried four different notebook rulebooks; those are retired.</dd>
      <dt>Standard 11 &mdash; integrated research</dt>
      <dd>A business plan for a design in an emerging field: the technical design, evidence of
        market potential, and an implementation strategy. This is where entrepreneurship
        (Standard 14) gets covered too.</dd>
      <dt>Standard 12 &mdash; advanced elective area</dt>
      <dd>A professional technical report on a system you reverse-engineered: how the components
        interact, rebuilt digitally, and validated with simulation or testing.</dd>
      <dt>Safety, always</dt>
      <dd>Eye protection in the Makerspace. Never a tool you have not been trained and authorized on.
        Never alone with power tools. Fifteen minutes of flowing water for anything in the eyes,
        before treatment. Report every injury. Clean your area, including the floor.</dd>
      <dt>How it ends</dt>
      <dd>A portfolio and a defense &mdash; you present the work and justify the decisions, using
        your logbook as the evidence.</dd>
    </dl>
  </div>
</section>
'''

nav_items = '\n'.join(
    '<button data-v="%s"><span class="std">%s</span>%s</button>' % (p['key'], p['std'], p['nav'])
    for p in P)

html = '''<title>E.E.P. Pathway Guides</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Spectral:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>
:root{
  --paper:#f3f1f7;--card:#fff;--ink:#191622;--ink-2:#4a4359;--ink-3:#78718a;
  --rule:#cdc6db;--rule-soft:#e3ddee;--accent:#5c3d8f;--accent-soft:#eee9f7;
  --moss:#3d6b43;--moss-soft:#e2eee3;--warm:#a8541c;--warm-soft:#fbeade;
  --shadow:0 1px 2px rgba(25,22,34,.05),0 8px 24px -14px rgba(25,22,34,.2);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#100d17;--card:#1a1622;--ink:#ece8f3;--ink-2:#bcb4cc;--ink-3:#877f99;
  --rule:#332c42;--rule-soft:#262032;--accent:#b195e0;--accent-soft:#2a2140;
  --moss:#8fbe95;--moss-soft:#1c2e1f;--warm:#e0965f;--warm-soft:#36230f;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -14px rgba(0,0,0,.75);
}}
:root[data-theme="dark"]{
  --paper:#100d17;--card:#1a1622;--ink:#ece8f3;--ink-2:#bcb4cc;--ink-3:#877f99;
  --rule:#332c42;--rule-soft:#262032;--accent:#b195e0;--accent-soft:#2a2140;
  --moss:#8fbe95;--moss-soft:#1c2e1f;--warm:#e0965f;--warm-soft:#36230f;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -14px rgba(0,0,0,.75);
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--serif);
  font-size:16.5px;line-height:1.65;-webkit-font-smoothing:antialiased}
.shell{display:grid;grid-template-columns:216px minmax(0,1fr);gap:42px;
  max-width:1140px;margin:0 auto;padding:28px 24px 90px;align-items:start}
@media(max-width:900px){.shell{grid-template-columns:1fr;gap:24px}}

nav{position:sticky;top:24px;font-family:var(--sans);
  border-right:1px solid var(--rule);padding-right:18px}
@media(max-width:900px){nav{position:static;border-right:0;
  border-bottom:1px solid var(--rule);padding:0 0 18px}}
.nt{font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);
  font-family:var(--mono);margin:0 0 11px}
.nt.gap{margin-top:22px}
.navgroup{display:flex;flex-direction:column;gap:1px}
nav button{display:flex;width:100%;text-align:left;gap:9px;align-items:baseline;
  background:none;border:0;cursor:pointer;color:var(--ink-2);font-size:13.5px;
  font-weight:500;padding:6px 8px;border-radius:3px;font-family:inherit;line-height:1.35}
nav button:hover{background:var(--accent-soft);color:var(--ink)}
nav button.on{background:var(--accent-soft);color:var(--accent);font-weight:600}
nav .std{font-family:var(--mono);font-size:11px;color:var(--ink-3);flex:none;width:22px}
nav button.on .std{color:var(--accent)}

.view{display:none}
.view.on{display:block}

.ph{border-bottom:2px solid var(--ink);padding-bottom:22px;margin-bottom:34px;
  display:flex;flex-direction:column;gap:9px}
.eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--accent);margin:0}
h2{font-family:var(--sans);font-weight:800;
  font-size:clamp(28px,4.6vw,42px);line-height:1.04;letter-spacing:-.028em;margin:0;
  text-wrap:balance;max-width:18ch}
.tag{margin:0;font-family:var(--sans);font-weight:600;font-size:18px;
  color:var(--ink-2);max-width:52ch;line-height:1.35;text-wrap:balance}
.intro{margin:4px 0 0;font-size:16.5px;color:var(--ink-2);max-width:64ch}
.newflag{margin:6px 0 0;font-size:14px;color:var(--moss);background:var(--moss-soft);
  border-radius:3px;padding:8px 12px;max-width:64ch;line-height:1.45}

.topic{margin-bottom:44px}
.th{display:flex;gap:15px;align-items:flex-start;margin-bottom:14px}
.tn{font-family:var(--sans);font-weight:700;font-size:14px;color:var(--accent);
  background:var(--accent-soft);width:28px;height:28px;flex:none;border-radius:4px;
  display:grid;place-items:center;margin-top:2px}
h3{font-family:var(--sans);font-weight:700;font-size:22px;letter-spacing:-.015em;
  margin:0;line-height:1.2}
.tq{margin:3px 0 0;font-size:14px;font-style:italic;color:var(--ink-3);max-width:60ch}
.blurb{margin:0 0 16px;color:var(--ink-2);max-width:66ch}

.roles{display:flex;flex-direction:column;gap:1px;background:var(--rule);
  border:1px solid var(--rule)}
.roles div{background:var(--card);padding:13px 18px;display:grid;
  grid-template-columns:minmax(0,180px) minmax(0,1fr);gap:3px 22px}
.roles b{font-family:var(--sans);font-weight:600;font-size:15px;line-height:1.4}
.roles span{color:var(--ink-2);font-size:15px;line-height:1.5}
@media(max-width:620px){.roles div{grid-template-columns:1fr}}

dl.defs{margin:0;display:flex;flex-direction:column;gap:1px;background:var(--rule);
  border:1px solid var(--rule)}
dl.defs dt{background:var(--card);padding:14px 18px 4px;font-family:var(--sans);
  font-weight:600;font-size:15.5px;line-height:1.35}
dl.defs dd{background:var(--card);margin:0;padding:0 18px 14px;color:var(--ink-2);
  font-size:15.5px;line-height:1.55}

.pullout{margin-top:16px;background:var(--card);border:1px solid var(--rule);
  border-left:3px solid var(--accent);padding:15px 20px}
.pullout b{font-family:var(--sans);font-weight:600;font-size:15.5px;display:block;
  margin-bottom:4px}
.pullout p{margin:0;color:var(--ink-2);font-size:15.5px;line-height:1.55;max-width:66ch}

.cred{background:var(--accent-soft);border:1px solid var(--rule);padding:15px 20px;
  margin-bottom:16px;display:flex;flex-direction:column;gap:3px}
.cred span{font-family:var(--mono);font-size:10px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent)}
.cred b{font-family:var(--sans);font-weight:700;font-size:17px;line-height:1.3;
  color:var(--ink)}
.cred em{font-style:normal;font-size:14px;color:var(--ink-2);margin-top:3px}

ul.ticks,ul.files{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;
  gap:1px;background:var(--rule);border:1px solid var(--rule)}
ul.ticks li,ul.files li{background:var(--card);padding:11px 18px 11px 40px;position:relative;
  font-size:15.5px;line-height:1.5}
ul.ticks li::before{content:"";position:absolute;left:19px;top:20px;width:7px;height:7px;
  border-radius:50%;background:var(--accent)}
ul.files li::before{content:"";position:absolute;left:18px;top:17px;width:9px;height:11px;
  border:1.4px solid var(--accent);border-radius:1px}

.briefs{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.briefs article{background:var(--card);padding:16px 19px;display:flex;flex-direction:column;
  gap:6px;box-shadow:0 0 0 1px var(--rule)}
.briefs b{font-family:var(--sans);font-weight:600;font-size:15.5px;line-height:1.3}
.briefs p{margin:0;color:var(--ink-2);font-size:15px;line-height:1.5}

/* briefs the shop has really run -- same grid, but tagged with the class it
   ran in, so a student can see it is a real assignment rather than a seed */
.runsh{margin:26px 0 6px;font-family:var(--sans);font-weight:700;font-size:17px;
  letter-spacing:-.01em;color:var(--ink)}
.runs{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.runs article{background:var(--card);padding:16px 19px;display:flex;
  flex-direction:column;gap:6px;box-shadow:0 0 0 1px var(--rule)}
.runs .ry{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--accent);font-weight:700}
.runs b{font-family:var(--sans);font-weight:600;font-size:15.5px;line-height:1.3}
.runs p{margin:0;color:var(--ink-2);font-size:15px;line-height:1.5}

.note{margin:16px 0 0;font-size:14.5px;color:var(--ink-2);background:var(--card);
  border:1px solid var(--rule);border-left:3px solid var(--ink-3);padding:12px 16px;
  max-width:70ch;line-height:1.5}

.tw{overflow-x:auto;border:1px solid var(--rule);background:var(--card);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;min-width:560px;font-size:15px}
th{font-family:var(--sans);font-weight:600;font-size:10.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3);text-align:left;padding:11px 14px;
  border-bottom:1.5px solid var(--rule);white-space:nowrap}
td{padding:11px 14px;border-bottom:1px solid var(--rule-soft);vertical-align:top;line-height:1.5}
tr:last-child td{border-bottom:0}
td.k{font-family:var(--sans);font-weight:600;white-space:nowrap}
td.s{font-family:var(--mono);color:var(--accent);font-variant-numeric:tabular-nums}
em{font-style:italic}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>

<div class="shell">
  <nav>
    <p class="nt">Start here</p>
    <div class="navgroup">
      <button data-v="overview" class="on"><span class="std">&mdash;</span>All pathways</button>
    </div>
    <p class="nt gap">The seven</p>
    <div class="navgroup">
      __NAV__
    </div>
  </nav>
  <main>
__OVERVIEW__
__VIEWS__
  </main>
</div>

<script>
document.querySelectorAll('nav button').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('nav button').forEach(function(x){x.classList.remove('on');});
    document.querySelectorAll('.view').forEach(function(x){x.classList.remove('on');});
    b.classList.add('on');
    var v=document.getElementById('v-'+b.dataset.v);
    if(v){v.classList.add('on');}
    window.scrollTo({top:0,behavior:'smooth'});
  });
});
</script>
'''

if __name__ == '__main__':
    html = html.replace('__NAV__', nav_items)
    html = html.replace('__OVERVIEW__', overview)
    html = html.replace('__VIEWS__', '\n'.join(render_pathway(p) for p in P))

    open('/tmp/outputs/eep-guides.html', 'w').write(html)
    print('built', len(html), 'bytes')
