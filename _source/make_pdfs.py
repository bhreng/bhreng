from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

ACCENT = HexColor('#14607f')
INK    = HexColor('#141c26')
INK2   = HexColor('#3f4e5d')
INK3   = HexColor('#6d7c8a')
RULE   = HexColor('#c3d0da')
SOFT   = HexColor('#e2eef4')
PAPER  = HexColor('#f4f7f9')

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(name=name, fontName='Helvetica', fontSize=10.5, leading=15,
                textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(**base)

st_intro   = S('intro', fontSize=11, leading=16.5, textColor=INK2, spaceAfter=14)
st_rule    = S('rule', fontSize=10.5, leading=14.5)
st_rulen   = S('rulen', fontName='Helvetica-Bold', fontSize=11, textColor=ACCENT,
               leading=14.5)
st_h2      = S('h2', fontName='Helvetica-Bold', fontSize=12, textColor=INK,
               leading=15, spaceAfter=4)
st_note    = S('note', fontSize=9.4, leading=13, textColor=INK2)
st_close   = S('close', fontName='Helvetica-Oblique', fontSize=10, leading=14.5,
               textColor=INK2)
st_cell    = S('cell', fontSize=9.0, leading=11.9)
st_cellb   = S('cellb', fontName='Helvetica-Bold', fontSize=9.0, leading=11.9)
st_th      = S('th', fontName='Helvetica-Bold', fontSize=8, textColor=INK3,
               leading=11)
st_foot    = S('foot', fontSize=8.5, leading=12, textColor=INK3)


def header_footer(title, subtitle):
    def draw(canvas, doc):
        canvas.saveState()
        # top rule + wordmark
        canvas.setFillColor(ACCENT)
        canvas.setFont('Helvetica-Bold', 8)
        canvas.drawString(MARGIN, PAGE_H - MARGIN + 26,
                          'BHR ENGINEERING TECHNOLOGY')
        canvas.setFillColor(INK3)
        canvas.setFont('Helvetica', 8)
        canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 26,
                               'Blue Hills Regional  ·  Room E-126')
        canvas.setStrokeColor(INK)
        canvas.setLineWidth(1.2)
        canvas.line(MARGIN, PAGE_H - MARGIN + 19, PAGE_W - MARGIN,
                    PAGE_H - MARGIN + 19)
        # title block
        canvas.setFillColor(INK)
        canvas.setFont('Helvetica-Bold', 21)
        canvas.drawString(MARGIN, PAGE_H - MARGIN - 8, title)
        canvas.setFillColor(INK2)
        canvas.setFont('Helvetica', 10.5)
        canvas.drawString(MARGIN, PAGE_H - MARGIN - 25, subtitle)
        # footer
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN, MARGIN - 14, PAGE_W - MARGIN, MARGIN - 14)
        canvas.setFillColor(INK3)
        canvas.setFont('Helvetica', 7.8)
        canvas.drawString(MARGIN, MARGIN - 26, subtitle)
        canvas.drawRightString(PAGE_W - MARGIN, MARGIN - 26,
                               'Page %d' % canvas.getPageNumber())
        canvas.restoreState()
    return draw


def build(path, title, subtitle, story):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN + 40, bottomMargin=MARGIN - 2,
                          title=title, author='BHR Engineering Technology')
    frame = Frame(MARGIN, MARGIN - 2,
                  PAGE_W - 2 * MARGIN, PAGE_H - (MARGIN + 40) - (MARGIN - 2),
                  id='body', leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame],
                                       onPage=header_footer(title, subtitle))])
    doc.build(story)


# ================================================================ RULES
rules = [
    "Cell phones during break and lunch only. Headphones are allowed <b>occasionally</b> "
    "while working on individual projects.",
    "Appropriate uniform, attire, and PPE are required and are part of your weekly grade. "
    "Maintain a professional workspace and use professional language and behavior.",
    "No eating or drinking in shop common areas.",
    "<b>Respect</b> your teacher and classmates &mdash; which includes their property, "
    "their space, and their creativity.",
    "The Engineering Lab and its equipment are used with permission. No writing, drawing "
    "or cutting on tables. Do not intentionally misuse equipment or property.",
    "Return things to their proper places after use. Clean up after <b>yourself and "
    "others</b>. Follow the end-of-day cleanup routine. This is all of our workspace, "
    "so keep it clean.",
    "<b>Stay in your assigned area.</b> Do not leave the shop without verbal permission "
    "or an e-hall pass.",
    "Computers are for educational purposes. When your work is done, ask a teacher for "
    "more, help a classmate, or help the department.",
    "<b>Time.</b> Be on time for class and for deadlines. Break and end-of-day preparation "
    "don't start until the instructor grants them.",
    "Communication is key. If you have questions or concerns, it is <b>your</b> "
    "responsibility to ask before the assignment is due, so what you hand in is "
    "grade-level work.",
    "Always work to your potential. Prepare to be challenged.",
]

story = []
story.append(Paragraph(
    "In order for us to live well with each other, we need some boundaries. Rules are not "
    "to restrict us; rules are given to us to fully enjoy the privileges of education, "
    "each other, and the equipment we have been given.", st_intro))

rows = [[Paragraph(str(i + 1), st_rulen), Paragraph(r, st_rule)]
        for i, r in enumerate(rules)]
t = Table(rows, colWidths=[0.34 * inch, None], hAlign='LEFT')
t.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ('LEFTPADDING', (0, 0), (0, -1), 0),
    ('RIGHTPADDING', (1, 0), (1, -1), 0),
    ('LINEBELOW', (0, 0), (-1, -2), 0.5, RULE),
]))
story.append(t)
story.append(Spacer(1, 16))

bonus = Table([[Paragraph("Bonus rule: use common sense.", st_cellb)]],
              colWidths=[PAGE_W - 2 * MARGIN], hAlign='LEFT')
bonus.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), SOFT),
    ('TEXTCOLOR', (0, 0), (-1, -1), ACCENT),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
]))
story.append(bonus)
story.append(Spacer(1, 14))
story.append(Paragraph(
    "Some of these are privileges, and privileges are not guaranteed. Follow the rules "
    "and we keep them &mdash; here and in the shop.", st_close))

build('/tmp/outputs/BHR-Classroom-Rules.pdf',
      'Classroom Rules and Privileges',
      'BHR Engineering Technology', story)


# ============================================================== GRADING
def table(data, widths, head=True):
    t = Table(data, colWidths=widths, hAlign='LEFT', repeatRows=1 if head else 0)
    style = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, RULE),
        ('BOX', (0, 0), (-1, -1), 0.7, RULE),
    ]
    if head:
        style += [('LINEBELOW', (0, 0), (-1, 0), 1.1, RULE),
                  ('BACKGROUND', (0, 0), (-1, 0), PAPER)]
    t.setStyle(TableStyle(style))
    return t


g = []
g.append(Paragraph(
    "Your grade comes from four categories. Notice what they add up to.",
    ParagraphStyle('gi', parent=st_intro, spaceAfter=8)))

W = PAGE_W - 2 * MARGIN
rows = [[Paragraph('CATEGORY', st_th), Paragraph('WHAT IT MEASURES', st_th),
         Paragraph('WEIGHT', st_th)]]
for name, desc, wt in [
    ("Project Grade", "Individual rubrics are created for each project. Graded on "
     "productivity, creativity, accuracy, and timing.", "35%"),
    ("Weekly Grade", "Behavior and performance &mdash; safety, initiative, preparation, "
     "attitude, work ethic and productivity.", "30%"),
    ("Classwork Assignments", "Classroom exercises concerned with pacing time, staying "
     "on task, and following directions.", "15%"),
    ("Employability", "Weekly and term-based soft skills centered on recurring "
     "assignments and professionalism in the shop.", "20%"),
]:
    rows.append([Paragraph(name, st_cellb), Paragraph(desc, st_cell),
                 Paragraph('<font color="#14607f"><b>%s</b></font>' % wt, st_cell)])
g.append(table(rows, [1.5 * inch, W - 1.5 * inch - 0.85 * inch, 0.85 * inch]))
g.append(Spacer(1, 9))

note = Table([[Paragraph(
    "<b>Half your grade is how you work, not what you make.</b> Weekly Grade and "
    "Employability together come to 50%. You can build something impressive and still "
    "not do well; a project can go wrong and you can still have a strong term. That is "
    "how you would be judged in an actual shop.", st_note)]],
    colWidths=[W], hAlign='LEFT')
note.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), SOFT),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
]))
g.append(note)
g.append(Spacer(1, 14))

g.append(Paragraph("The Weekly Grade", st_h2))
g.append(Paragraph(
    "Six criteria in two groups, assessed every week. This is what excellent looks like.",
    ParagraphStyle('gi2', parent=st_intro, spaceAfter=8)))

rows = [[Paragraph('', st_th), Paragraph('CRITERIA', st_th),
         Paragraph('THE STANDARD', st_th)]]
beh = [
    ("Safety", "Follows all safety rules, maintains a clean work area, and returns all "
     "materials to the proper place upon completing a task."),
    ("Initiative", "Stays on task, seeks additional work, offers assistance to peers, "
     "comes for help when needed, uses downtime effectively between jobs."),
    ("Preparation", "On time to class, agenda present, written instrument present, "
     "dressed to shop standards and ready for work, awake and alert."),
    ("Attitude", "Demonstrates a positive attitude, interacts appropriately with others, "
     "uses appropriate language, maintains self-control at all times."),
]
perf = [
    ("Work Ethic", "Work reflects the student's best efforts, cooperative, demonstrates "
     "peer leadership, stays on task, self-starter, uses proper language, never is "
     "publicly critical of the work of others."),
    ("Productivity", "Provides work of the highest quality, actively looks for and "
     "suggests solutions to problems, routinely uses time well, routinely provides "
     "useful ideas when participating in group discussion."),
]
for i, (n, d) in enumerate(beh):
    rows.append([Paragraph('<b>Behavior</b>' if i == 0 else '', st_cell),
                 Paragraph(n, st_cellb), Paragraph(d, st_cell)])
for i, (n, d) in enumerate(perf):
    rows.append([Paragraph('<b>Performance</b>' if i == 0 else '', st_cell),
                 Paragraph(n, st_cellb), Paragraph(d, st_cell)])
t2 = table(rows, [1.08 * inch, 1.05 * inch, W - 2.13 * inch])
t2.setStyle(TableStyle([('LINEABOVE', (0, 5), (-1, 5), 1.0, RULE)]))
g.append(t2)
g.append(Spacer(1, 14))

g.append(Paragraph("What each level is worth", st_h2))
levels = [("Excellent", "100"), ("Good", "92"), ("Fair", "78"),
          ("Unsatisfactory", "52"), ("Poor", "28")]
st_lvl = ParagraphStyle('lvl', parent=st_cellb, fontSize=8.6, leading=11,
                        alignment=1)
st_val = ParagraphStyle('val', parent=st_cellb, fontSize=15, leading=18,
                        alignment=1, textColor=ACCENT)
rows = [[Paragraph(l, st_lvl) for l, _ in levels],
        [Paragraph(v, st_val) for _, v in levels]]
cw = (PAGE_W - 2 * MARGIN) / 5.0
lt = Table(rows, colWidths=[cw] * 5, hAlign='LEFT')
lt.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BACKGROUND', (0, 0), (-1, 0), PAPER),
    ('TOPPADDING', (0, 0), (-1, 0), 6), ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('TOPPADDING', (0, 1), (-1, 1), 8), ('BOTTOMPADDING', (0, 1), (-1, 1), 10),
    ('BOX', (0, 0), (-1, -1), 0.7, RULE),
    ('LINEBELOW', (0, 0), (-1, 0), 0.7, RULE),
    ('LINEAFTER', (0, 0), (-2, -1), 0.5, RULE),
]))
g.append(KeepTogether(lt))

build('/tmp/outputs/BHR-Grading-and-Assessment.pdf',
      'Grading & Assessment',
      'BHR Engineering Technology', g)

print("built both")
