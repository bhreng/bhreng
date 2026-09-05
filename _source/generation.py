# -*- coding: utf-8 -*-
"""The generation tag: one token that marks every document built this year.

Dan's habit is to put a searchable token in file names so that a Drive search
for it returns only the current forms -- "BHR ENG" did that job last year.
This year's token is TAG. It goes in every file name AND inside every document
(footer, sheet header), so that

  * a Drive search for BHR27 returns only this generation, and
  * a copy a student renamed still says which generation it came from.

Next year: change TAG and REV here, rebuild, and the whole set re-stamps.
Last year's files keep their old names and drop out of the search.
"""

import datetime

TAG = 'BHR27'                       # school year 2026-27
REV = datetime.date(2026, 9, 5)     # the date printed in every footer

REV_TEXT = REV.strftime('%d %b %Y')
STAMP = '%s · rev %s' % (TAG, REV_TEXT)      # "BHR27 · rev 05 Sep 2026"


def fname(stem, ext):
    """'Daily-Logbook', 'docx' -> 'BHR27-Daily-Logbook.docx'"""
    return '%s-%s.%s' % (TAG, stem, ext)


def title(name):
    """'Daily Logbook' -> 'BHR27 · Daily Logbook' (for document names)"""
    return '%s · %s' % (TAG, name)
