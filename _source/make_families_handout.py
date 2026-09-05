# -*- coding: utf-8 -*-
"""The families handout: BHR Engineering, for parents and prospective students.

Deliberately NOT open-house-specific -- no "tonight", no date, nothing that
stops it being handed to a family in March. Open house is one place it gets
used; the others are eighth-grade visits, guidance meetings, and any parent
who asks what this shop is. The open-house-only material (questions to ask
on the night) lives on the website's Families page instead, where it can be
changed without reprinting anything.

Replaces the 2025 "Welcome To BHR Engineering" deck. That version was written
in framework language -- "matriculate to a competitive technical college",
"Empirical Analysis & Optimization", a numbered list of ten Essential
Concepts. That is the right register for a DESE reviewer and the wrong one
for a thirteen-year-old and their mother standing at a table with ninety
seconds to spare.

So this one is rewritten around the questions people actually ask at an open
house, in the order they ask them:

  1. What is this shop, and what do they make?
  2. What would my kid actually DO?
  3. What happens in each of the four years?
  4. What do they leave with?
  5. How does choosing it work, and is it safe?

Everything here is drawn from the same verified material as the website --
the harvested Classroom briefs, the unit breakdowns, the equipment list and
Dan's own account of how the program runs. Nothing is promised that the shop
does not do. In particular the college/career paragraph says most students go
on to college and some take a more direct route, and stops there: no claims
about what employers recognise, and no figures.

No student names, no student work, no photographs of students. No pricing.
"""

import os
import generation as G
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
import paths
GF = paths.FONTS
LOGO = os.path.join(HERE, 'logo', 'header.png')

# --- the site's palette ----------------------------------------------------
PURPLE = colors.HexColor('#6b4785')
PURPLE_D = colors.HexColor('#553669')
SOFT = colors.HexColor('#f1ebf7')
PAPER = colors.HexColor('#faf8f4')
INK = colors.HexColor('#262b39')
INK2 = colors.HexColor('#4f5566')
INK3 = colors.HexColor('#7d8394')
RULE = colors.HexColor('#dedbd5')
BLUE = colors.HexColor('#1d4e89')
GREEN = colors.HexColor('#2f6b3a')

for name, f in (('P', 'Poppins-Regular.ttf'), ('PB', 'Poppins-Bold.ttf'),
                ('PM', 'Poppins-Medium.ttf'), ('PL', 'Poppins-Light.ttf'),
                ('PI', 'Poppins-Italic.ttf')):
    pdfmetrics.registerFont(TTFont(name, os.path.join(GF, f)))
pdfmetrics.registerFont(TTFont('L', os.path.join(GF, 'Lora-Variable.ttf')))
pdfmetrics.registerFont(TTFont('LI', os.path.join(GF,
                                                  'Lora-Italic-Variable.ttf')))

from reportlab.lib.fonts import addMapping
# Lora ships here as a variable font with one instance, so <b> and <i> have
# nothing to switch to. Map the bold slots onto Poppins Bold, which is the
# face the headings already use -- emphasis inside body copy then actually
# shows up instead of silently doing nothing.
addMapping('L', 0, 0, 'L')
addMapping('L', 1, 0, 'PB')
addMapping('L', 0, 1, 'LI')
addMapping('L', 1, 1, 'PB')

M = 0.62 * inch
W = letter[0] - 2 * M

S = dict(
    h1=ParagraphStyle('h1', fontName='PB', fontSize=27, leading=29,
                      textColor=colors.white, spaceAfter=0),
    kick=ParagraphStyle('kick', fontName='PM', fontSize=8.4, leading=11,
                        textColor=colors.HexColor('#e2d6ee'),
                        spaceAfter=5),
    tag=ParagraphStyle('tag', fontName='PL', fontSize=11.4, leading=15,
                       textColor=colors.HexColor('#f0e8f7'), spaceBefore=7),
    h2=ParagraphStyle('h2', fontName='PB', fontSize=14.4, leading=17,
                      textColor=PURPLE, spaceBefore=13, spaceAfter=4),
    h3=ParagraphStyle('h3', fontName='PB', fontSize=10.4, leading=13,
                      textColor=INK, spaceBefore=7, spaceAfter=2),
    body=ParagraphStyle('body', fontName='L', fontSize=9.9, leading=14.2,
                        textColor=INK, spaceAfter=6),
    lede=ParagraphStyle('lede', fontName='L', fontSize=11.4, leading=16.4,
                        textColor=INK, spaceAfter=8),
    small=ParagraphStyle('small', fontName='L', fontSize=9.1, leading=12.8,
                         textColor=INK2, spaceAfter=4),
    it=ParagraphStyle('it', fontName='LI', fontSize=9.1, leading=12.6,
                      textColor=INK2, spaceAfter=5),
    cell=ParagraphStyle('cell', fontName='L', fontSize=8.8, leading=12,
                        textColor=INK),
    cellb=ParagraphStyle('cellb', fontName='PB', fontSize=8.8, leading=12,
                         textColor=PURPLE),
    cellh=ParagraphStyle('cellh', fontName='PB', fontSize=7.6, leading=10,
                         textColor=colors.white),
    quiet=ParagraphStyle('quiet', fontName='P', fontSize=7.6, leading=10,
                         textColor=INK3),
)


def hero(c, doc):
    """The purple band across the top of page one only."""
    c.saveState()
    c.setFillColor(PAPER)
    c.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    if doc.page == 1:
        c.setFillColor(PURPLE)
        c.rect(0, letter[1] - 2.62 * inch, letter[0], 2.62 * inch,
               fill=1, stroke=0)
        top = letter[1]
        if os.path.exists(LOGO):
            try:
                c.drawImage(LOGO, M, top - 1.02 * inch, height=0.42 * inch,
                            width=0.42 * inch, mask='auto',
                            preserveAspectRatio=True, anchor='sw')
            except Exception:
                pass
        c.setFont('PM', 8.4)
        c.setFillColor(colors.HexColor('#d9c9e8'))
        c.drawString(M + 0.56 * inch, top - 0.78 * inch,
                     'BLUE HILLS REGIONAL TECHNICAL SCHOOL')
        c.drawString(M + 0.56 * inch, top - 0.95 * inch,
                     'CANTON, MASSACHUSETTS')
        c.setFont('PB', 33)
        c.setFillColor(colors.white)
        c.drawString(M, top - 1.62 * inch, 'Engineering Technology')
        c.setFont('PL', 12.6)
        c.setFillColor(colors.HexColor('#efe6f7'))
        c.drawString(M, top - 1.96 * inch,
                     'Design it. Build it. Test it. Improve it.')
        c.setStrokeColor(colors.HexColor('#a98cc4'))
        c.setLineWidth(1)
        c.line(M, top - 2.22 * inch, M + 2.1 * inch, top - 2.22 * inch)
        c.setFont('PM', 8.6)
        c.setFillColor(colors.HexColor('#e2d6ee'))
        c.drawString(M, top - 2.44 * inch,
                     'GRADES 9\u201312  \u00b7  ROOM E-126  \u00b7  '
                     'MR. FRANK & MR. DRYER')
    # footer
    c.setFont('P', 7.4)
    c.setFillColor(INK3)
    c.drawString(M, 0.42 * inch,
                 'Blue Hills Regional Technical School  ·  '
                 'Engineering Technology  ·  Room E-126  ·  ' + G.STAMP)
    c.drawRightString(letter[0] - M, 0.42 * inch, 'Page %d of 3' % doc.page)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(M, 0.58 * inch, letter[0] - M, 0.58 * inch)
    c.restoreState()


def rule(space=8):
    t = Table([['']], colWidths=[W], rowHeights=[0.5])
    t.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), 1.1, PURPLE)]))
    return [Spacer(1, space), t, Spacer(1, space - 2)]


def kv(rows, widths, head=None, headbg=PURPLE):
    data = []
    style = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('LINEBELOW', (0, 0), (-1, -2), 0.5, RULE),
             ('TOPPADDING', (0, 0), (-1, -1), 5),
             ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
             ('LEFTPADDING', (0, 0), (-1, -1), 8),
             ('RIGHTPADDING', (0, 0), (-1, -1), 8)]
    off = 0
    if head:
        data.append([Paragraph(h.upper(), S['cellh']) for h in head])
        style += [('BACKGROUND', (0, 0), (-1, 0), headbg),
                  ('LINEBELOW', (0, 0), (-1, 0), 0, headbg)]
        off = 1
    for r in rows:
        data.append([Paragraph(r[0], S['cellb'])] +
                    [Paragraph(x, S['cell']) for x in r[1:]])
    for i in range(len(rows)):
        if i % 2 == 1:
            style.append(('BACKGROUND', (0, i + off), (-1, i + off), SOFT))
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle(style))
    return t


def bullets(items, style='body', gap=3):
    out = []
    for it in items:
        out.append(Table(
            [[Paragraph('&bull;', ParagraphStyle('b', fontName='L',
                                                 fontSize=10.5,
                                                 textColor=PURPLE)),
              Paragraph(it, S[style])]],
            colWidths=[0.19 * inch, W - 0.19 * inch]))
        out[-1].setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (0, 0), 0.5),
            ('TOPPADDING', (1, 0), (1, 0), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), gap),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0)]))
    return out


def build(path):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=M, rightMargin=M,
                          topMargin=M, bottomMargin=0.72 * inch,
                          title='BHR Engineering Technology — for families',
                          author='Blue Hills Regional Technical School')
    # ONE template, one full-height frame. Page 1 clears the purple band with
    # a spacer instead of a shorter frame -- a second template would have to
    # be switched into with NextPageTemplate, and forgetting that is exactly
    # how every page ends up starting 2.6 inches down the page.
    full = Frame(M, 0.72 * inch, W, letter[1] - M - 0.72 * inch,
                 id='full', leftPadding=0, rightPadding=0,
                 topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[full], onPage=hero)])

    F = [Spacer(1, 2.62 * inch - M + 10)]

    F += [Paragraph(
        'What your student would actually do, what they leave with, and how '
        'choosing us works.', S['lede'])]

    F += [Paragraph('So, what is it?', S['h2'])]
    F += [Paragraph(
        'Engineering Technology is the shop where students design things and '
        'then make them. A part gets drawn in professional CAD software, then '
        'printed, cut, machined or wired, and then measured against what it '
        'was supposed to do. That last step is what makes it engineering: '
        'every project ends with data, and the data is what tells a student '
        'which change to make next. Analyse, adjust, improve, measure again '
        '&mdash; that loop is the whole method.', S['body'])]
    F += [Paragraph(
        'It is not one job, either. Someone designs the part; someone works '
        'out whether it will hold; someone writes the code that moves it; '
        'someone schedules the build so it finishes on time. All of that is '
        'engineering, and it suits very different people — which is why '
        'the shop is organised around seven pathways rather than one '
        'curriculum.', S['body'])]

    F += [Spacer(1, 7)]
    F += [kv([
        ['Who teaches it',
         'Mr. Frank and Mr. Dryer. Both are in the shop with all four years; '
         'Mr. Dryer delivers Grades 9 and 10, Mr. Frank Grades 11 and 12.'],
        ['Where', 'Room E-126, plus the Makerspace next door.'],
        ['How the week runs',
         'One week in the shop — all five days, all day — then one '
         'week in academics. About twenty-five full shop days a term.'],
        ['Who it suits',
         'Students who would rather find out than be told, and who are '
         'willing to keep adjusting something in front of other people until '
         'it works.'],
    ], [1.45 * inch, W - 1.45 * inch])]

    # ---------------------------------------------------------------- page 2
    F += [Paragraph('The seven pathways', S['h2'])]
    F += [Paragraph(
        'Engineering is an enormous field, and no class can stay in one part '
        'of it for long. So alongside the regular curriculum every student '
        'picks a pathway each term and goes deep on it — the same one '
        'every term to specialise, or a different one each term to come out '
        'broad. Both are normal, and changing your mind is the point rather '
        'than a problem.', S['body'])]

    F += [Spacer(1, 4), kv([
        ['Industrial Design',
         'Form, ergonomics, and designing something for the machine that has '
         'to make it.'],
        ['Architecture &amp; Civil',
         'Structures, sites, drainage, and the construction drawings that go '
         'with them.'],
        ['Mechanical',
         'Forces, motion, materials — and testing a thing until it '
         'fails, on purpose.'],
        ['Electrical', 'Circuits, power, and measuring what is actually '
                       'happening rather than assuming.'],
        ['Software', 'Logic and code that controls something physical.'],
        ['Automation &amp; Robotics',
         'All three of the above at once. The pathway that pulls the others '
         'together.'],
        ['Project Management',
         'Scope, schedule, budget, and getting it finished. For students who '
         'want to run the project.'],
    ], [1.62 * inch, W - 1.62 * inch], head=['Pathway', 'What a term in it looks like'])]

    F += [Paragraph('Things students have actually built', S['h2'])]
    F += [Paragraph(
        'Not a wish list — these are real briefs that have been set, '
        'built and marked in this shop.', S['it'])]
    F += bullets([
        '<b>A pullback car, redesigned for a measurable improvement.</b> '
        'Baseline test it, find the real limitation, build the change, then '
        'prove the difference with data.',
        '<b>A take-apart toy car, reverse engineered.</b> Every part measured '
        'with calipers, modelled individually, then reassembled in CAD with '
        'working joints.',
        '<b>A tiny house, and an accessory dwelling unit.</b> Real '
        'constraints, real drawing sets, and a model at the end.',
        '<b>A city section designed around transit stops</b>, using the same '
        'site-analysis software urban planners use.',
        '<b>A speaker, designed and built</b> — enclosure, components, '
        'and a listening test that either works or does not.',
        '<b>A robot built and programmed to fight in a ring</b>, then an '
        'experiment sheet proving what it can and cannot push.',
        '<b>A senior capstone</b> the student chooses, plans, builds, tests '
        'and then defends in front of the room.',
    ])

    # ---------------------------------------------------------------- page 3
    F += [Paragraph('The four years', S['h2'])]
    F += [kv([
        ['Grade 9<br/><font size="7.4" color="#7d8394">Engineering I</font>',
         'A half year, Terms 3 and 4, after exploratory. First time making '
         'something on a screen that could be made for real — CAD, the '
         'design process, drawing so somebody else can build from it, and '
         'learning to be safe in a room with machines in it.'],
        ['Grade 10<br/><font size="7.4" color="#7d8394">Engineering II</font>',
         'The first full year. Documentation goes up a level, quality and '
         'testing get introduced, and <b>every student earns their OSHA 10 '
         'card</b> — which stays with them after school.'],
        ['Grade 11<br/><font size="7.4" color="#7d8394">Engineering III</font>',
         'The widest year. Projects run all four terms and cover every '
         'pathway — speakers, houses, robots, circuits, architecture '
         '— before a junior capstone at the end.'],
        ['Grade 12<br/><font size="7.4" color="#7d8394">Engineering IV</font>',
         'Two terms of short, sharp briefs, then the Senior Capstone: one '
         'project the student chooses and runs themselves, ending in a '
         'portfolio and a defence.'],
    ], [1.28 * inch, W - 1.28 * inch])]

    F += [Paragraph('What they leave with', S['h2'])]
    F += bullets([
        '<b>An OSHA 10 card</b>, earned in Grade 10, kept for life.',
        '<b>Industry certifications</b> in the software and equipment they '
        'have actually used — Autodesk certification is proctored here '
        'in the building, and the robotics, automation and 3D printing '
        'platforms each carry their own credential ladder.',
        '<b>Four years of documented work</b> — drawings, models, test '
        'data and write-ups, kept as a portfolio rather than handed in and '
        'forgotten.',
        '<b>The habit of writing it down.</b> Half the grade in this shop is '
        'how a student works, not what they make: safety, initiative, '
        'preparation, teamwork and professionalism are weighed as heavily as '
        'the project itself. That is deliberate, and it is how they would be '
        'judged in a real shop.',
    ])

    F += [Paragraph('And afterwards?', S['h2'])]
    F += [Paragraph(
        'Most students who leave this shop go on to college, and they go with '
        'four years of CAD, documentation and project work already behind '
        'them. Others decide on a more direct route into the field. The '
        'program is built so that both stay open — what a student does '
        'with it is their call, and we would rather they arrive at that '
        'decision having tried several kinds of engineering than having been '
        'told which one to want.', S['body'])]

    # ---------------------------------------------------------------- page 4
    F += [Paragraph('How choosing a shop works', S['h2'])]
    F += [Paragraph(
        'Grade 9 students do not have to decide on day one, and they get more '
        'than a glance at each option.', S['body'])]
    F += bullets([
        'Two <b>mini exploratory days</b>, one in each of the first two '
        'terms, which between them show every one of the school’s '
        'eighteen shops.',
        'From each of those days a student picks four or five shops to spend '
        '<b>a full week in</b> — nine week-long visits in all.',
        'Then they choose, and join their shop for Terms 3 and 4.',
    ])
    F += [Paragraph(
        'If your student spends their week with us, they are not sitting at '
        'the back watching. They are in the room with upperclassmen, '
        'working. From the day they walk in, it is their shop.', S['it'])]

    F += [Paragraph('Safety, plainly', S['h2'])]
    F += [Paragraph(
        'This is a room with a laser cutter, a CNC machine, power tools, '
        'heated printers and a collaborative robot in it. Nothing gets '
        'switched on by a student who has not been trained and authorised on '
        'that specific machine. Eye protection is required in the Makerspace. '
        'Closed-toe shoes always — no sandals, no Crocs. Nobody uses '
        'power tools alone. Every injury gets reported, however small.',
        S['body'])]
    F += [Paragraph(
        'Students wear shop attire carrying the Engineering Technology logo, '
        'ordered through the school store. It is not about looking smart; it '
        'is about being dressed for the room.', S['small'])]

    F += rule(10)
    F += [Paragraph(
        '<b>Come and talk to us.</b> Mr. Frank and Mr. Dryer are both in '
        'E-126, and the best thing you can do is ask a student in the room '
        'what they are building and why they chose it. They will tell you '
        'more in two minutes than this sheet manages in three pages.',
        S['body'])]

    doc.build(F)
    return path


if __name__ == '__main__':
    out = os.path.join(HERE, 'student-docs',
                       'BHR27-Welcome-Families.pdf')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
    print(out, os.path.getsize(out), 'bytes')
