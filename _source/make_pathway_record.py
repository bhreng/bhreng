# -*- coding: utf-8 -*-
"""The Independent Focus record: one page that follows a student for two years.

One row per term. Grade 11 Terms 1-4, Grade 12 Terms 1-2, and a seventh row
for the Senior Capstone whether or not it grew out of a focus term. By the
end a student can see their own shape at a glance -- three terms Architecture,
one Project Management, one Electrical, one Industrial Design -- which is a
decision history, and worth more in an interview than any single term's work.

Kept in the binder. Filled in by hand at the end of each term from the
term reflection, which is why the columns match its fields.
"""

import os
import generation as G
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
import paths
GF = paths.FONTS
for n, f in (('P', 'Poppins-Regular.ttf'), ('PB', 'Poppins-Bold.ttf'),
             ('PM', 'Poppins-Medium.ttf'), ('PL', 'Poppins-Light.ttf')):
    pdfmetrics.registerFont(TTFont(n, os.path.join(GF, f)))
pdfmetrics.registerFont(TTFont('L', os.path.join(GF, 'Lora-Variable.ttf')))
pdfmetrics.registerFont(TTFont('LI', os.path.join(GF, 'Lora-Italic-Variable.ttf')))

PURPLE = colors.HexColor('#6b4785')
SOFT = colors.HexColor('#f1ebf7')
INK = colors.HexColor('#262b39')
INK2 = colors.HexColor('#4f5566')
INK3 = colors.HexColor('#7d8394')
RULE = colors.HexColor('#cfc9d9')

W, H = letter
M = 0.55 * inch


def build(path):
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle('Independent Focus Record')

    # header band
    c.setFillColor(PURPLE)
    c.rect(0, H - 1.25 * inch, W, 1.25 * inch, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#dccfe9'))
    c.setFont('PM', 8)
    c.drawString(M, H - 0.42 * inch, 'BHR ENGINEERING TECHNOLOGY  ·  INDEPENDENT FOCUS')
    c.setFillColor(colors.white)
    c.setFont('PB', 22)
    c.drawString(M, H - 0.78 * inch, 'Your pathway record')
    c.setFont('PL', 10.5)
    c.setFillColor(colors.HexColor('#efe6f7'))
    c.drawString(M, H - 1.02 * inch,
                 'One row per term. Fill it in from your term reflection. '
                 'By graduation this page is the shape of what you chose.')

    # identity
    y = H - 1.62 * inch
    c.setFont('PB', 8.5); c.setFillColor(INK)
    c.drawString(M, y, 'NAME'); c.drawString(M + 3.6 * inch, y, 'CLASS OF')
    c.setStrokeColor(RULE); c.setLineWidth(0.7)
    c.line(M + 0.55 * inch, y - 2, M + 3.3 * inch, y - 2)
    c.line(M + 4.35 * inch, y - 2, W - M, y - 2)

    # table
    cols = [('Term', 0.78), ('Pathway', 1.32), ('What I worked on', 2.35),
            ('What came of it', 2.05), ('Stay / move', 0.95)]
    total = sum(w for _, w in cols)
    x0 = M
    tw = W - 2 * M
    scale = tw / (total * inch)
    xs = [x0]
    for _, w in cols:
        xs.append(xs[-1] + w * inch * scale)

    ty = y - 0.42 * inch
    rh_head = 0.3 * inch
    c.setFillColor(PURPLE)
    c.rect(x0, ty - rh_head, tw, rh_head, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont('PB', 7.6)
    for i, (name, _) in enumerate(cols):
        c.drawString(xs[i] + 6, ty - rh_head + 10, name.upper())

    rows = [('Gr 11 · T1', ''), ('Gr 11 · T2', ''), ('Gr 11 · T3', ''),
            ('Gr 11 · T4', ''), ('Gr 12 · T1', ''), ('Gr 12 · T2', ''),
            ('Gr 12 · T3–4', 'Senior Capstone')]
    rh = 0.92 * inch
    yy = ty - rh_head
    for r, (label, sub) in enumerate(rows):
        top = yy
        yy -= rh
        if r % 2 == 1:
            c.setFillColor(SOFT)
            c.rect(x0, yy, tw, rh, fill=1, stroke=0)
        if sub:
            c.setFillColor(colors.HexColor('#f7f3fb'))
            c.rect(x0, yy, tw, rh, fill=1, stroke=0)
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.line(x0, yy, x0 + tw, yy)
        for xi in xs[1:-1]:
            c.line(xi, yy, xi, top)
        c.setFillColor(INK); c.setFont('PB', 9)
        c.drawString(xs[0] + 6, top - 15, label)
        if sub:
            c.setFont('LI', 8.4); c.setFillColor(INK2)
            c.drawString(xs[0] + 6, top - 28, sub)
            c.setFont('LI', 8); c.setFillColor(INK3)
            c.drawString(xs[1] + 6, top - 15,
                         'Grew out of a focus term?   yes  /  no')
        # faint ruled lines in the writing cells
        c.setStrokeColor(colors.HexColor('#e6e1ee')); c.setLineWidth(0.4)
        for k in range(1, 4):
            ly = top - k * (rh / 4.2) - 4
            for ci in (2, 3):
                c.line(xs[ci] + 6, ly, xs[ci + 1] - 6, ly)
    c.setStrokeColor(RULE); c.setLineWidth(0.8)
    c.rect(x0, yy, tw, ty - yy, fill=0, stroke=1)

    # foot
    fy = yy - 0.32 * inch
    c.setFont('L', 8.8); c.setFillColor(INK2)
    lines = [
        'Stay in one pathway to go deep, or move each term to come out broad. Both are good.',
        'The point of this page is that either choice is visible as a choice, and that you made it.',
        'Your focus stops when the Senior Capstone starts in Grade 12 Term 3. The capstone may grow',
        'out of it, but it does not have to.',
    ]
    for i, ln in enumerate(lines):
        c.drawString(M, fy - i * 12.5, ln)

    c.setFont('P', 7.2); c.setFillColor(INK3)
    c.drawString(M, 0.42 * inch,
                 'Blue Hills Regional Technical School  ·  Engineering Technology  ·  Room E-126  ·  ' + G.STAMP)
    c.drawRightString(W - M, 0.42 * inch, 'Keep in your binder')
    c.save()
    return path


if __name__ == '__main__':
    out = os.path.join(HERE, 'student-docs', 'BHR27-Independent-Focus-Record.pdf')
    build(out)
    print(out, os.path.getsize(out))
