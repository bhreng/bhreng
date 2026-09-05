# -*- coding: utf-8 -*-
"""One page: which hand-in document, and when.

Printed for the binder and the wall. This is the piece that was missing --
there were ten documents in circulation and nothing anywhere said which one
you fill in on a Monday.
"""

import os
import generation as G
import paths
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, Table, TableStyle)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'logo', 'header.png')

ACCENT = HexColor('#6b4785')          # shop purple
INK    = HexColor('#141c26')
INK2   = HexColor('#3f4e5d')
INK3   = HexColor('#6d7c8a')
RULE   = HexColor('#c3d0da')
SOFT   = HexColor('#f1ebf7')

PAGE_W, PAGE_H = letter
MARGIN = 0.7 * inch

for name, path in [
    ('DejaVu', paths.font('DejaVuSans.ttf')),
    ('DejaVu-Bold', paths.font('DejaVuSans-Bold.ttf')),
    ('DejaVu-Oblique', paths.font('DejaVuSans-Oblique.ttf')),
]:
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))
SANS = 'DejaVu' if os.path.exists(
    paths.font('DejaVuSans.ttf')) else 'Helvetica'
BOLD = SANS + '-Bold' if SANS == 'DejaVu' else 'Helvetica-Bold'
ITAL = SANS + '-Oblique' if SANS == 'DejaVu' else 'Helvetica-Oblique'


def S(name, **kw):
    base = dict(name=name, fontName=SANS, fontSize=7.8, leading=10.1,
                textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(**base)


st_intro = S('intro', fontSize=9.2, leading=12.8, textColor=INK2, spaceAfter=8)
st_h2    = S('h2', fontName=BOLD, fontSize=11.5, textColor=ACCENT, leading=14,
             spaceBefore=13, spaceAfter=5)
st_cell  = S('cell')
st_cellb = S('cellb', fontName=BOLD, fontSize=8.8)
st_when  = S('when', fontName=BOLD, fontSize=8.4, textColor=ACCENT)
st_th    = S('th', fontName=BOLD, fontSize=7.4, textColor=INK3)
st_close = S('close', fontName=ITAL, fontSize=9, leading=13.5, textColor=INK2)


def header_footer(c, doc):
    c.saveState()
    if os.path.exists(LOGO):
        c.drawImage(LOGO, MARGIN, PAGE_H - MARGIN + 20, width=22, height=22,
                    mask='auto')
    c.setFillColor(ACCENT)
    c.setFont(BOLD, 8)
    c.drawString(MARGIN + 28, PAGE_H - MARGIN + 27,
                 'BHR ENGINEERING TECHNOLOGY')
    c.setFillColor(INK3)
    c.setFont(SANS, 7.5)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 27,
                      'Blue Hills Regional  ·  Room E-126')
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.line(MARGIN, PAGE_H - MARGIN + 14, PAGE_W - MARGIN, PAGE_H - MARGIN + 14)

    c.setFillColor(INK)
    c.setFont(BOLD, 17)
    c.drawString(MARGIN, PAGE_H - MARGIN - 6, 'Which document, and when')

    c.setFillColor(INK3)
    c.setFont(SANS, 7.5)
    c.drawString(MARGIN, MARGIN - 16,
                 'BHR Engineering Technology  ·  hand-in reference  ·  ' + G.STAMP)
    c.drawRightString(PAGE_W - MARGIN, MARGIN - 16, 'Page %d' % doc.page)
    c.restoreState()


ROWS = [
    ('Daily Logbook', 'Every day',
     'Three intervals, filled in as the day goes. Highlights, roadblocks, '
     'photographs, then a synthesis and what you do next class.'),
    ('Weekly Planner', 'Monday',
     'Goals for the week, the tasks that get you there, and how long you '
     'think each will take.'),
    ('Weekly Reflection', 'Friday',
     'What actually happened against Monday’s plan, what you would '
     'improve, and a sketch of the improvement.'),
    ('Project Reflection', 'End of a project',
     'Whether the result is a fair reflection of what you can do, what the '
     'results told you to change, and what you would do differently.'),
    ('Do Now! Reflection', 'After a Do Now',
     'One skill: what it taught you, the steps you followed, where it goes '
     'next, and whether you could repeat it alone.'),
    ('Design Brief and Initial Planner', 'Starting a project',
     'Problem, design statement, criteria, constraints, goals and '
     'deliverables. The document that fixes what "finished" means.'),
    ('Mid-Project Design Review', 'Partway through a project',
     'Where you are, what is left, why this concept, and the single element '
     'most likely to fail and needing a test.'),
    ('Instructor Meeting Notes', 'After every one-on-one',
     'Follow-up, new business, what was said, and the action items with '
     'names and dates against them.'),
    ('Research Log', 'Capstone and Independent Focus',
     'A spreadsheet. One new source a day is the target; more during '
     'brainstorming and research.'),
    ('Part List', 'Any project with more than one part',
     'A spreadsheet. Every part in the design including the fasteners, what '
     'it is made of, and whether you make it or buy it.'),
    ('Order Request Form', 'When you need parts',
     'A spreadsheet. Quantity, cost, links, and the reason — the reason '
     'is the column that gets it approved.'),
    ('Project Gantt Chart', 'Projects with a schedule',
     'A spreadsheet. Break the work into tasks, then put them on a calendar '
     'to find out where two of them collide.'),
    ('Decision Matrix', 'Choosing between concepts',
     'A spreadsheet. Weighted criteria down the side, concepts across the '
     'top; the totals decide.'),
    ('Test and Measurement Log', 'Whenever you measure something',
     'A spreadsheet. Predicted, measured, and the difference — the last '
     'column is what tells you what to change.'),
    ('I/O Map and Commissioning', 'Any automated system',
     'A spreadsheet. Every input and output, what it is wired to, and the '
     'checklist you commission it against.'),
    ('Independent Focus Proposal', 'First day of a term',
     'The idea, the work, the five weeks, and what done looks like. Handed '
     'in for review before you start.'),
    ('Independent Focus Reflection', 'Last day of a term',
     'What got done, what changed, and where next term starts. Ten minutes.'),
    ('Independent Focus Record', 'End of every term',
     'One page kept in your binder: one row per term across two years.'),
]


def main(path):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN + 34, bottomMargin=MARGIN,
                          title='Which document, and when',
                          author='BHR Engineering Technology')
    frame = Frame(MARGIN, MARGIN, PAGE_W - 2 * MARGIN,
                  PAGE_H - (MARGIN + 34) - MARGIN, id='body',
                  leftPadding=0, rightPadding=0, topPadding=0,
                  bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame],
                                       onPage=header_footer)])

    story = [Paragraph(
        'Engineering runs on its paperwork, which is a dull sentence for a '
        'true thing: the record is what lets you defend the work later. '
        'This page says which document you are filling in, and when.',
        st_intro)]

    data = [[Paragraph('Document', st_th), Paragraph('When', st_th),
             Paragraph('What it asks for', st_th)]]
    for name, when, what in ROWS:
        data.append([Paragraph(name, st_cellb), Paragraph(when, st_when),
                     Paragraph(what, st_cell)])

    t = Table(data, colWidths=[1.75 * inch, 1.45 * inch, None],
              hAlign='LEFT', repeatRows=1)
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.7),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 0), (-1, 0), SOFT),
        ('LINEBELOW', (0, 0), (-1, 0), 1.1, RULE),
        ('LINEBELOW', (0, 1), (-1, -2), 0.5, RULE),
        ('BOX', (0, 0), (-1, -1), 0.7, RULE),
    ]))
    story.append(t)
    story.append(Spacer(1, 7))

    note = Table([[Paragraph(
        'The Daily Logbook replaces both the old Logbook Template and the '
        'Engineering Daily Journal. They were the same document under two '
        'names and were being handed out at the same time. There is one now.',
        st_cellb)]], colWidths=[PAGE_W - 2 * MARGIN], hAlign='LEFT')
    note.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SOFT),
        ('TEXTCOLOR', (0, 0), (-1, -1), ACCENT),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 11),
        ('RIGHTPADDING', (0, 0), (-1, -1), 11),
    ]))
    story.append(note)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        'If a document asks you something you cannot answer, that is worth '
        'saying out loud rather than leaving blank. A gap you can explain is '
        'information; a gap you cannot is just a gap.', st_close))

    doc.build(story)
    return path


if __name__ == '__main__':
    p = main(os.path.join(HERE, 'student-docs',
                          'BHR27-Which-Document-When.pdf'))
    print(p, os.path.getsize(p), 'bytes')
