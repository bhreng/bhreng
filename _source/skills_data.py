#!/usr/bin/env python3
"""
The Skill Library — what used to be "Do Now!" assignments.

A Do Now is a short, supplemental skill module Mr. Frank inserts mid-project
when he sees a skill that needs work. Stored as dated Classroom assignments
they copied forward every year and became unfindable. Here each one is a
permanent entry with a stable address, so a Classroom post is one line and a
link rather than a new assignment.

Entries are tagged twice, because they serve two places:
  tool   the software or platform it is about
  paths  which Engineering Pathways it belongs in, under "Build Your Skills"

status:
  live      currently in use; students see it
  retired   kept for the record, hidden from students

INVENTORY NOTE — September 2026
Titles below were captured from the two most recent archived classes
(Engineering III Class 27, Engineering IV Class 26). Where the original
title named its topic, `tool` is filled in from that title. Where the title
was only a date, the topic is unknown until the assignment is opened.

`what` is deliberately EMPTY on every entry that has not been read. Do not
guess it — the description, the video link and the reflection prompt all
come out of the original assignment. `needs_content=True` marks those.
"""

S = []


def add(**kw):
    kw.setdefault('status', 'live')
    kw.setdefault('what', '')
    kw.setdefault('link', '')
    kw.setdefault('mins', '')
    kw.setdefault('reflection', False)
    kw.setdefault('paths', [])
    kw.setdefault('tool', '')
    kw.setdefault('needs_content', not kw.get('what'))
    S.append(kw)


# ------------------------------------------------------------------
# Topic identifiable from the original title
# ------------------------------------------------------------------

add(id='forma-1', title='Autodesk Forma — first pass',
    tool='Autodesk Forma', paths=['architecture'],
    source=['Do Now! 11/21 Forma #1 (Eng III)', 'Do Now! - 1/21 Forma #1 (Eng IV)'])

add(id='forma-2', title='Autodesk Forma — second pass',
    tool='Autodesk Forma', paths=['architecture'],
    source=['Do Now! - 3/2 Forma #2 (Eng III)', 'Do Now! 11/21 Forma #2 (Eng IV)'])

add(id='forma-tools', title='Forma — the new design tools',
    tool='Autodesk Forma', paths=['architecture'],
    source=['Do Now! 4/7 - New Forma Design tools (Eng III)'])

add(id='adobe-neo', title='Adobe Neo',
    tool='Adobe Neo', paths=['industrial'],
    source=['Do Now! 3/23 - Adobe Neo (Eng III)'])

add(id='coreldraw-logo', title='CorelDraw — shop logo',
    tool='CorelDraw', paths=['industrial'],
    source=['Do Now! - CorelDraw Shop Logo (Eng IV, draft)'])

add(id='brilliant', title='Brilliant — logic warm-up',
    tool='Brilliant', paths=['software', 'mechanical', 'electrical', 'project'],
    reflection=True,
    source=['Do (Brilliant) Now! - w/ reflection - 2/9 (Eng III)'])

add(id='ai-capstone', title='Using AI on your capstone',
    tool='AI tools', paths=['project'],
    source=['Do Now! - AI Help for Capstone (Eng III)'])

add(id='house-plans', title='Recreate a set of house plans',
    tool='CAD', paths=['architecture'],
    source=['Do Now! - Recreate House plans (Eng III)'])

add(id='is-log', title='Monday morning focus log',
    tool='', paths=['project'],
    source=['Do Now! - Monday Morning Independent Study Log (Eng III)'])

# ------------------------------------------------------------------
# Date-only titles — topic unknown until opened.
# Listed so the harvest has a checklist and nothing gets missed.
# ------------------------------------------------------------------

UNREAD = [
    # Engineering III — Class 27
    'Do Now! 5/27 (with included reflection)',
    'Do Now! 3/3 (with included reflection)',
    'Do Now! 1/12 (with included reflection)',
    'Do Now! 12/2',
    'Do Now! 12/1 (with included reflection)',
    'Do Now! 11/3 (with included reflection)',
    'Do Now! 3/3 (draft)',
    'Do Now! 1/27 (draft)',
    'Do Now! 10/12 (draft)',
    'Do Now! 11/9 (draft)',
    'Do Now! 11/10 (draft)',
    'Do Now! (draft, untitled)',
    # Engineering IV — Class 26
    'Do Now! 11/14 (with included reflection)',
    'Do Now! 9/3',
    'Do Now! 9/30',
]

# Observed: most titles carry "(with included reflection)", which suggests the
# reflection is part of the standard format rather than an occasional extra.
# Confirm when the contents are read.
