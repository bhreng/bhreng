# -*- coding: utf-8 -*-
"""The two instructors.

Not biography pages. The question a student actually has is "which one of them
do I go to with this?", and the answer is not "whoever teaches your grade" --
both work with all four years. So each page answers three things: what this
instructor covers, which grades he delivers, and what a good question for him
looks like.

The axis names (EDF / ESEC) and the two lists of what each covers are from the
shop's own framing, already used on the EDF-and-ESEC poster. Pathway leads come
from build_hubs, so if a pathway changes hands the page follows automatically.
"""

STAFF = [
    dict(
        key='frank', name='Mr. Frank', role='Lead Teacher',
        axis='EDF', axis_full='Engineering Design &amp; Fabrication',
        grades=[11, 12],
        tone='#6b4785', tone_dark='#b191c6',
        soft='#f1ebf7', soft_dark='#2b2536',
        blurb='Turning an idea into a thing that exists, and making it hold up.',
        covers=[
            'Designing in CAD so it works and looks right',
            'Getting a part ready to print or cut',
            'Structures that carry load',
            'Drawings someone else could build from',
            'Fixing a prototype that came out wrong',
        ],
        ask=[
            ('My model will not do the thing I want',
             'Bring the file, not a description of the file.'),
            ('This came off the printer wrong',
             'Bring the print and the settings you used.'),
            ('Will this actually hold?',
             'Bring the load you think it has to take, even if you guessed it.'),
            ('I need a drawing someone can build from',
             'Bring the model and who is going to build it.'),
        ],
        also='Certiport proctor for the shop, so the certification exams run '
             'through him.',
    ),
    dict(
        key='dryer', name='Mr. Dryer', role='Instructor',
        axis='ESEC', axis_full='Engineering Systems &amp; Emerging Concepts',
        grades=[9, 10],
        tone='#1f5f9e', tone_dark='#7fb2e0',
        soft='#e7f0f8', soft_dark='#122230',
        blurb='The invisible half &mdash; the code and the circuits that make '
              'something decide what to do.',
        covers=[
            'Designing or troubleshooting a circuit',
            'Writing and debugging code for a board or robot',
            'Working out why a system misbehaves',
            'Getting sensors and motors working together',
            'Proving with data that it does what you claim',
        ],
        ask=[
            ('My circuit does nothing',
             'Bring the board wired up as it is, not tidied first.'),
            ('The code runs but the robot does the wrong thing',
             'Bring the code and what you expected it to do.'),
            ('It works sometimes',
             'Bring what is different between the times it works and the times '
             'it does not.'),
            ('How do I prove this actually works?',
             'Bring the measurement you took, or the fact that you have not '
             'taken one yet.'),
        ],
        also='',
    ),
]


def by_key(k):
    for s in STAFF:
        if s['key'] == k:
            return s
    raise KeyError(k)
