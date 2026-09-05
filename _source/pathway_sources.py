#!/usr/bin/env python3
"""
Sources for the pathway hubs, sorted into the five topics.

Origin: the Gemini Notebook built for each pathway. Those notebooks were
assembled by Gemini's source-discovery feature, which answered "what is this
discipline" rather than "what should a high school student explore" — so the
raw lists mix genuinely good student material with university syllabi,
paywalled textbooks and dead links.

What survives here passed three tests:
  it opens        no paywall, no login, no dead link
  it is respected a real institution or practitioner, not a content farm
  it is on topic  actually about this pathway

Breadth is deliberate. The hubs are for self-discovery, so depth is fine —
`level` tells a student what they are opening rather than keeping them out.

  start    approachable now, no background needed
  deeper   assumes some grounding; worth the effort
  college  university-level or professional reference

EVERY URL BELOW WAS FETCHED AND CONFIRMED IN SEPTEMBER 2026. Do not add an
entry without checking it the same way — a dead link on a student page is
worse than an absent one.
"""

S = []


def add(path, topic, title, url, level='start', kind='video', note=''):
    S.append(dict(path=path, topic=topic, title=title, url=url,
                  level=level, kind=kind, note=note))


LEVELS = {
    'start':   ('Start here', 'ok'),      # school green
    'deeper':  ('Going deeper', 'deep'),  # school blue
    'college': ('College level', 'hard'), # navy outline -- serious, not a warning
}

TOPIC_NUM = {'field': 1, 'learn': 2, 'skills': 3, 'build': 4, 'files': 5}


# ==================================================================
# ARCHITECTURE & CIVIL ENGINEERING
# The strongest of the seven notebooks. Massachusetts building code
# makes it specific to these students rather than generic.
# ==================================================================

# --- 1. Explore the Field -----------------------------------------
add('architecture', 'field', '7 principles for building better cities',
    'https://www.ted.com/talks/peter_calthorpe_7_principles_for_building_better_cities',
    'start', 'talk',
    'Peter Calthorpe, TED. Why cities are shaped the way they are, and what '
    'would have to change.')

add('architecture', 'field', 'First year architecture student project',
    'https://www.youtube.com/watch?v=RKEGqwZBfn0', 'start', 'video',
    'What an end-of-term submission and studio life actually look like. The '
    'most honest preview of the next step after here.')

add('architecture', 'field', 'How to create an architecture portfolio',
    'https://www.youtube.com/watch?v=-hdmy7cK6cI', 'start', 'video',
    'DamiLee. Relevant sooner than you think &mdash; your Independent Focus work is the '
    'portfolio.')

add('architecture', 'field', 'Peter Cook on the benefits of drawing by hand',
    'https://www.youtube.com/watch?v=1suurGcp8BI', 'deeper', 'talk',
    'Louisiana Channel. An architect arguing for the pencil in a CAD world.')

# --- 2. Learn the Concepts ----------------------------------------
add('architecture', 'learn', 'Understanding and analysing trusses',
    'https://www.youtube.com/watch?v=Hn_iozUo9m4', 'start', 'video',
    'The Efficient Engineer. Method of joints and method of sections, clearly.')

add('architecture', 'learn', 'How to read architectural plans',
    'https://www.youtube.com/watch?v=vrTJ25lx7bo', 'start', 'video',
    'For beginners. Start here before your first drawing set.')

add('architecture', 'learn', 'Architectural plans explained',
    'https://www.youtube.com/watch?v=8opn2McSc0E', 'start', 'video',
    'Stewart Hicks. Why plans are drawn the way they are.')

add('architecture', 'learn', 'How this tower barely touches the ground',
    'https://www.youtube.com/watch?v=kNph_SxgcPg', 'start', 'video',
    'Stewart Hicks. A structure that looks impossible, explained &mdash; the '
    'Unique Concept capstone in one video.')

add('architecture', 'learn', 'Harvard model bridge testing',
    'https://www.youtube.com/watch?v=oqUNMGr0lo8', 'start', 'video',
    'Trusses and beams tested to failure. Watch what actually breaks first.')

add('architecture', 'learn', 'An introduction to BIM',
    'https://www.istructe.org/resources/guidance/an-introduction-to-building-information-modelling/',
    'deeper', 'doc',
    'Institution of Structural Engineers. Free download, no membership needed.')

add('architecture', 'learn', 'Basic Structural Design (MIT 4.440)',
    'https://ocw.mit.edu/courses/4-440-basic-structural-design-spring-2009/',
    'college', 'course',
    'Full MIT course materials, free. From 2009 &mdash; the structures have '
    'not changed.')

add('architecture', 'learn', 'BIM Use Definitions standard',
    'https://nibs.org/nbims/v4/bud/', 'college', 'doc',
    'National Institute of Building Sciences. What each BIM use formally means.')

# --- 3. Build Your Skills -----------------------------------------
add('architecture', 'skills', 'Revit for beginners',
    'https://www.youtube.com/playlist?list=PLe_I-JWckL7HnPkUSHT3FhT4mEEz8OTYe',
    'start', 'playlist',
    'Complete beginner playlist. Revit is the ACU certification for this '
    'pathway, so this is the one to work through.')

add('architecture', 'skills', 'AutoCAD Civil 3D for beginners',
    'https://www.youtube.com/watch?v=nPLskWcmUrI', 'start', 'video',
    'Full walkthrough. This is the site and grading tool.')

add('architecture', 'skills', 'A better way to draw in AutoCAD',
    'https://www.youtube.com/watch?v=SKD_lTiAf4k', 'start', 'video',
    'One setting that changes how drawing feels. Worth six minutes.')

add('architecture', 'skills', 'Three styles to sketch like an architect',
    'https://www.youtube.com/watch?v=lEAWy2ms7gw', 'start', 'video',
    'Henry Gao. Sketching is still how ideas get out fastest.')

add('architecture', 'skills', 'Draw like an architect',
    'https://www.youtube.com/watch?v=24rnfO8s0hU', 'start', 'video',
    '30X40 Design Workshop. Essential drawing tips.')

add('architecture', 'skills', 'Sketching and designing architectural details',
    'https://www.youtube.com/watch?v=v8gTCuvQxBc', 'deeper', 'video',
    '30X40 Design Workshop. Where a building actually gets resolved.')

add('architecture', 'skills', 'Skyscraper in Revit',
    'https://www.youtube.com/watch?v=nfOtPvts3Tw', 'deeper', 'video',
    'Balkan Architect. A full tower, start to finish.')

add('architecture', 'skills', '3D terrain from Google Maps in Blender',
    'https://www.youtube.com/watch?v=Mj7Z1P2hUWk', 'deeper', 'video',
    'CG Geek. How to get real site topography into a model.')

# --- 4. Find a Project --------------------------------------------
add('architecture', 'build', 'Structural design for laser cutting',
    'https://aetlabs.com/events/structural-design-for-laser-cutting-student-project-ideas/',
    'start', 'doc',
    'Student project ideas, free recorded session. Note this is an equipment '
    'vendor&rsquo;s page, so it is part sales pitch &mdash; the project ideas '
    'are still good.')

add('architecture', 'build', 'Flexible buildings: the future of architecture',
    'https://www.youtube.com/watch?v=sw9zpH717ts', 'start', 'video',
    'Free Documentary. Buildings that adapt rather than get demolished.')

add('architecture', 'build', 'This city concept breaks architecture',
    'https://www.youtube.com/watch?v=2b7uMJkvS0o', 'start', 'video',
    'DamiLee on THE LINE. A serious critique of a famous megaproject &mdash; '
    'good model for the Revitalization pitch.')

add('architecture', 'build', 'The CityTree',
    'https://www.youtube.com/watch?v=gGCJrqv0xPQ', 'start', 'video',
    'CNET. Moss that cleans and cools city air. Regenerative design, built.')

add('architecture', 'build', 'Large high-rise model building',
    'https://www.youtube.com/watch?v=CfgYtMGmSxM', 'deeper', 'video',
    'Korean model-building technique, full process. If you are making a '
    'physical model, watch this first.')

# --- 5. Get the Files ---------------------------------------------
add('architecture', 'files', 'Massachusetts State Building Code, 10th edition',
    'https://www.mass.gov/handbook/tenth-edition-of-the-ma-state-building-code-780',
    'college', 'doc',
    'The actual code your buildings would be held to, 780 CMR. Published as '
    'one page per chapter &mdash; this is the index.')

add('architecture', 'files', '780 CMR Chapter 16 — Structural Design',
    'https://www.mass.gov/regulations/780-CMR-tenth-edition-chapter-16-structural-design-amendments',
    'college', 'doc',
    'The structural chapter, if you want to see what a real load requirement '
    'looks like written down.')

add('architecture', 'files', 'Massachusetts Stormwater Handbook and Standards',
    'https://www.mass.gov/guides/massachusetts-stormwater-handbook-and-stormwater-standards',
    'deeper', 'doc',
    'Where drainage requirements on a site plan come from.')

add('architecture', 'files', 'MassDOT stormwater design guide',
    'https://www.mass.gov/info-details/stormwater-management-unit', 'deeper', 'doc',
    'The state highway version. Link goes to the landing page; the guide '
    'itself is a very large download.')

add('architecture', 'files', 'Stormwater report checklist',
    'https://www.mass.gov/doc/stormwater-report-checklist/download', 'deeper', 'doc',
    'MassDEP. A real professional checklist &mdash; use it on your site plan.')

add('architecture', 'files', 'BIM guidelines for design and construction',
    'https://www.mass.gov/info-details/bim-guidelines-for-design-and-construction',
    'deeper', 'doc',
    'DCAMM. How the Commonwealth expects BIM to be delivered on its projects.')

add('architecture', 'files', 'Designer procedures and guidelines',
    'https://www.mass.gov/info-details/designer-procedures-and-guidelines',
    'college', 'doc',
    'DCAMM. What a designer is actually contracted to produce.')

add('architecture', 'files', 'MIT design standards — BIM and CAD drawing',
    'https://web.mit.edu/facilities/maps/DesignStandards/T03%20-%20BIM%20and%20CAD%20Drawing%20Standards%202022.pdf',
    'deeper', 'doc',
    'A real institution&rsquo;s drawing standard, 2022. Layer naming, file '
    'structure, the unglamorous part that makes a set usable.')

add('architecture', 'files', 'Architects: Massachusetts statutes and regulations',
    'https://www.mass.gov/lists/architects-statutes-and-regulations', '', 'doc',
    '231 CMR &mdash; what it takes to be a registered architect in this state.')
S[-1]['level'] = 'deeper'

add('architecture', 'files', 'Free CAD blocks (.dwg)',
    'https://cad-blocks.net/', 'start', 'tool',
    'Doors, windows, furniture, vehicles. Free, no sign-up. Stop drawing a '
    'toilet from scratch.')

add('architecture', 'files', 'Site planning and design (TM 5-803-14)',
    'https://www.wbdg.org/FFC/ARMYCOE/COETM/ARCHIVES/tm_5_803_14.pdf',
    'college', 'doc',
    'US Army manual on site planning. Archived and superseded &mdash; read it '
    'as a thorough reference, not as current practice.')


# ------------------------------------------------------------------
# Dropped from the Architecture notebook, and why. Kept as a record so
# nobody re-adds them.
#
#   SciShow Kids "What Makes Bridges So Strong?"  aimed at ages 5-9
#   Town subdivision regs (Cohasset, Sheffield)   too narrow to be useful
#   Methuen zoning board letter                   a single case document
#   "Just a moment..."                            Cloudflare error page
#   "R U L E S A N D R E G U L A T I"             broken extraction
#   Vanasse Hangen Brustlin consultant doc        not a teaching resource
#   "For DCAMM Use Only", "GLOSSARY"              fragments
#   CNM-205 surveying syllabus                    college course admin
#
# CORRECTION: the notebook cited 250 CMR as the architects' board. It is
# not — 250 CMR is Professional Engineers and Land Surveyors. Architects
# are 231 CMR, which is what is linked above.
# ------------------------------------------------------------------


def by(path, topic):
    return [s for s in S if s['path'] == path and s['topic'] == topic]


def count(path):
    return len([s for s in S if s['path'] == path])


# ==================================================================
# AUTOMATION & ROBOTICS
# The other strong notebook. Every YouTube link below was confirmed by
# title AND channel through YouTube's own oEmbed endpoint, not by
# search-index matching — several near-identical videos exist for the
# maker items and the wrong one would be easy to link.
# ==================================================================

# --- 1. Explore the Field -----------------------------------------
add('automation', 'field', 'The robot sidekicks of Jorvon Moss',
    'https://www.youtube.com/watch?v=3dnC_y8bDrU', 'start', 'video',
    'Adam Savage&rsquo;s Tested. A working maker whose robots are companions '
    'rather than machines &mdash; a real career built out of this pathway.')

add('automation', 'field', 'Devices that morph and transform',
    'https://www.youtube.com/watch?v=CdPLzA4xIF0', 'start', 'video',
    'Brigham Young University. Compliant mechanisms &mdash; things that move '
    'without joints. Research engineering you can actually watch.')

add('automation', 'field', 'BYU Compliant Mechanisms Research',
    'https://compliantmechanisms.byu.edu/', 'deeper', 'doc',
    'The lab behind that video, with papers and downloadable models.')

# --- 2. Learn the Concepts ----------------------------------------
add('automation', 'learn', 'How things are made',
    'https://www.youtube.com/watch?v=Um_g8sQ_p3Y', 'start', 'video',
    'The Efficient Engineer. Animated tour of manufacturing processes &mdash; '
    'casting, forming, machining, joining. Where to start.')

add('automation', 'learn', 'Automating Manufacturing Systems with PLCs',
    'https://archive.org/details/ost-engineering-plcbook5_1', 'deeper', 'doc',
    'Hugh Jack&rsquo;s full textbook, free and open. The best free PLC '
    'reference there is. The author&rsquo;s old site is dead &mdash; this '
    'Internet Archive copy is the live one.')

add('automation', 'learn', 'Mechatronics video demos and lab manual',
    'https://mechatronics.colostate.edu/', 'deeper', 'course',
    'Colorado State&rsquo;s free companion site to the standard mechatronics '
    'textbook. Video demonstrations and a full lab manual, no book needed.')

add('automation', 'learn', 'Introduction to Robotics (Stanford CS223A)',
    'https://see.stanford.edu/Course/CS223A', 'college', 'course',
    'Oussama Khatib&rsquo;s course, free through Stanford Engineering '
    'Everywhere. Serious mathematics &mdash; but it is the real thing.')

# --- 3. Build Your Skills -----------------------------------------
add('automation', 'skills', 'Universal Robots Academy — free e-learning',
    'https://academy.universal-robots.com/free-e-learning/', 'start', 'course',
    'Six tracks on programming collaborative robots, all in simulation so no robot '
    'is needed. Start with UR20/30, then e-Series. This is the manufacturer of the '
    'UR3 and UR5 in our own shop, so it maps straight onto real hardware. '
    'Free account required.')

add('automation', 'skills', 'Universal Robots Academy — Risk Assessment track',
    'https://academy.universal-robots.com/free-e-learning/', 'start', 'course',
    'The module worth doing even if you never program a robot. A cobot is not '
    'inherently safe — only the application around it can be, and this is how '
    'that judgement is actually made. Pairs with the shop cobot safety check.')

add('automation', 'skills', 'PLC programming with Micro800',
    'https://www.youtube.com/watch?v=ZiPO2J3ZBG8', 'start', 'video',
    'Tim Wilborne. Connected Components Workbench from scratch.')

add('automation', 'skills', 'Getting started with PLCs — classroom projects',
    'https://www.youtube.com/watch?v=y8p8SfeOOks', 'start', 'video',
    'Aimed at high school specifically. Note the channel is an equipment '
    'vendor, so there is some product placement.')

add('automation', 'skills', 'Dobot Magician and Dobot Studio',
    'https://www.youtube.com/watch?v=QaEV0gNT2Ug', 'start', 'video',
    'Setup and first program on the desktop arm.')

add('automation', 'skills', 'Titans of CNC Academy',
    'https://academy.titansofcnc.com/', 'start', 'course',
    'Free CNC training, start to finish. A free account is needed to watch, '
    'but nothing is paid.')

add('automation', 'skills', 'Program the TITAN-2M in Fusion 360',
    'https://academy.titansofcnc.com/video/how-to-program-the-titan-2m',
    'deeper', 'video',
    'CAM in the software you already use, on a real machine.')

add('automation', 'skills', 'Robotiq wrist camera — parametric object teaching',
    'https://www.youtube.com/watch?v=3bhboLZCbm8', 'deeper', 'video',
    'Teaching a robot to find an object by sight rather than by coordinate.')

add('automation', 'skills', 'Robotiq eLearning',
    'https://elearning.robotiq.com/course/view.php?id=5&section=4',
    'deeper', 'course',
    'Full lessons on grippers and vision. Open with guest access &mdash; no '
    'login needed.')

add('automation', 'skills', 'Siemens SCE training documents',
    'https://www.siemens.com/en-us/content/sce-educational-institutions/documents/',
    'college', 'doc',
    'Industrial-grade PLC and TIA Portal curriculum, free. It does require a '
    'Siemens account to download, which is a slog &mdash; worth it if you are '
    'going deep on PLCs.')

# --- 4. Find a Project --------------------------------------------
add('automation', 'build', 'I built cute robots for your desk... again',
    'https://www.youtube.com/watch?v=UOrwMG7Eqks', 'start', 'video',
    'Creative Chance. Small, achievable, and genuinely charming. A good first '
    'robot that is not a kit.')

add('automation', 'build', 'How do welding squares get made?',
    'https://www.youtube.com/watch?v=GdFVIEM5KBo', 'start', 'video',
    'Fireball Tool. Manufacturing a precision tool from raw stock &mdash; '
    'tolerance and fixturing made visible.')

add('automation', 'build', 'Machining aluminium isogrid coasters',
    'https://www.youtube.com/watch?v=-XxDSFjIRa0', 'deeper', 'video',
    'Winston Moy. Isogrid is the structure used on rocket bodies, cut here at '
    'coaster scale. Small project, real technique.')

# --- 5. Get the Files ---------------------------------------------
add('automation', 'files', 'SVGnest',
    'https://svgnest.com/', 'start', 'tool',
    'Free open-source nesting &mdash; packs your parts onto a sheet with the '
    'least waste. Use it before every laser or plasma job.')

add('automation', 'files', 'Deepnest',
    'https://deepnest.io/', 'start', 'tool',
    'The same author&rsquo;s successor to SVGnest, more capable for laser and '
    'plasma. Also free and open source.')


# ------------------------------------------------------------------
# Dropped from the Robotics & Automation notebook, and why.
#
#   FluidSIM                        paid product; only a 30-day trial is free
#   The Robotics Primer (MIT Press) commercial book, ~$30. The free PDFs
#                                   circulating are unauthorised copies
#   IBM TJBot                       IBM has discontinued support; the Watson
#                                   services it depends on have changed
#   Epilog laser tube replacement   high-voltage service task, not a student
#                                   activity
#   xTool D1 review                 vendor-seeded product review
#   Epilog Fusion Pro overview      manufacturer marketing
#   Modern Robotics (Cambridge)     paywalled — the notebook flagged this itself
#   ~12 university syllabi          course admin, not teaching material
#   NUREG/CR-6090 PLCs in nuclear
#     reactor systems               genuinely interesting, genuinely not for a
#                                   high school hub
# ------------------------------------------------------------------


# ==================================================================
# MECHANICAL ENGINEERING
# Good maker material buried under fifteen FEA papers and a dozen
# university catalogues. What is here is the top layer.
# ==================================================================

# --- 1. Explore the Field -----------------------------------------
add('mechanical', 'field', 'What I do as a mechanical design engineer',
    'https://www.youtube.com/watch?v=pX03H1oeyN0', 'start', 'video',
    'Tamer Shaheen. A working engineer describing an actual week.')

add('mechanical', 'field', 'The one skill that changed my career',
    'https://www.youtube.com/watch?v=07ynjb23r5c', 'start', 'video',
    'Engineering Gone Wild. Worth watching before you decide what to get good at.')

add('mechanical', 'field', 'How a Harvard professor makes transforming toys',
    'https://www.youtube.com/watch?v=xN9hTo3iR6A', 'start', 'video',
    'WIRED, on Chuck Hoberman. Mechanisms as a career, not a hobby.')

# --- 2. Learn the Concepts ----------------------------------------
add('mechanical', 'learn', 'Understanding engineering drawings',
    'https://www.youtube.com/watch?v=ht9GwXQMgpo', 'start', 'video',
    'The Efficient Engineer. The clearest explanation of what a drawing is '
    'actually telling you. Start here.')

add('mechanical', 'learn', '507 Mechanical Movements',
    'https://507movements.com/', 'start', 'tool',
    'Henry Brown&rsquo;s 1868 catalogue of mechanisms, animated. When you need '
    'a way to turn one motion into another, the answer is probably in here.')

add('mechanical', 'learn', 'Aerodynamics, explained by a record-holder',
    'https://www.youtube.com/watch?v=3KqjRPV9_PY', 'start', 'video',
    'WIRED, with the world-record paper aeroplane designer. Real fluid '
    'dynamics on a subject you can test at your desk.')

add('mechanical', 'learn', 'Engineering Statics: Open and Interactive',
    'https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics:_Open_and_Interactive_(Baker_and_Haynes)',
    'deeper', 'doc',
    'Baker and Haynes. A complete free statics textbook, openly licensed, with '
    'interactive figures. Statics only &mdash; no dynamics.')

add('mechanical', 'learn', 'Introduction to Statics and Dynamics',
    'https://ruina.tam.cornell.edu/Book/index.html', 'college', 'doc',
    'Ruina and Pratap, Cornell. Free, 1,000 pages, and genuinely rigorous. '
    'Read it from the author&rsquo;s page &mdash; he asks that the files not '
    'be copied elsewhere.')

add('mechanical', 'learn', 'NASA engineering drawing standards manual',
    'https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/NASA%20GSFC-X-673-64-1F.pdf',
    'college', 'doc',
    'Goddard Space Flight Center. What drawing standards look like when the '
    'part has to work in orbit.')

# --- 3. Build Your Skills -----------------------------------------
add('mechanical', 'skills', 'Planetary gear train in Fusion 360',
    'https://www.youtube.com/watch?v=W-tIlhVpZpw', 'start', 'video',
    'Modelling and animating a real gear train. The best single Fusion '
    'exercise for understanding assemblies.')

add('mechanical', 'skills', 'Parametric Lego bricks in Fusion 360',
    'https://www.instructables.com/Parametric-Lego-Bricks-in-Fusion-360/',
    'start', 'doc',
    'Six steps, and it teaches parametric modelling better than most courses. '
    'Change one number, get a different brick.')

add('mechanical', 'skills', 'Designing snap-fit joints for 3D printing',
    'https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/',
    'start', 'doc',
    'Real design rules with the maths. It sits on a manufacturing '
    'company&rsquo;s site &mdash; the engineering is sound, the quote button '
    'is not for you.')

add('mechanical', 'skills', 'Designing for mass production',
    'https://www.youtube.com/watch?v=NLeTvSaPJIs', 'start', 'video',
    'Slant 3D. Corner brackets designed for a print farm rather than one '
    'print. Note the channel belongs to a printing service.')

add('mechanical', 'skills', 'Toothpick bridge stress simulation',
    'https://www.youtube.com/watch?v=UxO7NoWUaDU', 'deeper', 'video',
    'Fusion 360 simulation on something you can also build and break. The '
    'cheapest way to check a simulation against reality.')

add('mechanical', 'skills', 'Reverse engineering a car part from scan data',
    'https://www.youtube.com/watch?v=dnRh4aYvdpU', 'deeper', 'video',
    'Fender modelling from a 3D scan. This is the Standard 12 reverse '
    'engineering task, done properly.')

add('mechanical', 'skills', 'Ansys Student',
    'https://ansys.synopsys.com/academic/students/ansys-student.html',
    'deeper', 'tool',
    'Professional FEA, free for students, no cost and no purchase. Windows '
    'only and a large install &mdash; check with Mr. Frank before putting it '
    'on a school machine.')

# --- 4. Find a Project --------------------------------------------
add('mechanical', 'build', 'Hydraulics from cheap plastic syringes',
    'https://www.youtube.com/watch?v=ioLtieMWRT8', 'start', 'video',
    'Adam Savage. Working hydraulics for a few dollars &mdash; a real system '
    'you can build this week.')

add('mechanical', 'build', 'Mechanical clocks are simpler than you think',
    'https://www.youtube.com/watch?v=yfNFbE0ahi0', 'start', 'video',
    'Engineezy, 3D printing a clock. Escapements, gear ratios and tolerance '
    'all in one build.')

add('mechanical', 'build', '18 mechanical design tips',
    'https://www.youtube.com/watch?v=TbWFRvMV3gw', 'start', 'video',
    'Jeremy Fielding. Hard-won practical advice you will not find in a '
    'textbook.')

add('mechanical', 'build', 'Rolling objects that are not spheres',
    'https://www.youtube.com/watch?v=fRqwYsfiME8', 'start', 'video',
    'Maker&rsquo;s Muse. Constant-width shapes. A small print with genuinely '
    'surprising geometry behind it.')

add('mechanical', 'build', '3D printed planetary gearbox',
    'https://www.youtube.com/watch?v=d9P5LBQqgFo', 'deeper', 'video',
    'Michael Rechtin. Resin against FDM for the same gearbox &mdash; a real '
    'process comparison with data.')

add('mechanical', 'build', 'Redesigning vintage electronics',
    'https://www.youtube.com/watch?v=9TwW0Jfkz3g', 'deeper', 'video',
    'Distracted by Design. Reverse engineering plus restoration, which is two '
    'standards in one project.')


# ==================================================================
# INDUSTRIAL DESIGN
# Strong core, odd tail. The military human-factors standards that
# dominated the notebook are almost all gone — see the note below.
# ==================================================================

# --- 1. Explore the Field -----------------------------------------
add('industrial', 'field', 'Combine art and engineering',
    'https://www.ted.com/talks/bran_ferren_to_create_for_the_ages_let_s_combine_art_and_engineering',
    'start', 'talk',
    'Bran Ferren, TED. The argument for this pathway existing at all.')

add('industrial', 'field', 'LEGO for grownups',
    'https://www.ted.com/talks/hillel_cooperman_lego_for_grownups', 'start', 'talk',
    'Hillel Cooperman, TED. On play as design practice.')

add('industrial', 'field', 'How Pixar&rsquo;s animation evolved over 24 years',
    'https://www.youtube.com/watch?v=qTPKGVrFtQU', 'start', 'video',
    'Insider. Technical constraint driving aesthetic decisions, traced across '
    'four films.')

# --- 2. Learn the Concepts ----------------------------------------
add('industrial', 'learn', 'Why our screwdriver took three years',
    'https://www.youtube.com/watch?v=2K5Gqp1cEcM', 'start', 'video',
    'Linus Tech Tips. Genuinely the best account of design-for-manufacture '
    'and tolerance stacking on the internet. It is also a long advert for '
    'their own product, and there is some mild language.')

add('industrial', 'learn', 'Ergonomics and design: a reference guide',
    'https://ehs.oregonstate.edu/sites/ehs.oregonstate.edu/files/pdf/ergo/ergonomicsanddesignreferenceguidewhitepaper.pdf',
    'deeper', 'doc',
    'Anthropometric tables and reach zones &mdash; the actual numbers for '
    'sizing a product to a human. Written by a furniture manufacturer, which '
    'is why the examples are all chairs, but the data is the data.')

add('industrial', 'learn', 'Human Factors Design Standard (FAA)',
    'https://hf.tc.faa.gov/publications/2016-12-human-factors-design-standard/',
    'college', 'doc',
    'What a real human-factors specification looks like &mdash; 900 pages of '
    'it, for air traffic control consoles. Browse it to see the level of '
    'detail professionals work to; do not try to read it.')

# --- 3. Build Your Skills -----------------------------------------
add('industrial', 'skills', '3D sketching in Fusion 360',
    'https://www.youtube.com/watch?v=TNrPnerxvnA', 'start', 'video',
    'Frame design. 3D sketch is the tool most people skip and then need.')

add('industrial', 'skills', 'Realistic renderings in Fusion 360',
    'https://www.youtube.com/watch?v=ewRzgxK0wLk', 'start', 'video',
    'Autodesk&rsquo;s own tutorial. Rendering is how your design gets taken '
    'seriously in a pitch.')

add('industrial', 'skills', 'The Fusion Essentials',
    'https://www.youtube.com/@TheFusionEssentials', 'start', 'playlist',
    'A whole channel of Fusion lessons. Not affiliated with Autodesk, and '
    'often clearer for it.')

add('industrial', 'skills', 'Poly Haven',
    'https://polyhaven.com/', 'start', 'tool',
    'Free HDRIs, textures and models, public domain, no account. This is what '
    'makes a render stop looking like a render.')


# ------------------------------------------------------------------
# Dropped from the Mechanical and Industrial Design notebooks, and why.
#
#   MakerBot / Mattel toy workshop   registration wall harvesting name, email,
#                                    employer and phone. Never on a student page
#   Vectr                            no longer a free vector editor; now a paid
#                                    AI logo tool
#   Delft Design Guide               commercial book, not free
#   The Way We Design                academic conference paper, not a manual
#   Adobe Illustrator sushi tutorial requires a paid Illustrator licence
#   ZenTek "Direct Modeling"         CAD reseller's promotional video
#   SOLIDWORKS finger skateboard     we are Autodesk only
#   MIL-STD-1472H, NASA-STD-3001     military and spaceflight compliance
#                                    standards; mispitched for this audience
#   Handbook of Human Factors and
#     Ergonomics Methods             commercial book; the free PDFs online are
#                                    unauthorised copies
#   "NASA Mechanical Design
#     Reliability Handbook"          not NASA — an ASQ publication, and a
#                                    reliability statistics monograph well past
#                                    grade 12
#   CMU "Introduction to Finite
#     Element Methods"               actually computer-graphics radiosity, not
#                                    mechanical FEA. Wrong subject entirely
#   ~15 FEA papers, ~12 university
#     catalogues                     course admin and graduate research
#   "ERROR: The request could not
#     be satisfied"                  a captured error page
# ------------------------------------------------------------------


# ==================================================================
# ELECTRICAL ENGINEERING
# The notebook had only 31 sources and it showed. This is researched
# rather than filtered — found for this age group, not inherited.
# ==================================================================

add('electrical', 'field', 'What is electrical engineering?',
    'https://www.youtube.com/watch?v=QQewdCJTcIU', 'start', 'video',
    'Zach Star. The whole field surveyed &mdash; power, signals, controls, '
    'semiconductors &mdash; so you know what you are choosing between.')

add('electrical', 'field', 'How does the power grid work?',
    'https://www.youtube.com/watch?v=v1BMWczn7JM', 'start', 'video',
    'Practical Engineering. Grady builds physical demo rigs. The bridge from '
    'a breadboard circuit to actual infrastructure.')

add('electrical', 'field', 'How are microchips made?',
    'https://www.youtube.com/watch?v=dX9CGRZwD-w', 'start', 'video',
    'Branch Education. Photoreal animation of a semiconductor fab. The best '
    'single argument for caring about electronics.')

add('electrical', 'field', 'Electrical engineers — Occupational Outlook',
    'https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm',
    'start', 'doc',
    'Bureau of Labor Statistics. Real duties, real pay, real growth figures, '
    'updated this year. Use this for your Career Vision Summary rather than '
    'whatever a search turns up.')

add('electrical', 'learn', 'Ohm&rsquo;s law, voltage, current and resistance',
    'https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/all',
    'start', 'doc',
    'SparkFun. The cleanest first explanation there is &mdash; water-tank '
    'analogy, then V&nbsp;=&nbsp;IR, then picking a real resistor for an LED.')

add('electrical', 'learn', 'Resistors and colour codes',
    'https://learn.sparkfun.com/tutorials/resistors/all', 'start', 'doc',
    'Four, five and six band codes plus series and parallel combination. Two '
    'things you need, one page.')

add('electrical', 'learn', 'All About Circuits — the full textbook',
    'https://www.allaboutcircuits.com/textbook/', 'start', 'doc',
    'Six volumes: DC, AC, semiconductors, digital, reference, and DIY '
    'experiments. Openly licensed, no account. The backbone of this pathway.')

add('electrical', 'learn', 'Khan Academy — circuit analysis',
    'https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic',
    'start', 'course',
    'Ohm and Kirchhoff with worked practice problems. Free; the account is '
    'only for tracking progress.')

add('electrical', 'learn', 'Ultimate Electronics',
    'https://ultimateelectronicsbook.com/', 'deeper', 'doc',
    'A free book with 200+ live simulations built in &mdash; change a value '
    'and watch the maths move. Theory you can poke at.')

add('electrical', 'learn', 'Kirchhoff&rsquo;s circuit laws',
    'https://www.youtube.com/watch?v=d-a9Pr2z-qg', 'deeper', 'video',
    'From ElectroBOOM&rsquo;s teaching series, which is a real from-zero '
    'course. Worth knowing his main channel is deliberate high-voltage '
    'stunts &mdash; entertaining, and the opposite of how to work safely.')

add('electrical', 'learn', 'Circuits and Electronics (MIT 6.002)',
    'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/',
    'college', 'course',
    'Full MIT course, free. Lectures, notes, labs and exams. The set textbook '
    'is not free &mdash; work from the lecture notes.')

add('electrical', 'skills', 'How to use a multimeter',
    'https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/all',
    'start', 'doc',
    'Voltage, resistance, current, continuity &mdash; and how people blow the '
    'fuse measuring current wrong. Read before you touch the bench meter.')

add('electrical', 'skills', 'How to use a breadboard',
    'https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all',
    'start', 'doc',
    'Rails, the centre ravine, and a worked LED and button build.')

add('electrical', 'skills', 'How to solder',
    'https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all',
    'start', 'doc',
    'Through-hole soldering. The joint should look like a volcano, not a '
    'ball &mdash; and now you know why.')

add('electrical', 'skills', 'How to use an oscilloscope',
    'https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope/all',
    'deeper', 'doc',
    'Controls, triggering, and 10X probe compensation &mdash; which is the '
    'calibration step Standard 5 asks for.')

add('electrical', 'skills', 'Introduction to the oscilloscope',
    'https://www.youtube.com/watch?v=Iq4QlfH-oqk', 'deeper', 'video',
    'EEVblog #926. A practising engineer walking the whole instrument. Pair '
    'it with the written guide above.')

add('electrical', 'skills', 'How NOT to blow up your oscilloscope',
    'https://www.youtube.com/watch?v=xaELqAo4kkQ', 'deeper', 'video',
    'EEVblog #279, on scope grounding. Watch this before plugging a probe '
    'into anything mains-referenced.')

add('electrical', 'skills', 'Arduino built-in examples',
    'https://docs.arduino.cc/built-in-examples/', 'start', 'doc',
    'Sixty-plus first-party examples that ship inside the IDE. The official '
    'skills ladder, from blinking an LED to reading sensors.')

add('electrical', 'skills', 'Multi-tasking the Arduino',
    'https://learn.adafruit.com/multi-tasking-the-arduino-part-1', 'deeper', 'doc',
    'Adafruit. How to stop using delay() and write code that does more than '
    'one thing. The single biggest step up from beginner Arduino.')

add('electrical', 'build', 'SparkFun Inventor&rsquo;s Kit guide',
    'https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41/all',
    'start', 'doc',
    'Sixteen circuits with wiring, code and explanation. You can build every '
    'one in Tinkercad Circuits without owning the kit.')

add('electrical', 'build', 'Adafruit Learn — sensors',
    'https://learn.adafruit.com/category/sensors', 'start', 'doc',
    'Temperature, light, motion, distance, orientation &mdash; each a '
    'complete build with parts list, wiring and code.')

add('electrical', 'build', 'Arduino Project Hub',
    'https://projecthub.arduino.cc/', 'start', 'doc',
    'Thousands of projects filterable by difficulty. Community-submitted, so '
    'quality varies &mdash; treat it as an index, not a curriculum.')

add('electrical', 'build', 'Build an 8-bit computer on breadboards',
    'https://eater.net/8bit', 'deeper', 'course',
    'Ben Eater. Forty-four videos and free schematics, building a working '
    'computer from logic chips by hand. The most respected breadboarding '
    'project on the internet, and a serious capstone.')

add('electrical', 'files', 'Falstad circuit simulator',
    'https://www.falstad.com/circuit/', 'start', 'tool',
    'Free, no account, runs in the browser. Animated current flow makes '
    'series and parallel visible instead of abstract. Use it constantly.')

add('electrical', 'files', 'Tinkercad Circuits',
    'https://www.tinkercad.com/circuits', 'start', 'tool',
    'Breadboard, multimeter, oscilloscope and Arduino, all simulated. Debug a '
    'build before you wire it.')

add('electrical', 'files', 'CircuitVerse',
    'https://circuitverse.org/', 'start', 'tool',
    'Free digital logic simulator for gates, truth tables and flip-flops. '
    'Account only needed to save.')

add('electrical', 'files', 'Arduino IDE',
    'https://www.arduino.cc/en/software', 'start', 'tool',
    'The real toolchain, free and open source. The desktop version needs no '
    'account.')

add('electrical', 'files', 'Resistor colour code calculator',
    'https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code',
    'start', 'tool',
    'Four, five and six band. Hosted by a parts distributor but the tool '
    'itself sells you nothing.')

add('electrical', 'files', 'Energy Explained',
    'https://www.eia.gov/energyexplained/', 'start', 'doc',
    'US Energy Information Administration. Generation, storage and delivery, '
    'plus solar, wind, hydro and geothermal, with real data behind it.')

add('electrical', 'files', 'NREL solar energy basics',
    'https://www.nrel.gov/research/re-solar.html', 'deeper', 'doc',
    'National Renewable Energy Laboratory. The correct vocabulary for '
    'photovoltaic against solar thermal against concentrating solar.')


# ==================================================================
# SOFTWARE ENGINEERING
# The notebook was 68 ISO/IEEE standards documents and university
# syllabi with three usable items. All of this is new, and weighted
# toward code that controls hardware, which is what this shop does.
# ==================================================================

add('software', 'field', 'Software developers — Occupational Outlook',
    'https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm',
    'start', 'doc',
    'Bureau of Labor Statistics. Growth here is attributed to robotics, IoT '
    'and connected devices &mdash; which is this pathway exactly.')

add('software', 'field', 'Robotics technicians — what the job involves',
    'https://www.onetonline.org/link/summary/17-3024.01', 'start', 'doc',
    'O*NET. The clearest "code that controls physical hardware" career page: '
    'microprocessors, controllers, sensor feedback, robot programming.')

add('software', 'field', '100+ computer science concepts explained',
    'https://www.youtube.com/watch?v=-uleG_Vecis', 'start', 'video',
    'Fireship. Fifteen minutes to learn the vocabulary of the whole field, '
    'so you know what to go and look up.')

add('software', 'learn', 'Boolean logic and logic gates',
    'https://www.youtube.com/watch?v=gI-qXk7XojA', 'start', 'video',
    'Crash Course Computer Science #3. Where Boolean algebra meets actual '
    'gates.')

add('software', 'learn', 'Binary and hexadecimal',
    'https://www.youtube.com/watch?v=1GSjbWt0c9M', 'start', 'video',
    'Crash Course #4. Number systems, and why hexadecimal exists at all.')

add('software', 'learn', 'Exploring how computers work',
    'https://www.youtube.com/watch?v=QZwneRb-zqA', 'start', 'video',
    'Sebastian Lague builds from one logic gate to a working computer. The '
    'best answer to "why does any of this matter".')

add('software', 'learn', 'De Morgan&rsquo;s theorems',
    'https://www.allaboutcircuits.com/textbook/digital/chpt-7/demorgans-theorems/',
    'deeper', 'doc',
    'Free textbook chapter, with every identity tied back to a gate circuit '
    'rather than left as algebra.')

add('software', 'learn', 'Karnaugh mapping',
    'https://www.allaboutcircuits.com/textbook/digital/chpt-8/introduction-to-karnaugh-mapping/',
    'deeper', 'doc',
    'Truth table to K-map to minimised expression, including don&rsquo;t-care '
    'conditions. This is the logic simplification unit.')

add('software', 'learn', 'Making logic gates from transistors',
    'https://www.youtube.com/watch?v=sTu3LwpF6XI', 'deeper', 'video',
    'Ben Eater. One level below the gate &mdash; what a gate physically is.')

add('software', 'learn', 'Introduction to CS and Programming (MIT 6.0001)',
    'https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/',
    'college', 'course',
    'Full MIT course with lectures, problem sets and code. Free, no account, '
    'downloadable for offline use.')

add('software', 'skills', 'CS50&rsquo;s Introduction to Python',
    'https://cs50.harvard.edu/python/', 'start', 'course',
    'Harvard, free. Unusually, it teaches debugging and unit testing properly '
    '&mdash; which most beginner courses skip and you will need.')

add('software', 'skills', 'Automate the Boring Stuff with Python',
    'https://automatetheboringstuff.com/', 'start', 'doc',
    'The whole book, free to read. Project-shaped: every chapter makes '
    'something do something.')

add('software', 'skills', 'Python for Everybody',
    'https://www.py4e.com/', 'start', 'course',
    'Dr Chuck at Michigan. Free textbook, lectures and exercises, and the '
    'gentlest start of the university-grade options.')

add('software', 'skills', 'Arduino course for everybody',
    'https://www.youtube.com/watch?v=DPqiIzK97K0', 'start', 'video',
    'freeCodeCamp. Ten hours, fourteen projects, IDE through sensors and '
    'motors. The closest free thing to a full firmware course.')

add('software', 'skills', 'Arduino language reference',
    'https://docs.arduino.cc/language-reference/', 'start', 'doc',
    'Every function by category &mdash; digital and analog I/O, PWM, '
    'communication, interrupts, timing. Learn to read the real docs.')

add('software', 'skills', 'I2C explained',
    'https://learn.sparkfun.com/tutorials/i2c/all', 'deeper', 'doc',
    'SDA and SCL, pull-up resistors, addressing and acknowledgement. How two '
    'chips actually talk.')

add('software', 'skills', 'SPI on a real oscilloscope trace',
    'https://www.youtube.com/watch?v=MCi7dCBhVpQ', 'deeper', 'video',
    'Ben Eater shows the protocol on an actual scope &mdash; which is exactly '
    'how you verify your own bus when it misbehaves.')

add('software', 'skills', 'PLC programming for beginners',
    'https://www.youtube.com/watch?v=y2eWdLk0-Ho', 'start', 'video',
    'RealPars. Their YouTube library is free and is the best video route into '
    'ladder logic. Their website courses are paid &mdash; stay on YouTube.')

add('software', 'skills', 'Ladder logic tutorial',
    'https://www.plcacademy.com/ladder-logic-tutorial/', 'start', 'doc',
    'Rungs, contacts, coils, the seal-in start/stop circuit, and how the scan '
    'cycle works. Free to read, no login. The best written starting point.')

add('software', 'skills', 'Understanding ladder logic',
    'https://library.automationdirect.com/understanding-ladder-logic/',
    'deeper', 'doc',
    'Written by a PLC manufacturer: relay history, scan order, and the six '
    'instruction families, ending in free exercises.')

add('software', 'build', 'Hackster and Arduino Project Hub',
    'https://projecthub.arduino.cc/', 'start', 'doc',
    'Thousands of hardware projects with wiring and code, filterable by '
    'difficulty. Free to browse.')

add('software', 'build', 'Adafruit CircuitPython',
    'https://learn.adafruit.com/welcome-to-circuitpython', 'start', 'doc',
    'Python on a microcontroller. Edit one file, save, it runs &mdash; the '
    'shortest path from language to hardware.')

add('software', 'build', 'SparkFun tutorials',
    'https://learn.sparkfun.com/tutorials', 'start', 'doc',
    'Nine hundred-plus free tutorials across Arduino, ESP32, sensors and '
    'robotics. No login.')

add('software', 'build', 'Nand2Tetris',
    'https://www.nand2tetris.org/', 'college', 'course',
    'Build a working computer starting from NAND gates, then write the '
    'software stack on top of it. Free, with simulator tools. Ambitious, and '
    'a genuine capstone.')

add('software', 'files', 'Python Tutor',
    'https://pythontutor.com/', 'start', 'tool',
    'Steps through your code line by line and draws what memory is doing. The '
    'best free tool for actually learning to debug rather than guess.')

add('software', 'files', 'Thonny',
    'https://thonny.org/', 'start', 'tool',
    'A beginner Python editor that bundles Python, has a real step debugger, '
    'and talks to MicroPython boards. From the University of Tartu.')

add('software', 'files', 'Flowgorithm',
    'https://www.flowgorithm.org/', 'start', 'tool',
    'Draw a flowchart and then run it, then convert it to Python or C++. '
    'Turns the flowcharting requirement into something executable.')

add('software', 'files', 'Wokwi',
    'https://wokwi.com/', 'start', 'tool',
    'Browser simulator for Arduino, ESP32 and Pico with real sensors and '
    'displays. Free for personal use; account only to save.')

add('software', 'files', 'OpenPLC Editor',
    'https://autonomylogic.com/', 'deeper', 'tool',
    'Free, open-source ladder logic editor that targets Arduino and Raspberry '
    'Pi &mdash; so you can run real ladder programs on the hardware you '
    'already have. Use the desktop editor.')

add('software', 'files', 'Logisim-evolution',
    'https://github.com/logisim-evolution/logisim-evolution', 'deeper', 'tool',
    'Desktop digital logic designer with timing diagrams. Offline, no '
    'account, open source.')


# ==================================================================
# PROJECT MANAGEMENT
# The notebook was NASA systems engineering handbooks plus papers on
# college freshman retention. This is entirely new. Project management
# content online is overrun by software vendors selling subscriptions,
# so every item here was checked for that specifically.
# ==================================================================

add('project', 'field', 'Project management specialists — Occupational Outlook',
    'https://www.bls.gov/ooh/business-and-financial/project-management-specialists.htm',
    'start', 'doc',
    'Bureau of Labor Statistics. Duties, pay and growth, with no one trying '
    'to sell you a certification.')

add('project', 'field', 'Construction managers — Occupational Outlook',
    'https://www.bls.gov/ooh/management/construction-managers.htm', 'start', 'doc',
    'The construction side, including an honest description of a job spent on '
    'site rather than at a desk.')

add('project', 'field', 'What project managers actually do all day',
    'https://www.onetonline.org/link/summary/13-1082.00', 'start', 'doc',
    'O*NET. Twenty concrete daily tasks and the software really used.')

add('project', 'field', 'A sixth sense for project management',
    'https://www.ted.com/talks/tres_roeder_a_sixth_sense_for_project_management',
    'start', 'talk',
    'Tres Roeder, TED. Aimed at people moving into work, and about the people '
    'side rather than the charts.')

add('project', 'learn', 'Project Management Skills for Life',
    'https://www.pmi.org/-/media/pmi/documents/public/pdf/pmief/skills-for-life-english.pdf',
    'start', 'doc',
    'The best thing found for this pathway. Sixty-two pages written for ages '
    '12 to 19 by the PMI Educational Foundation, covering the whole process '
    'with worked examples and a pack of blank templates. Free PDF, no login.')

add('project', 'learn', 'The Agile Manifesto principles',
    'https://agilemanifesto.org/principles.html', 'start', 'doc',
    'Twelve principles on one page. The original document, not somebody '
    'summarising it.')

add('project', 'learn', 'The Scrum Guide',
    'https://scrumguides.org/scrum-guide.html', 'deeper', 'doc',
    'Thirteen pages by the people who invented Scrum. Beats any second-hand '
    'explainer.')

add('project', 'learn', 'What is risk management?',
    'https://www.apm.org.uk/resources/what-is-project-management/what-is-risk-management/',
    'deeper', 'doc',
    'The UK&rsquo;s chartered body for the profession. Separates the cause, '
    'the risk event and the effect properly &mdash; which is the bit everyone '
    'gets wrong in a feasibility check.')

add('project', 'learn', 'Project management: the start of the journey',
    'https://www.open.edu/openlearn/money-business/leadership-management/project-management-the-start-the-project-journey/content-section-0',
    'deeper', 'course',
    'The Open University, free, and it ends in a statement of participation. '
    'Feasibility, life cycle, and the manager&rsquo;s actual role.')

add('project', 'learn', 'Requirements definition (MIT 16.842)',
    'https://ocw.mit.edu/courses/16-842-fundamentals-of-systems-engineering-fall-2015/pages/lecture-notes/',
    'college', 'doc',
    'Session 2 covers turning stakeholder needs into functional requirements '
    '&mdash; the hardest topic here to find taught well. Graduate level; read '
    'the one session rather than the course.')

add('project', 'skills', 'What is a work breakdown structure?',
    'https://www.youtube.com/watch?v=akO2Lf1fHmM', 'start', 'video',
    'Under five minutes, from a chartered project manager rather than a '
    'software company.')

add('project', 'skills', 'Building a WBS properly',
    'https://www.youtube.com/watch?v=PyR2VLP3xnA', 'deeper', 'video',
    'The long version: decomposition rules, how far down to go, and where '
    'people go wrong.')

add('project', 'skills', 'What is the critical path method?',
    'https://www.youtube.com/watch?v=rxGcV0tuxRU', 'start', 'video',
    'Same educator. Finding the sequence where any delay moves your end date.')

add('project', 'skills', 'Gantt chart in Google Sheets',
    'https://www.youtube.com/watch?v=JxqZ47Ilzis', 'start', 'video',
    'Built by a teacher, in a tool you already have, for nothing.')

add('project', 'skills', 'Concept selection and decision matrices',
    'https://courses.grainger.illinois.edu/me170/sp2020/Concept%20Selection.pdf',
    'deeper', 'doc',
    'University of Illinois. Two pages covering both the weighted decision '
    'matrix and Pugh convergence. Exactly the decision matrix method, done '
    'rigorously.')

add('project', 'skills', 'Specifying requirements',
    'https://www.sciencebuddies.org/science-fair-projects/engineering-design-process/engineering-design-process-steps',
    'start', 'doc',
    'Science Buddies. The clearest treatment of user needs against measurable '
    'design requirements written at this level.')

add('project', 'skills', 'Scheduling, earned value and risk (MIT ESD.36)',
    'https://ocw.mit.edu/courses/esd-36-system-project-management-fall-2012/pages/lecture-notes/',
    'college', 'doc',
    'Free lecture notes with dedicated sessions on critical path, WBS, PERT, '
    'earned value and risk. The densest free coverage of this material '
    'anywhere.')

add('project', 'build', 'Project management for CTE',
    'https://pmief.org/library/resources/project-management-for-career-and-technical-education',
    'start', 'doc',
    'Three ready-made projects built for exactly this kind of course &mdash; '
    'charter, scope, quality planning, risk, and a lessons-learned review. '
    'Free, but you need an account to download.')

add('project', 'build', 'Creative engineering design unit',
    'https://www.teachengineering.org/curricularunits/view/cub_creative_curricularunit',
    'start', 'doc',
    'Grades 9 to 12, six activities across the design process, and the '
    'challenge is yours to choose. Maps almost directly onto a capstone.')

add('project', 'build', 'Design a wooden bridge',
    'https://www.teachengineering.org/activities/ind-2472-trust-truss-design-wooden-bridge-activity',
    'deeper', 'doc',
    'Grades 11 and 12, teams of four, and material cost counts in the '
    'scoring &mdash; so it is a real Bill of Materials exercise, not a toy.')

add('project', 'build', 'Engineering ethics case files',
    'https://www.nspe.org/career-growth/ethics/board-ethical-review-cases',
    'deeper', 'doc',
    'Real adjudicated cases from the National Society of Professional '
    'Engineers, sorted by topic. What professional judgement looks like when '
    'it is tested.')

add('project', 'build', 'Write your business plan',
    'https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan',
    'start', 'doc',
    'US Small Business Administration. Two full worked plans, a one-page '
    'canvas, a startup cost worksheet and a break-even calculator. This is '
    'the Standard 11 business plan, resourced properly.')

add('project', 'files', 'GanttProject',
    'https://www.ganttproject.biz/', 'start', 'tool',
    'Free forever, open source, desktop. Does WBS, Gantt, critical path and '
    'resources offline. The download page asks for an optional contribution '
    '&mdash; the software itself costs nothing.')

add('project', 'files', 'ProjectLibre',
    'https://www.projectlibre.com/', 'deeper', 'tool',
    'The open-source equivalent of Microsoft Project. Ignore the cloud '
    'subscription they advertise; the free desktop download is the one.')

add('project', 'files', 'draw.io',
    'https://app.diagrams.net/', 'start', 'tool',
    'For WBS trees and network diagrams. Free forever, no sign-up, no '
    'account, saves to your own Drive. The cleanest tool on this page.')

add('project', 'files', 'Free Gantt chart template',
    'https://www.vertex42.com/ExcelTemplates/excel-gantt-chart.html', 'start', 'tool',
    'A Google Sheets version, free, no registration, no macros. Pairs with '
    'the Gantt video above.')

add('project', 'files', 'Quality assurance against quality control',
    'https://asq.org/quality-resources/quality-assurance-vs-control', 'deeper', 'doc',
    'The American Society for Quality&rsquo;s own definitions &mdash; the one '
    'authoritative page in a subject where everything else online is a '
    'software advert.')


# ------------------------------------------------------------------
# Deliberately excluded from these three pathways
#
#   PMI Project Management Ready    no free component at all; schools buy it
#   Google PM Certificate           "Enroll for free" routes to a paid trial;
#                                   only the buried audit link is free
#   EveryCircuit                    free tier caps you at 5 components
#   TI Precision Labs               excellent, but college level and partly
#                                   account-gated
#   TeamGantt / most CPM videos     project management software vendors
#   PLC "simulator" sites           SEO content farms with no institution
#                                   behind them
#   Code.org CS Discoveries         built for grades 6-10 and teacher-led
#   NASA design challenges          labelled grades 5-8
#   PBS Design Squad                pitched well below this age
#   bridgecontest.org               frozen since 2016
#   W3Schools                       accuracy not good enough for hardware work
#   HP LIFE                         free, but its terms-of-use page 404s so
#                                   the age requirement could not be confirmed
# ------------------------------------------------------------------


# ==================================================================
# INDUSTRIAL DESIGN — the two empty topics filled
# ==================================================================

# --- 1. Explore the Field (additions) -----------------------------
add('industrial', 'field', 'A day in the life of an industrial designer',
    'https://www.youtube.com/watch?v=f1MsHts8B80', 'start', 'video',
    'Joyce Tu describing the actual job, from a non-profit that makes career '
    'films for students.')

add('industrial', 'field', 'Industrial design inside a company',
    'https://www.youtube.com/watch?v=4RSC6dMqEMA', 'start', 'video',
    'Johnson Controls&rsquo; in-house team. A useful contrast to consultancy '
    'work &mdash; note it is made by the employer, so it is a self-portrait.')

add('industrial', 'field', 'Eric Strebel',
    'https://www.youtube.com/@EricStrebel', 'deeper', 'playlist',
    'A working industrial designer filming real client jobs &mdash; foam '
    'models, sketching, finishing, low-volume manufacturing, portfolio '
    'critique. The closest thing to shadowing someone in the trade.')

# --- 4. Find a Project --------------------------------------------
add('industrial', 'build', 'Make:able Challenge',
    'https://www.makeablechallenge.com/', 'start', 'doc',
    'Design and 3D print an assistive product for a real person with a '
    'disability or an older adult. Free, ages 14 to 18, runs to May 2027, and '
    'uses Fusion 360. A real user, real constraints, real deadline.')

add('industrial', 'build', 'NASA HUNCH design briefs',
    'https://nasahunch.com/programs/design-and-prototyping', 'deeper', 'doc',
    'Eight live 2026-27 briefs from NASA &mdash; lunar packing boxes, habitat '
    'shoes, a zero-gravity washing machine. Students prototype and present to '
    'NASA engineers. Needs a school sign-up through Mr. Frank.')

add('industrial', 'build', 'Cooper Hewitt design competition',
    'https://www.cooperhewitt.org/design-competition-design-challenge/',
    'start', 'doc',
    'The Smithsonian&rsquo;s national design museum runs this for grades 9 to '
    '12, individually or in threes. Entries open each January &mdash; watch '
    'this page.')

add('industrial', 'build', 'Design an ergonomic product',
    'https://education.theiet.org/secondary/teaching-resources/designing-an-ergonomic-product/',
    'start', 'doc',
    'Institution of Engineering and Technology. A complete brief: a carrier '
    'for shoppers over 60, sized using real anthropometric data. This is the '
    'user-centred design unit as a buildable project.')

add('industrial', 'build', 'Instructables contests',
    'https://www.instructables.com/contest/', 'start', 'doc',
    'Real judged contests with deadlines and prizes, including toys and games. '
    'Judging weights documentation and photography, so it pushes the '
    'presentation side. Free account needed to enter.')

add('industrial', 'build', '3D printing class projects',
    'https://www.instructables.com/class/3D-Printing-Class/', 'deeper', 'course',
    'Seventeen lessons ending in three complete builds &mdash; a wax seal '
    'stamp, a bottle lock with working joints, a multi-part bike fender. '
    'Covers fit tests, supports and finishing. Autodesk-owned.')

add('industrial', 'build', 'Lemelson-MIT InvenTeams',
    'https://lemelson.mit.edu/inventeams', 'deeper', 'doc',
    'A grant plus a year of MIT mentoring for a high school team inventing a '
    'solution to a community problem. Ambitious, and it has run for 23 years.')

# --- 5. Get the Files ---------------------------------------------
add('industrial', 'skills', 'Stratasys Academy — J5 Series training',
    'https://support.stratasys.com/en/Welcome/Training/PolyJet/J5-Series',
    'start', 'course',
    'The manufacturer’s own training for the J55 in our Makerspace. Four tracks: '
    'Getting Started, Operating, Designing, Post-Processing. The Designing track is '
    'design for additive manufacturing in general and transfers to any printer.')

add('industrial', 'files', 'Blender',
    'https://www.blender.org/', 'deeper', 'tool',
    'Free and open source forever. Real ray-traced product renders, and it '
    'reads Poly Haven and ambientCG assets natively. This is how a student '
    'render stops looking like a render.')

add('industrial', 'files', 'Inkscape',
    'https://inkscape.org/', 'start', 'tool',
    'Free open-source vector editor, and it exports clean SVG and DXF for the '
    'laser cutter.')

add('industrial', 'files', 'ambientCG',
    'https://ambientcg.com/', 'start', 'tool',
    'Public-domain PBR textures up to 8K, plus HDRI skies. No account, no '
    'licence worries. Sits alongside Poly Haven.')

add('industrial', 'files', 'NASA 3D resources',
    'https://science.nasa.gov/3d-resources/', 'start', 'tool',
    'Free models, printable models and textures, no account needed. Also '
    'Blender rendering tutorials.')

add('industrial', 'files', 'PureRef',
    'https://www.pureref.com/', 'start', 'tool',
    'A mood board that floats above everything else on screen. Drag images in, '
    'arrange, annotate. Pay-what-you-want, and zero is a real option.')

add('industrial', 'files', 'Coolors',
    'https://coolors.co/', 'start', 'tool',
    'Palette generator with a contrast checker and image colour picker. Works '
    'without an account; the free tier is five colours a palette, which is '
    'plenty.')

add('industrial', 'files', 'Google Fonts',
    'https://fonts.google.com/', 'start', 'tool',
    'Open-licensed typefaces for boards, product graphics and your portfolio. '
    'No account, no cost.')

add('industrial', 'files', 'DINED anthropometric database',
    'https://dined.io.tudelft.nl/en/database/tool', 'deeper', 'tool',
    'TU Delft. Over a hundred body measurements &mdash; reach, grip, seated '
    'and standing dimensions, joint mobility &mdash; across populations '
    'including children and older adults. The best free ergonomics tool there '
    'is. Some datasets need a free account.')

add('industrial', 'files', 'US anthropometric reference data',
    'https://www.cdc.gov/nchs/data/series/sr_03/sr03-050.pdf', 'deeper', 'doc',
    'CDC, 2021 to 2023. Current American percentile tables from the 5th to the '
    '95th, by sex and age. Use it with DINED so you are sizing for the people '
    'who will actually hold the thing.')

add('industrial', 'files', 'NASA Man-Systems Integration Standards',
    'https://msis.jsc.nasa.gov/', 'college', 'doc',
    'Reach envelopes, anthropometry, controls and workstation layout &mdash; '
    'and unusually readable for a standards document. Officially superseded, '
    'so read it as a reference rather than a live requirement.')


# ==================================================================
# MECHANICAL — the empty Get the Files topic, plus approachable
# additions to Learn the Concepts
# ==================================================================

add('mechanical', 'learn', 'The design of the aluminium drink can',
    'https://www.youtube.com/watch?v=hUhisi2FBuw', 'start', 'video',
    'engineerguy. A university professor unpacking thin-wall forming, '
    'pressure and material economy in an object you have held a thousand '
    'times. No maths needed.')

add('mechanical', 'learn', 'Gears explained',
    'https://www.youtube.com/watch?v=4ROtKKuSaBI', 'start', 'video',
    'The Engineering Mindset. Gear types and ratios, animated, before you go '
    'anywhere near involute geometry.')

add('mechanical', 'learn', 'Understanding GD&amp;T',
    'https://www.youtube.com/watch?v=G7wnGeR_69k', 'deeper', 'video',
    'The Efficient Engineer. The best free explanation of geometric '
    'dimensioning and tolerancing, and the bridge between a drawing and a '
    'fits table.')

add('mechanical', 'learn', 'Understanding stresses in beams',
    'https://www.youtube.com/watch?v=f08Y39UiC-o', 'deeper', 'video',
    'Bending, shear and where a beam actually fails. Watch before using any '
    'beam calculator.')

add('mechanical', 'files', 'The Engineering ToolBox',
    'https://www.engineeringtoolbox.com/', 'start', 'tool',
    'Twenty-five categories of tables and live calculators &mdash; Young&rsquo;s '
    'modulus, friction coefficients, beam dimensions, thermal properties, unit '
    'conversion. Free, no account. You will use this constantly.')

add('mechanical', 'files', 'Cantilever beam calculator',
    'https://www.engineeringtoolbox.com/cantilever-beams-d_1848.html',
    'start', 'tool',
    'Deflection and stress formulas for point, uniform and triangular loads, '
    'with the calculator right there and a worked steel example.')

add('mechanical', 'files', 'Gear ratio calculator',
    'https://www.omnicalculator.com/physics/gear-ratio', 'start', 'tool',
    'Ratio from tooth counts, plus output speed, torque and mechanical '
    'advantage. Exactly the Standard 7 calculation.')

add('mechanical', 'files', 'MakeItFrom materials database',
    'https://www.makeitfrom.com/', 'deeper', 'tool',
    'Material properties built for comparison rather than datasheet dumping '
    '&mdash; search by property value and put two materials side by side.')

add('mechanical', 'files', 'Fastener reference charts',
    'https://www.boltdepot.com/fastener-information/', 'start', 'doc',
    'Type charts, how to measure a fastener, materials and grades, tap and '
    'drill tables &mdash; and free printable to-scale sizing charts to pin up '
    'in the shop. A supplier&rsquo;s site, but the reference is genuinely good.')

add('mechanical', 'files', 'Fastener property tables',
    'https://www.fastenal.com/content/merch_rules/images/fcom/content-library/Fastener%20Reference%20Guide.pdf',
    'deeper', 'doc',
    'Mechanical properties for metric and inch grades, stainless, socket head '
    'cap screws, matching nuts and washers. Supplier-published, no torque '
    'tables &mdash; pair it with Bolt Depot.')

add('mechanical', 'files', 'ISO limits and fits calculator',
    'https://xometry.pro/en-eu/tools/iso-286-limits-and-fits-calculator/',
    'deeper', 'tool',
    'Type in a fit like 25 H7/g6 and get the actual hole and shaft sizes and '
    'the clearance range. This is what a tolerance callout on your drawing '
    'really means. Vendor-hosted, but the tool sells you nothing.')

add('mechanical', 'files', 'Elements of metric gear technology',
    'https://sdp-si.com/resources/elements-of-metric-gear-technology/index.php',
    'college', 'doc',
    'Twenty-one sections covering spur, helical, bevel and worm gears, contact '
    'ratio, backlash, forces and strength. Effectively a free gear textbook.')

add('mechanical', 'files', 'Beam calculator',
    'https://skyciv.com/free-beam-calculator/', 'deeper', 'tool',
    'Reactions, shear and bending moment diagrams, deflection and stress. The '
    'free version handles ordinary problems; the paid tier adds code checks '
    'you do not need.')

add('mechanical', 'files', 'McMaster-Carr CAD models',
    'https://www.mcmaster.com/', 'deeper', 'tool',
    'Downloadable models for essentially every fastener, bearing and bracket '
    'made. The fastest way to fill an assembly with real parts instead of '
    'ones you drew yourself.')

add('mechanical', 'files', 'GrabCAD library',
    'https://grabcad.com/', 'deeper', 'tool',
    'Millions of shared CAD models. Free account needed to download.')
