# -*- coding: utf-8 -*-
"""The four grade homes.

The organising split is by GRADE, not by teacher. Both instructors work with
every student; the grade is who delivers the assignments and owns the
gradebook. So the site says "Grade 11" first and "Mr. Frank" second.

  9  and 10  -> Mr. Dryer
  11 and 12  -> Mr. Frank

Grades 9 and 10 deliberately carry only the unit map. Mr. Dryer sets those up
himself, and a half-filled page written by someone else is worse than an
honest empty one.

Colours come from Dan's own Google Classroom banners, sampled from the images:
grade 9 red, grade 10 gold, grade 11 green, grade 12 purple. Each has a dark
variant chosen to clear 4.5:1 on the dark paper.

Unit names are quoted from the four Drive documents
"BHR Eng - <n>th Grade - EDF Unit Breakdown". Assignment lists are harvested
from the live Google Classroom classes. Nothing here is invented.
"""

# ---------------------------------------------------------------- the grades

GRADES = [
    dict(
        key='9', num=9, course='Engineering I', teacher='Mr. Dryer',
        banner='grade-1.jpg',
        ink='#a03c36', ink_dark='#e59089', soft='#fbeceb', soft_dark='#3a1e1c',
        lede='Grade 9 in this shop is <b>Terms 3 and 4</b>. You spend the '
             'first half of the year on exploratory, one week in each of nine '
             'shops, and you join us for the back half once you have chosen. '
             'So this is half a year, and it moves quickly.',
        exploratory=True,
        units=[
            ('Exploratory &amp; Shop Readiness',
             'What the shop is, how to be safe in it, and what engineering '
             'technology actually means as a trade.'),
            ('Intro to Digital Design &amp; CAD',
             'Your first time making something on a screen that could be made '
             'for real.'),
            ('Engineering Design &amp; Planning',
             'The design process: define the problem before you solve it.'),
            ('Graphics &amp; Documentation Basics',
             'Drawing so that someone else can build from it.'),
            ('Intro to Fabrication &amp; Prototyping',
             'Turning the file into a thing you can hold.'),
            ('Grade 9 EOY Project',
             'Everything above, in one build, at the end of the year.'),
        ],
    ),
    dict(
        key='10', num=10, course='Engineering II', teacher='Mr. Dryer',
        banner='grade-2.jpg',
        ink='#8a6410', ink_dark='#dcae4f', soft='#faf0d9', soft_dark='#332a10',
        lede='Grade 10 is where the safety certifications get real and the '
             'documentation standard goes up. You are no longer visiting.',
        exploratory=False,
        units=[
            ('Review, Safety Certification &amp; Prep',
             'Back in the shop, re-certified, before anything is switched on.'),
            ('Skill Reinforcement: Technical Documentation Mastery',
             'The notebook and the drawing set, held to a higher standard than '
             'last year.'),
            ('Safety &amp; Certification (OSHA Prep)',
             'The OSHA unit. This is the one that follows you out of school.'),
            ('Intro to Quality Assurance &amp; Testing',
             'Measuring whether it actually works, rather than assuming.'),
            ('Civil/Architectural Foundations',
             'Structures, sites, and the drawings that go with them.'),
            ('Grade 10 EOY Capstone Project',
             'The year, proved in one project.'),
        ],
    ),
    dict(
        key='11', num=11, course='Engineering III', teacher='Mr. Frank',
        banner='grade-3.jpg',
        ink='#0b622c', ink_dark='#71bd88', soft='#e9f4ec', soft_dark='#152c1c',
        lede='Grade 11 is the widest year. Projects run all four terms and '
             'cover every pathway in the shop &mdash; speakers, houses, '
             'robots, circuits, architecture &mdash; before the capstone at '
             'the end.',
        exploratory=False,
        units=[
            ('Review, Acclimation &amp; Higher Expectations Prep', ''),
            ('Roles of an Engineer &amp; Professional Management', ''),
            ('Skill Reinforcement', ''),
            ('Advanced Manufacturing &amp; DFM Theory', ''),
            ('Junior Capstone: Architectural Design', ''),
            ('Year-End Wrap-Up &amp; Portfolio Prep', ''),
        ],
    ),
    dict(
        key='12', num=12, course='Engineering IV', teacher='Mr. Frank',
        banner='grade-4.jpg',
        ink='#4a2a70', ink_dark='#b998d0', soft='#f0eaf7', soft_dark='#2b2038',
        lede='Grade 12 has a different shape from every year before it. Terms '
             '1 and 2 are a run of short, varied briefs. Terms 3 and 4 are one '
             'thing: the Senior Capstone, which you choose and run yourself.',
        exploratory=False,
        units=[
            ('Review, Career Readiness &amp; Leadership', ''),
            ('Skill Reinforcement: Shop Equipment Mastery', ''),
            ('Skill Reinforcement / Elective Exploration', ''),
            ('Senior Capstone', ''),
        ],
    ),
]


def by_key(k):
    for g in GRADES:
        if g['key'] == k:
            return g
    raise KeyError(k)
