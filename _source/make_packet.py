from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether,
                                NextPageTemplate, PageBreak)

# ---- shop purple, school blue & green -------------------------------------
PURPLE   = HexColor('#5c3d8f')
PURPLE_D = HexColor('#3d2861')
PURPLE_S = HexColor('#efeaf7')
BLUE     = HexColor('#1f5f9e')
GREEN    = HexColor('#3d7a4e')
INK      = HexColor('#191622')
INK2     = HexColor('#474155')
INK3     = HexColor('#78718a')
RULE     = HexColor('#cdc6db')
PAPER    = HexColor('#f6f4fa')

PAGE_W, PAGE_H = letter
M = 0.75 * inch


def S(name, **kw):
    b = dict(name=name, fontName='Helvetica', fontSize=10, leading=14,
             textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    b.update(kw)
    return ParagraphStyle(**b)


st_body   = S('body', fontSize=10, leading=14.2)
st_lead   = S('lead', fontSize=11, leading=16, textColor=INK2, spaceAfter=11)
st_h2     = S('h2', fontName='Helvetica-Bold', fontSize=14.5, textColor=INK,
              leading=18, spaceAfter=6)
st_h3     = S('h3', fontName='Helvetica-Bold', fontSize=11, textColor=PURPLE,
              leading=14, spaceAfter=3)
st_cell   = S('cell', fontSize=9.2, leading=12.4)
st_cellb  = S('cellb', fontName='Helvetica-Bold', fontSize=9.2, leading=12.4)
st_th     = S('th', fontName='Helvetica-Bold', fontSize=7.8, textColor=INK3, leading=10)
st_rule   = S('rule', fontSize=9.6, leading=13)
st_rulen  = S('rulen', fontName='Helvetica-Bold', fontSize=10, textColor=PURPLE,
              leading=13)
st_note   = S('note', fontSize=9.4, leading=13, textColor=INK2)
st_close  = S('close', fontName='Helvetica-Oblique', fontSize=9.6, leading=13.4,
              textColor=INK2)
st_sign   = S('sign', fontSize=9.6, leading=26)

TOP = M + 40
BOT = M - 2


def chrome(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PURPLE)
    canvas.setFont('Helvetica-Bold', 7.8)
    canvas.drawString(M, PAGE_H - M + 24, 'BHR ENGINEERING TECHNOLOGY')
    canvas.setFillColor(INK3)
    canvas.setFont('Helvetica', 7.8)
    canvas.drawRightString(PAGE_W - M, PAGE_H - M + 24,
                           'Welcome Packet  ·  Room E-126')
    canvas.setStrokeColor(PURPLE)
    canvas.setLineWidth(1.4)
    canvas.line(M, PAGE_H - M + 17, PAGE_W - M, PAGE_H - M + 17)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(M, M - 16, PAGE_W - M, M - 16)
    canvas.setFillColor(INK3)
    canvas.setFont('Helvetica', 7.6)
    canvas.drawString(M, M - 28, 'Blue Hills Regional Technical School')
    canvas.drawRightString(PAGE_W - M, M - 28, 'Page %d' % (canvas.getPageNumber() - 1))
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PURPLE)
    canvas.rect(0, PAGE_H - 3.5 * inch, PAGE_W, 3.5 * inch, stroke=0, fill=1)
    canvas.setFillColor(GREEN)
    canvas.rect(0, PAGE_H - 3.5 * inch - 9, PAGE_W, 5, stroke=0, fill=1)
    canvas.setFillColor(BLUE)
    canvas.rect(0, PAGE_H - 3.5 * inch - 16, PAGE_W, 4, stroke=0, fill=1)

    canvas.setFillColor(white)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(M, PAGE_H - 1.15 * inch, 'BLUE HILLS REGIONAL TECHNICAL SCHOOL')
    canvas.setFont('Helvetica-Bold', 40)
    canvas.drawString(M, PAGE_H - 2.05 * inch, 'Engineering')
    canvas.drawString(M, PAGE_H - 2.62 * inch, 'Technology')
    canvas.setFont('Helvetica', 15)
    canvas.drawString(M, PAGE_H - 3.08 * inch, 'Welcome Packet')

    canvas.setFillColor(INK)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(M, PAGE_H - 5.6 * inch, 'Everything you need for your first week')
    canvas.setFillColor(INK2)
    canvas.setFont('Helvetica', 10.5)
    for i, ln in enumerate([
        'Who to ask for what, what to wear, how the shop runs, and how',
        'you are graded. Keep this — the answers to most first-term',
        'questions are in here.']):
        canvas.drawString(M, PAGE_H - 5.95 * inch - i * 15, ln)

    contents = [('1', 'Welcome, who to ask, what you can earn'),
                ('2', 'What to wear, safety in short'),
                ('3', 'Classroom rules and privileges'),
                ('4', 'How you are graded'),
                ('5', 'Sign and return')]
    y = PAGE_H - 7.15 * inch
    canvas.setFillColor(INK3)
    canvas.setFont('Helvetica-Bold', 7.8)
    canvas.drawString(M, y, 'WHAT IS INSIDE')
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(M, y - 8, M + 3.4 * inch, y - 8)
    for i, (n, lbl) in enumerate(contents):
        yy = y - 25 - i * 17
        canvas.setFillColor(PURPLE)
        canvas.setFont('Helvetica-Bold', 9.5)
        canvas.drawString(M, yy, 'Page ' + n)
        canvas.setFillColor(INK2)
        canvas.setFont('Helvetica', 9.5)
        canvas.drawString(M + 0.62 * inch, yy, lbl)

    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.7)
    canvas.line(M, 1.55 * inch, PAGE_W - M, 1.55 * inch)
    canvas.setFillColor(INK3)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(M, 1.28 * inch, 'Room E-126  ·  Mr. Frank (Grades 11 & 12)  ·  Mr. Dryer (Grades 9 & 10)')
    canvas.setFont('Helvetica-Bold', 9)
    canvas.setFillColor(PURPLE)
    canvas.drawString(M, 1.05 * inch, 'store.bluehills.org  —  uniform ordering')
    canvas.restoreState()


def table(data, widths, head=True, pad=5):
    t = Table(data, colWidths=widths, hAlign='LEFT', repeatRows=1 if head else 0)
    style = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('TOPPADDING', (0, 0), (-1, -1), pad),
             ('BOTTOMPADDING', (0, 0), (-1, -1), pad),
             ('LEFTPADDING', (0, 0), (-1, -1), 8),
             ('RIGHTPADDING', (0, 0), (-1, -1), 8),
             ('LINEBELOW', (0, 0), (-1, -2), 0.5, RULE),
             ('BOX', (0, 0), (-1, -1), 0.7, RULE)]
    if head:
        style += [('LINEBELOW', (0, 0), (-1, 0), 1.0, RULE),
                  ('BACKGROUND', (0, 0), (-1, 0), PAPER)]
    t.setStyle(TableStyle(style))
    return t


def band(text, style=None, bg=PURPLE_S, tc=None):
    p = Paragraph(text, style or st_note)
    t = Table([[p]], colWidths=[PAGE_W - 2 * M], hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg),
                           ('LEFTPADDING', (0, 0), (-1, -1), 12),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                           ('TOPPADDING', (0, 0), (-1, -1), 9),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 9)]))
    return t


W = PAGE_W - 2 * M
s = []

# ---------------------------------------------------------------- page 1
s.append(NextPageTemplate('body'))
s.append(PageBreak())

s.append(Paragraph('Welcome to the shop', st_h2))
s.append(Paragraph(
    "You are joining a program that treats you like an engineer rather than a student "
    "who happens to be in a shop. You will design things, build them, test them, and "
    "explain why they worked or did not. Some of what you make will fail. That is part "
    "of it — what matters is that you can say why.", st_lead))

s.append(Paragraph('Who to ask for what', st_h2))
rows = [[Paragraph('MR. FRANK  ·  GRADES 11 & 12', st_th),
         Paragraph('MR. DRYER  ·  GRADES 9 & 10', st_th)],
        [Paragraph("<b>Helps you make it real</b> — how it looks, how it is drawn, "
                   "how it gets built.<br/><br/>"
                   "• Designing in CAD so it works and looks right<br/>"
                   "• Getting a part ready to 3D print or laser cut<br/>"
                   "• Making a structure that holds up<br/>"
                   "• Drawings someone else could build from<br/>"
                   "• Fixing a prototype that came out wrong", st_cell),
         Paragraph("<b>Helps you make it work</b> — circuits, code, and proving "
                   "it performs.<br/><br/>"
                   "• Designing or troubleshooting a circuit<br/>"
                   "• Writing and debugging code for a board or robot<br/>"
                   "• Working out why a system misbehaves<br/>"
                   "• Getting sensors and motors working together<br/>"
                   "• Showing with data that it does what you claim", st_cell)]]
s.append(table(rows, [W / 2, W / 2], pad=9))
s.append(Spacer(1, 9))
s.append(band("Both of us teach across all four years. Go to whoever fits the problem "
              "in front of you — you will not be sent away for asking the wrong one."))

s.append(Spacer(1, 16))
s.append(Paragraph('What you can earn here', st_h2))
s.append(Paragraph(
    "<b>OSHA 10 — Construction</b> in Grade 10. This is the credential that lets you "
    "work on the equipment, and it is recognized well outside this building.<br/><br/>"
    "<b>Autodesk Certified User</b> in Inventor, Fusion 360 and Revit Architecture. Which "
    "ones you go for depends on the work you are doing and when you are ready.<br/><br/>"
    "<b>Cooperative education</b> — working in a real engineering setting for part of "
    "your schedule. Available to juniors from Term 3 and seniors from Term 1.", st_body))

# ---------------------------------------------------------------- page 2
s.append(PageBreak())
s.append(Paragraph('What to wear', st_h2))
s.append(Paragraph(
    "You wear a uniform during your shop week. It is not about looking smart — it is "
    "about being dressed for a room with machines in it.", st_lead))

rows = [[Paragraph('ITEM', st_th), Paragraph('WHAT IS REQUIRED', st_th)],
        [Paragraph('Shop attire', st_cellb),
         Paragraph("Anything carrying the Engineering Technology logo, bought through the "
                   "school store — T-shirts long or short sleeve, hoodies, crew necks, "
                   "quarter-zips, sweaters. Any of it counts.", st_cell)],
        [Paragraph('Footwear', st_cellb),
         Paragraph("Shoes, sneakers or work boots. <b>No open-toed shoes, sandals or "
                   "Crocs</b> in the Makerspace.", st_cell)],
        [Paragraph('Eye protection', st_cellb),
         Paragraph("Required in the Makerspace. Situational in the main shop — if you "
                   "are unsure, put them on.", st_cell)],
        [Paragraph('Not required', st_cellb),
         Paragraph("Sweatshirts are available but optional. They carry the Blue Hills logo "
                   "on the front and the Engineering Technology logo on the back.", st_cell)]]
s.append(table(rows, [1.25 * inch, W - 1.25 * inch]))
s.append(Spacer(1, 10))
s.append(band("<b>Ordering.</b> Uniforms are ordered at <b>store.bluehills.org</b> during "
              "the window posted on the website — that is when pricing is best and "
              "delivery to the school is free. There is no limit on how many you buy; most "
              "students get at least two. Refer to the Blue Hills Parent/Student Handbook "
              "for anything else about attire."))

s.append(Spacer(1, 18))
s.append(Paragraph('Safety, in short', st_h2))
s.append(Paragraph(
    "The full rules are posted in the shop and you will be trained on them. These are the "
    "ones that matter before you touch anything.", st_lead))
safety = [
    "Report every injury immediately, however small. If a chemical gets in your eyes, "
    "wash for <b>15 minutes</b> before seeking treatment.",
    "Never use a tool you have not been trained and authorized on.",
    "Never work alone with power tools — two people, both visible to each other.",
    "Machines run only with all guards and shields in place. Never walk away from a "
    "running tool.",
    "Clean your area every time you leave it, including the floor.",
]
rows = [[Paragraph('•', st_rulen), Paragraph(x, st_rule)] for x in safety]
t = Table(rows, colWidths=[0.2 * inch, W - 0.2 * inch], hAlign='LEFT')
t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('TOPPADDING', (0, 0), (-1, -1), 4),
                       ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                       ('LEFTPADDING', (0, 0), (0, -1), 0),
                       ('RIGHTPADDING', (1, 0), (1, -1), 0)]))
s.append(t)

# ---------------------------------------------------------------- page 3
s.append(PageBreak())
s.append(Paragraph('Classroom rules and privileges', st_h2))
s.append(Paragraph(
    "In order for us to live well with each other, we need some boundaries. Rules are not "
    "to restrict us; rules are given to us to fully enjoy the privileges of education, "
    "each other, and the equipment we have been given.", st_lead))

rules = [
    "Cell phones during break and lunch only. Headphones are allowed <b>occasionally</b> "
    "while working on individual projects.",
    "Appropriate uniform, attire, and PPE are required and are part of your weekly grade. "
    "Maintain a professional workspace and use professional language and behavior.",
    "No eating or drinking in shop common areas.",
    "<b>Respect</b> your teacher and classmates — which includes their property, their "
    "space, and their creativity.",
    "The Engineering Lab and its equipment are used with permission. No writing, drawing or "
    "cutting on tables. Do not intentionally misuse equipment or property.",
    "Return things to their proper places after use. Clean up after <b>yourself and "
    "others</b>. Follow the end-of-day cleanup routine. This is all of our workspace, so "
    "keep it clean.",
    "<b>Stay in your assigned area.</b> Do not leave the shop without verbal permission or "
    "an e-hall pass.",
    "Computers are for educational purposes. When your work is done, ask a teacher for "
    "more, help a classmate, or help the department.",
    "<b>Time.</b> Be on time for class and for deadlines. Break and end-of-day preparation "
    "don't start until the instructor grants them.",
    "Communication is key. If you have questions or concerns, it is <b>your</b> "
    "responsibility to ask before the assignment is due, so what you hand in is grade-level "
    "work.",
    "Always work to your potential. Prepare to be challenged.",
]
rows = [[Paragraph(str(i + 1), st_rulen), Paragraph(r, st_rule)]
        for i, r in enumerate(rules)]
t = Table(rows, colWidths=[0.3 * inch, W - 0.3 * inch], hAlign='LEFT')
t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('TOPPADDING', (0, 0), (-1, -1), 5),
                       ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                       ('LEFTPADDING', (0, 0), (0, -1), 0),
                       ('RIGHTPADDING', (1, 0), (1, -1), 0),
                       ('LINEBELOW', (0, 0), (-1, -2), 0.4, RULE)]))
s.append(t)
s.append(Spacer(1, 10))
s.append(band("<b>Bonus rule: use common sense.</b>", st_cellb))
s.append(Spacer(1, 9))
s.append(Paragraph("Some of these are privileges, and privileges are not guaranteed. "
                   "Follow the rules and we keep them — here and in the shop.", st_close))

# ---------------------------------------------------------------- page 4
s.append(PageBreak())
s.append(Paragraph('How you are graded', st_h2))
s.append(Paragraph("Your grade comes from four categories. Notice what they add up to.",
                   st_lead))
rows = [[Paragraph('CATEGORY', st_th), Paragraph('WHAT IT MEASURES', st_th),
         Paragraph('WEIGHT', st_th)]]
for n, d, w in [
    ("Project Grade", "Individual rubrics are created for each project. Graded on "
     "productivity, creativity, accuracy, and timing.", "35%"),
    ("Weekly Grade", "Behavior and performance — safety, initiative, preparation, "
     "attitude, work ethic and productivity.", "30%"),
    ("Classwork Assignments", "Classroom exercises concerned with pacing time, staying on "
     "task, and following directions.", "15%"),
    ("Employability", "Weekly and term-based soft skills centered on recurring assignments "
     "and professionalism in the shop.", "20%")]:
    rows.append([Paragraph(n, st_cellb), Paragraph(d, st_cell),
                 Paragraph('<font color="#5c3d8f"><b>%s</b></font>' % w, st_cell)])
s.append(table(rows, [1.4 * inch, W - 2.25 * inch, 0.85 * inch]))
s.append(Spacer(1, 9))
s.append(band("<b>Half your grade is how you work, not what you make.</b> Weekly Grade and "
              "Employability come to 50% between them. You can build something impressive "
              "and still not do well; a project can go wrong and you can still have a "
              "strong term. That is how you would be judged in an actual shop."))

s.append(Spacer(1, 14))
s.append(Paragraph('The weekly grade', st_h2))
s.append(Paragraph("Six things, in two groups, assessed every week. This is what excellent "
                   "looks like.", st_lead))
rows = [[Paragraph('', st_th), Paragraph('CRITERIA', st_th),
         Paragraph('THE STANDARD', st_th)]]
beh = [("Safety", "Follows all safety rules, maintains a clean work area, returns all "
        "materials to the proper place upon completing a task."),
       ("Initiative", "Stays on task, seeks additional work, offers assistance to peers, "
        "comes for help when needed, uses downtime effectively."),
       ("Preparation", "On time, agenda present, written instrument present, dressed to "
        "shop standards, awake and alert."),
       ("Attitude", "Positive attitude, interacts appropriately, appropriate language, "
        "maintains self-control at all times.")]
perf = [("Work Ethic", "Best efforts, cooperative, peer leadership, stays on task, "
         "self-starter, never publicly critical of the work of others."),
        ("Productivity", "Work of the highest quality, suggests solutions to problems, "
         "uses time well, provides useful ideas in discussion.")]
for i, (n, d) in enumerate(beh):
    rows.append([Paragraph('<b>Behavior</b>' if i == 0 else '', st_cell),
                 Paragraph(n, st_cellb), Paragraph(d, st_cell)])
for i, (n, d) in enumerate(perf):
    rows.append([Paragraph('<b>Performance</b>' if i == 0 else '', st_cell),
                 Paragraph(n, st_cellb), Paragraph(d, st_cell)])
t = table(rows, [1.05 * inch, 1.0 * inch, W - 2.05 * inch], pad=4)
t.setStyle(TableStyle([('LINEABOVE', (0, 5), (-1, 5), 1.0, RULE)]))
s.append(t)
s.append(Spacer(1, 12))

levels = [("Excellent", "100"), ("Good", "92"), ("Fair", "78"),
          ("Unsatisfactory", "52"), ("Poor", "28")]
st_l = ParagraphStyle('l', parent=st_cellb, fontSize=8.4, leading=11, alignment=TA_CENTER)
st_v = ParagraphStyle('v', parent=st_cellb, fontSize=14, leading=17,
                      alignment=TA_CENTER, textColor=PURPLE)
lt = Table([[Paragraph(a, st_l) for a, _ in levels],
            [Paragraph(b, st_v) for _, b in levels]],
           colWidths=[W / 5.0] * 5, hAlign='LEFT')
lt.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                        ('BACKGROUND', (0, 0), (-1, 0), PAPER),
                        ('TOPPADDING', (0, 0), (-1, 0), 5),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
                        ('TOPPADDING', (0, 1), (-1, 1), 6),
                        ('BOTTOMPADDING', (0, 1), (-1, 1), 8),
                        ('BOX', (0, 0), (-1, -1), 0.7, RULE),
                        ('LINEBELOW', (0, 0), (-1, 0), 0.7, RULE),
                        ('LINEAFTER', (0, 0), (-2, -1), 0.5, RULE)]))
s.append(KeepTogether(lt))

# ---------------------------------------------------------------- page 5
s.append(PageBreak())
s.append(Paragraph('Please read, sign and return', st_h2))
s.append(Paragraph(
    "Return this page to Mr. Frank or Mr. Dryer during the first week. Keep the rest of "
    "the packet — you will want it later.", st_lead))

s.append(Paragraph('We have read and understood', st_h3))
for x in ["The classroom rules and privileges, including that some of them are privileges "
          "that can be lost.",
          "The uniform and footwear requirements, and how to order through the school store.",
          "The safety expectations, including that no tool is used without training and "
          "authorization.",
          "How the grade is calculated, including that half of it reflects how a student "
          "works."]:
    cb = Table([['']], colWidths=[9.5], rowHeights=[9.5])
    cb.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.8, PURPLE),
                            ('LEFTPADDING', (0, 0), (-1, -1), 0),
                            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                            ('TOPPADDING', (0, 0), (-1, -1), 0),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    row = Table([[cb, Paragraph(x, st_body)]],
                colWidths=[0.28 * inch, W - 0.28 * inch], hAlign='LEFT')
    row.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                             ('TOPPADDING', (0, 0), (0, 0), 2),
                             ('TOPPADDING', (1, 0), (1, 0), 0),
                             ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                             ('LEFTPADDING', (0, 0), (0, 0), 0),
                             ('RIGHTPADDING', (1, 0), (1, 0), 0)]))
    s.append(row)
    s.append(Spacer(1, 8))

s.append(Spacer(1, 16))
line = '<font color="#cdc6db">' + '_' * 58 + '</font>'
rows = [[Paragraph('Student name (printed)', st_th), Paragraph('Grade', st_th)],
        [Paragraph(line, st_sign), Paragraph('<font color="#cdc6db">______</font>', st_sign)],
        [Paragraph('Student signature', st_th), Paragraph('Date', st_th)],
        [Paragraph(line, st_sign), Paragraph('<font color="#cdc6db">__________</font>', st_sign)],
        [Paragraph('Parent or guardian signature', st_th), Paragraph('Date', st_th)],
        [Paragraph(line, st_sign), Paragraph('<font color="#cdc6db">__________</font>', st_sign)]]
t = Table(rows, colWidths=[W - 1.4 * inch, 1.4 * inch], hAlign='LEFT')
t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
                       ('TOPPADDING', (0, 0), (-1, -1), 2),
                       ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                       ('LEFTPADDING', (0, 0), (-1, -1), 0)]))
s.append(t)
s.append(Spacer(1, 20))
s.append(band("<b>Questions?</b> Ask either of us before the assignment is due, not after. "
              "That is rule ten, and it is the one that saves the most grades."))

# ---------------------------------------------------------------- build
doc = BaseDocTemplate('/tmp/outputs/BHR-Engineering-Welcome-Packet.pdf',
                      pagesize=letter, leftMargin=M, rightMargin=M,
                      topMargin=TOP, bottomMargin=BOT,
                      title='BHR Engineering Technology — Welcome Packet',
                      author='Blue Hills Regional Technical School')
full = Frame(M, BOT, PAGE_W - 2 * M, PAGE_H - TOP - BOT, id='f',
             leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
cvr = Frame(M, M, PAGE_W - 2 * M, PAGE_H - 2 * M, id='c')
doc.addPageTemplates([PageTemplate(id='cover', frames=[cvr], onPage=cover),
                      PageTemplate(id='body', frames=[full], onPage=chrome)])
doc.build(s)
print('built')
