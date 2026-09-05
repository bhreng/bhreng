#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shop posters, 11x17 (tabloid), for the graphics shop to print.

Design rules, so the set reads as one thing on a wall:
  * Purple band across the top, logo at the left, kicker on the right.
  * One idea per poster. If it needs two ideas, it is two posters.
  * The single most important line is the biggest thing on the page.
  * Readable from across the room: nothing below 13pt, headlines 40-90pt.
  * Colour is meaningful, not decorative -- green go, blue information,
    orange warning, purple the shop.

Every fact traces to a source already verified in this project: the two rules
documents, the manufacturer manuals behind the equipment checks, or Dan's own
course material. Nothing new is invented here.

Output: ./posters/*.pdf
"""

import os
import textwrap

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import safety_data as SD
import equipment_data as EQ
import build_hubs as B

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'posters')
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'site', 'assets', 'logo-240.png')

TABLOID = (11 * 72, 17 * 72)          # 792 x 1224 pt

import paths
D = paths.FONTS + '/'
pdfmetrics.registerFont(TTFont('Sans', D + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Sans-B', D + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Cond-B', D + 'DejaVuSansCondensed-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono', D + 'DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', D + 'DejaVuSansMono-Bold.ttf'))

PURPLE = HexColor('#6b4785')
BRAND = HexColor('#8d63ab')
NAVY = HexColor('#262b39')
INK2 = HexColor('#4f5566')
INK3 = HexColor('#7d8394')
RULE = HexColor('#cfccc6')
PAPER = HexColor('#faf8f4')
BLUE = HexColor('#1f5f9e')
BLUE_S = HexColor('#e7f0f8')
GREEN = HexColor('#2f6b40')
GREEN_S = HexColor('#e8f3ea')
WARM = HexColor('#a8541c')
WARM_S = HexColor('#fbeade')

M = 54                                  # margin


# ----------------------------------------------------------------- helpers

def wrap(c, text, x, y, w, font='Sans', size=15, lead=None, colour=NAVY,
         align='l'):
    """Draw wrapped text, return the y below it."""
    lead = lead or size * 1.34
    c.setFont(font, size)
    c.setFillColor(colour)
    words, line = text.split(), ''
    lines = []
    for word in words:
        t = (line + ' ' + word).strip()
        if c.stringWidth(t, font, size) <= w:
            line = t
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    for ln in lines:
        if align == 'c':
            c.drawCentredString(x + w / 2.0, y, ln)
        else:
            c.drawString(x, y, ln)
        y -= lead
    return y + lead - lead


def fit(c, text, w, font, start, floor=20):
    """Largest size at or below `start` that keeps `text` on one line."""
    s = start
    while s > floor and c.stringWidth(text, font, s) > w:
        s -= 1
    return s


def frame(c, kicker, page=TABLOID):
    """Common furniture: purple band, logo, kicker, footer."""
    W, H = page
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(BRAND)
    c.rect(0, H - 26, W, 26, stroke=0, fill=1)
    try:
        img = ImageReader(LOGO)
        iw, ih = img.getSize()
        h = 46.0
        c.drawImage(img, M, H - 26 - h - 16, width=h * iw / ih, height=h,
                    mask='auto')
    except Exception:
        pass
    c.setFont('Mono-B', 11)
    c.setFillColor(INK3)
    c.drawRightString(W - M, H - 26 - 30, kicker.upper())
    c.setFont('Mono', 9)
    c.drawString(M, 30, 'BHR ENGINEERING TECHNOLOGY')
    c.drawRightString(W - M, 30, 'THE SHOP HUB')
    return H - 26 - 46 - 40


def band(c, y, text, w, bg, fg, size=17, pad=16, font='Sans-B', page=TABLOID):
    """A filled callout. Returns the y below it."""
    W, _ = page
    c.setFont(font, size)
    words, line, lines = text.split(), '', []
    for word in words:
        t = (line + ' ' + word).strip()
        if c.stringWidth(t, font, size) <= w - 2 * pad:
            line = t
        else:
            lines.append(line); line = word
    if line:
        lines.append(line)
    h = len(lines) * size * 1.3 + 2 * pad
    c.setFillColor(bg)
    c.rect(M, y - h, w, h, stroke=0, fill=1)
    c.setFillColor(fg)
    yy = y - pad - size
    for ln in lines:
        c.drawString(M + pad, yy, ln)
        yy -= size * 1.3
    return y - h


def numbered(c, y, items, w, size=17, gap=13, colour=PURPLE, page=TABLOID):
    """A numbered list with circular markers."""
    for i, it in enumerate(items, 1):
        r = max(13, size * 0.68)        # marker scales with the text
        c.setFillColor(colour)
        c.circle(M + r, y - r + 3, r, stroke=0, fill=1)
        c.setFont('Sans-B', max(12, size * 0.62))
        c.setFillColor(white)
        c.drawCentredString(M + r, y - r - size * 0.20, str(i))
        end = wrap(c, it, M + 2 * r + 12, y - 4, w - 2 * r - 12,
                   'Sans', size, size * 1.3)
        y = min(end, y - 2 * r) - gap
    return y


def bullets(c, y, items, w, size=15, gap=10, dot=GREEN, page=TABLOID):
    for it in items:
        c.setFillColor(dot)
        # centre the dot on the first line's x-height, not below its baseline
        c.circle(M + 5.5, y + size * 0.30, 4.5, stroke=0, fill=1)
        end = wrap(c, it, M + 22, y, w - 22, 'Sans', size, size * 1.32)
        y = end - gap
    return y


def clean(t):
    return (t.replace('&hellip;', '…').replace('&mdash;', '—')
             .replace('&rsquo;', '’').replace('&ldquo;', '“')
             .replace('&rdquo;', '”').replace('&deg;', '°')
             .replace('&nbsp;', ' ').replace('&amp;', '&')
             .replace('&middot;', '·'))


# ------------------------------------------------------------ the posters

def p_emergency(c):
    """The one that matters at the worst moment. Hang it by the door and the
    eyewash, not on a noticeboard."""
    W, H = TABLOID
    y = frame(c, 'If someone is hurt')
    c.setFont('Cond-B', 96); c.setFillColor(WARM)
    c.drawString(M, y - 80, 'EMERGENCY')
    y -= 118
    c.setStrokeColor(NAVY); c.setLineWidth(3)
    c.line(M, y, W - M, y); y -= 46

    c.setFont('Sans-B', 30); c.setFillColor(NAVY)
    c.drawString(M, y, 'School nurse'); y -= 106
    c.setFont('Cond-B', 138); c.setFillColor(BLUE)
    c.drawString(M, y, 'ext. ' + SD.NURSE_EXT)
    y -= 66

    y = band(c, y, 'Report all injuries. Every one, however small.',
             W - 2 * M, GREEN_S, GREEN, size=28)
    y -= 48

    c.setFont('Sans-B', 30); c.setFillColor(NAVY)
    c.drawString(M, y, 'Chemical in the eyes'); y -= 46
    y = wrap(c, 'Wash the eye under an open flow of water for FIFTEEN MINUTES '
                'before going for treatment. Have someone else fetch help while '
                'you stay at the water.',
             M, y, W - 2 * M, 'Sans', 23, 33, INK2)
    y -= 28
    y = band(c, y, 'Never try to remove a foreign object from an eye or from '
                   'the body. Water only.',
             W - 2 * M, WARM_S, WARM, size=22)
    y -= 42

    c.setFont('Sans-B', 27); c.setFillColor(NAVY)
    c.drawString(M, y, 'Know these before you need them'); y -= 40
    return bullets(c, y, ['Where the first aid kit is.',
                          'Where the eyewash is.',
                          'Where the fire extinguisher is.',
                          'Where the nearest instructor is.',
                          'Never work alone with power tools. Two people, '
                          'both able to see each other.'],
                   W - 2 * M, size=19, gap=12, dot=BLUE)


def p_primary(c):
    W, H = TABLOID
    y = frame(c, 'Conditions of entry')
    c.setFont('Cond-B', 70); c.setFillColor(NAVY)
    c.drawString(M, y - 58, 'THE TEN RULES')
    y -= 88
    y = wrap(c, 'Primary Makerspace Rules. Be familiar with the complete set '
                'before using the Makerspace.',
             M, y, W - 2 * M, 'Sans', 19, 27, INK2)
    y -= 34
    y = numbered(c, y, [clean(r) for r in SD.PRIMARY_RULES], W - 2 * M,
                 size=25, gap=17)
    c.setFillColor(BLUE_S)
    c.rect(M, 60, W - 2 * M, 56, stroke=0, fill=1)
    c.setFont('Sans-B', 19); c.setFillColor(BLUE)
    c.drawString(M + 18, 88, 'Maximum occupancy: %s students' % SD.MAX_OCCUPANCY)
    c.setFont('Sans', 14); c.setFillColor(INK2)
    c.drawString(M + 18, 68, 'Over that, it is the instructor’s call.')
    return y - 76   # the occupancy box occupies y = 60..116


def p_ppe(c):
    W, H = TABLOID
    y = frame(c, 'Before you walk in')
    c.setFont('Cond-B', 92); c.setFillColor(NAVY)
    c.drawString(M, y - 76, 'DRESS RIGHT')
    y -= 108
    y = band(c, y, 'No safety glasses… No entry.', W - 2 * M, WARM_S, WARM,
             size=34)
    y -= 34
    y = wrap(c, 'Eye protection is worn at all times in the Makerspace — '
                'whether you are working or not. Someone else’s work can reach '
                'your eyes while you are just walking through.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 30
    _, _, items = SD.MAKERSPACE_RULES[1]
    return numbered(c, y, [clean(i) for i in items], W - 2 * M, size=22,
                    gap=17, colour=BLUE)


def p_trained(c):
    W, H = TABLOID
    y = frame(c, 'Primary rule 8')
    c.setFont('Cond-B', 60); c.setFillColor(NAVY)
    c.drawString(M, y - 50, 'BEFORE YOU TOUCH')
    c.drawString(M, y - 110, 'A MACHINE')
    y -= 150
    y = band(c, y, 'Only trained AND authorized students may operate machinery '
                   'or hand tools.', W - 2 * M, WARM_S, WARM, size=25)
    y -= 46
    col = (W - 2 * M - 26) / 2.0
    for i, (term, meaning) in enumerate(SD.TRAINED_AUTHORIZED):
        x = M + i * (col + 26)
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(x, y - 176, col, 176, stroke=1, fill=1)
        c.setFillColor(PURPLE); c.setFont('Cond-B', 44)
        c.drawString(x + 20, y - 62, term.upper())
        wrap(c, meaning, x + 20, y - 96, col - 40, 'Sans', 17, 25, INK2)
    y -= 210
    c.setFont('Sans-B', 24); c.setFillColor(NAVY)
    c.drawString(M, y, 'They are not the same thing'); y -= 36
    y = wrap(c, 'Training is the instruction. Authorization is the check that '
                'you took it in. Doing the training does not authorize you, and '
                'being confident authorizes you least of all.',
             M, y, W - 2 * M, 'Sans', 21, 30, INK2)
    y -= 34
    return bullets(c, y, ['Every machine is separate. The bandsaw does not '
                   'certify you on the laser.',
                   'Access can be revoked at any time, at an instructor’s '
                   'discretion.',
                   'Never work alone with power tools — two people, both able '
                   'to see each other.'],
            W - 2 * M, size=21, gap=20, dot=BLUE)


def p_printers(c):
    """Landscape: the ladder reads as a grid."""
    W, H = landscape(TABLOID)
    y = frame(c, '3D printer access', page=landscape(TABLOID))
    c.setFont('Cond-B', 68); c.setFillColor(NAVY)
    c.drawString(M, y - 56, '3D PRINTER CERTIFICATION')
    y -= 92
    y = band(c, y, 'Every job is approved by an instructor first — at every '
                   'level, on every machine.', W - 2 * M, WARM_S, WARM, size=20,
             page=landscape(TABLOID))
    y -= 40
    levels = [('BEGINNER', 'Print with an instructor helping you.'),
              ('INTERMEDIATE', 'Print with an approved peer helping you.'),
              ('ADVANCED', 'Print on your own.')]
    col = (W - 2 * M - 40) / 3.0
    for i, (nm, txt) in enumerate(levels):
        x = M + i * (col + 20)
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(x, y - 150, col, 150, stroke=1, fill=1)
        c.setFillColor(GREEN_S); c.rect(x, y - 34, col, 34, stroke=0, fill=1)
        c.setFillColor(GREEN); c.setFont('Sans-B', 15)
        c.drawString(x + 16, y - 24, 'LEVEL %d' % (i + 1))
        c.setFillColor(NAVY)
        s = fit(c, nm, col - 32, 'Cond-B', 40)
        c.setFont('Cond-B', s); c.drawString(x + 16, y - 76, nm)
        wrap(c, txt, x + 16, y - 104, col - 32, 'Sans', 16, 23, INK2)
    y -= 190
    c.setFont('Sans-B', 26); c.setFillColor(NAVY)
    c.drawString(M, y, 'And the machines go in order'); y -= 46
    machines = [('A1 MINI', 'Where everyone starts'),
                ('X1C', 'Bigger, faster, enclosed'),
                ('H2D', 'The largest machine in the room')]
    for i, (nm, txt) in enumerate(machines):
        x = M + i * (col + 20)
        c.setFillColor(BLUE_S); c.rect(x, y - 92, col, 92, stroke=0, fill=1)
        c.setFillColor(BLUE); c.setFont('Cond-B', 38)
        c.drawString(x + 16, y - 48, nm)
        c.setFillColor(INK2); c.setFont('Sans', 15)
        c.drawString(x + 16, y - 72, txt)
        if i < 2:
            c.setFillColor(INK3); c.setFont('Sans-B', 26)
            c.drawCentredString(x + col + 10, y - 52, '›')
    y -= 128
    return wrap(c, 'After a level on one machine you may go up a level on that '
                'machine, or take the same level on the next machine. You cannot '
                'skip a machine. Training is the free Bambu Lab Academy course '
                'for that printer — bring your completion to Mr. Frank.',
                M, y, W - 2 * M, 'Sans', 17, 25, INK2)


def p_laser(c):
    W, H = TABLOID
    y = frame(c, 'At the laser')
    c.setFont('Cond-B', 78); c.setFillColor(NAVY)
    c.drawString(M, y - 64, 'THE LASER')
    y -= 104
    y = band(c, y, 'NEVER cut PVC, vinyl or Kydex.', W - 2 * M, WARM_S, WARM,
             size=36)
    y -= 30
    y = wrap(c, 'They release hydrogen chloride, which becomes hydrochloric acid '
                'in your lungs and on the machine. It corrodes the optics and the '
                'rails for months afterwards, and it voids the warranty.',
             M, y, W - 2 * M, 'Sans', 20, 29, INK2)
    y -= 26
    y = band(c, y, 'Unlabelled plastic? Do not cut it. Find out what it is first.',
             W - 2 * M, BLUE_S, BLUE, size=22)
    y -= 46
    c.setFont('Sans-B', 30); c.setFillColor(NAVY)
    c.drawString(M, y, 'Fire'); y -= 44
    y = numbered(c, y, [
        'Stay with the laser. Never run it unattended — not for twelve '
        'minutes, not for two.',
        'Cutting starts fires; engraving rarely does. Always use air assist '
        'when cutting through.',
        'Clear the debris under the cutting grid. Most fires are lit by your '
        'job and fed by last month’s scrap.',
        'If a flame appears: press the EMERGENCY STOP, then get an instructor.',
    ], W - 2 * M, size=20, gap=16, colour=WARM)
    y -= 20
    c.setFont('Sans-B', 26); c.setFillColor(NAVY)
    c.drawString(M, y, 'Two things people get wrong'); y -= 40
    return bullets(c, y, [
        'You cannot see the cutting beam. It is invisible infrared — the red '
        'dot is a separate pointer, and the glow is the material burning.',
        'The lid is not what protects you. Interlock switches cut the beam. '
        'Defeat them and you have a Class 4 laser in an open box.',
    ], W - 2 * M, size=20, gap=17, dot=BLUE)


def p_resin(c):
    W, H = TABLOID
    y = frame(c, 'At the J55')
    c.setFont('Cond-B', 66); c.setFillColor(NAVY)
    c.drawString(M, y - 54, 'RESIN IS A CHEMICAL,')
    c.drawString(M, y - 116, 'NOT A PLASTIC')
    y -= 156
    y = band(c, y, 'A part fresh off the printer is coated in uncured resin. '
                   'Nitrile gloves.', W - 2 * M, WARM_S, WARM, size=25)
    y -= 44
    c.setFont('Sans-B', 30); c.setFillColor(NAVY)
    c.drawString(M, y, 'It does not have to hurt to harm you'); y -= 46
    y = wrap(c, 'The support material is a Category 1 skin sensitiser. Repeated '
                'small exposures can build a permanent allergy — after which even '
                'a trace sets it off. A little on your hands every week for a '
                'semester is how that happens. Absence of pain is not absence '
                'of harm.',
             M, y, W - 2 * M, 'Sans', 19, 27, INK2)
    y -= 40
    y = band(c, y, 'Diluting caustic soda? Caustic soda INTO water. Never water '
                   'into caustic soda.', W - 2 * M, BLUE_S, BLUE, size=22)
    y -= 44
    c.setFont('Sans-B', 26); c.setFillColor(NAVY)
    c.drawString(M, y, 'The rules'); y -= 40
    return bullets(c, y, [
        'Nitrile gloves — not latex, which acrylates go straight through.',
        'Gloves come OFF before you touch a door, a phone or a keyboard.',
        'Resin in the eye: rinse 15 minutes, under the eyelids too, then get '
        'treatment. This is Category 1 eye damage.',
        'Resin on skin: soap and water, 15 minutes.',
        'A part is safe bare-handed only after full support removal and washing.',
    ], W - 2 * M, size=19, gap=16, dot=WARM)


def p_cobot(c):
    W, H = TABLOID
    y = frame(c, 'At the UR arms')
    c.setFont('Cond-B', 62); c.setFillColor(NAVY)
    c.drawString(M, y - 52, '“COLLABORATIVE”')
    c.drawString(M, y - 112, 'IS NOT “SAFE”')
    y -= 152
    y = wrap(c, 'Universal Robots’ own words: cobots alone are not '
                'collaborative — only cobot applications can be. The 2025 '
                'revision of the international standard deleted the term '
                '“collaborative robot” for exactly this reason.',
             M, y, W - 2 * M, 'Sans', 19, 27, INK2)
    y -= 34
    y = band(c, y, 'The tool on the end is NOT protected by the robot’s safety '
                   'system.', W - 2 * M, WARM_S, WARM, size=25)
    y -= 30
    y = wrap(c, 'The arm is force-limited. The gripper, the blade, the hot iron '
                'it is holding are not monitored at all. And force limiting caps '
                'force, not pressure — a point concentrates the same force into '
                'a tiny area and punctures skin.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 38
    c.setFont('Sans-B', 28); c.setFillColor(NAVY)
    c.drawString(M, y, 'Slow does not mean gentle'); y -= 42
    y = wrap(c, 'Near full extension, or working close to its own base, the arm '
                'can deliver high force at low speed. You cannot judge the danger '
                'by how fast it looks.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 38
    return bullets(c, y, [
        'UR3 reaches 500 mm. UR5 reaches 850 mm. Know which one you are '
        'standing next to.',
        'Support the arm before releasing the brakes. It falls.',
        'Free-drive is a one-person job. Nobody leans in.',
        'Change the tool and the risk assessment has to be redone.',
    ], W - 2 * M, size=21, gap=21, dot=BLUE)


def p_solder(c):
    W, H = TABLOID
    y = frame(c, 'At the bench')
    c.setFont('Cond-B', 70); c.setFillColor(NAVY)
    c.drawString(M, y - 58, 'SOLDERING')
    c.drawString(M, y - 122, 'AND HOT GLUE')
    y -= 162
    y = band(c, y, 'That white smoke is FLUX, not lead.', W - 2 * M, BLUE_S,
             BLUE, size=30)
    y -= 30
    y = wrap(c, 'Lead boils at about 1,740 °C; the iron runs near 350 °C. What '
                'you can smell is rosin flux, and it causes occupational asthma. '
                'Watery eyes, a scratchy throat or a cough means you have had '
                'enough of it — say so.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 34
    c.setFont('Sans-B', 28); c.setFillColor(NAVY)
    c.drawString(M, y, 'Lead gets in by being swallowed'); y -= 42
    y = wrap(c, 'Hands, bench, phone, snack, mouth. That is the route. No food '
                'or drink at the bench, wash your hands and arms properly '
                'afterwards, and wipe the surface down.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 38
    y = band(c, y, 'The iron lives in its stand. Every time.', W - 2 * M,
             GREEN_S, GREEN, size=26)
    y -= 44
    c.setFont('Sans-B', 26); c.setFillColor(NAVY)
    c.drawString(M, y, 'Hot glue burns worse than the iron'); y -= 40
    y = wrap(c, 'It is cooler, and it sticks — so it keeps putting heat into you '
                'and you cannot pull away. Cold running water for 15 minutes, and '
                'do not peel the glue off first.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 34
    return bullets(c, y, [
        'Safety glasses. Solder spits when flux flashes.',
        'Use the fume extractor at the source — a desk fan just moves it '
        'onto the person next to you.',
        'The joint, the component leads and the board stay hot after the iron '
        'has gone.',
    ], W - 2 * M, size=19, gap=16, dot=WARM)


def p_cleanup(c):
    W, H = TABLOID
    y = frame(c, 'Before you leave')
    c.setFont('Cond-B', 88); c.setFillColor(NAVY)
    c.drawString(M, y - 72, 'CLEAN UP')
    y -= 108
    y = wrap(c, 'Every time you leave an area. Including the floor.',
             M, y, W - 2 * M, 'Sans-B', 26, 34, PURPLE)
    y -= 30
    _, _, items = SD.MAKERSPACE_RULES[4]
    y = numbered(c, y, [clean(i) for i in items], W - 2 * M, size=22, gap=20,
                 colour=GREEN)
    y -= 10
    return band(c, y, 'Use a brush or a hook for chips and shavings. Never your '
                      'hands — they are sharp and they are often still hot.',
                W - 2 * M, WARM_S, WARM, size=19)


def p_pathways(c):
    """Landscape. The wall version of the chooser."""
    W, H = landscape(TABLOID)
    y = frame(c, 'Every student, every term', page=landscape(TABLOID))
    c.setFont('Cond-B', 72); c.setFillColor(NAVY)
    c.drawString(M, y - 60, 'THE SEVEN PATHWAYS')
    y -= 96
    y = wrap(c, 'Each one is the home of a state technical standard, and each is '
                'somewhere you could spend a term going deep. You do not have to '
                'pick the one you are best at.',
             M, y, W - 2 * M, 'Sans', 19, 27, INK2)
    y -= 34
    col = (W - 2 * M - 3 * 18) / 4.0
    for i, p in enumerate(B.P):
        cx = M + (i % 4) * (col + 18)
        cy = y - (i // 4) * 216
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(cx, cy - 200, col, 200, stroke=1, fill=1)
        c.setFillColor(PURPLE); c.rect(cx, cy - 32, col, 32, stroke=0, fill=1)
        c.setFillColor(white); c.setFont('Mono-B', 13)
        c.drawString(cx + 14, cy - 22, 'STANDARD ' + clean(p['std']))
        c.setFillColor(NAVY)
        size = fit(c, clean(p['nav']), col - 28, 'Cond-B', 31, 17)
        c.setFont('Cond-B', size)
        c.drawString(cx + 14, cy - 64, clean(p['nav']))
        wrap(c, clean(p.get('tag', '')), cx + 14, cy - 92, col - 28,
             'Sans', 14.5, 21, INK2)
        c.setFillColor(INK3); c.setFont('Mono', 11)
        c.drawString(cx + 14, cy - 186, clean(p.get('lead', '')).upper())
    return y - 216 * 2 + 16


ROLES = [
    ('Design', 'Turns a requirement into a mechanism, with the calculations '
               'to back it. Produces the drawing set or the CAD model.'),
    ('Research', 'Investigates, and predicts a new use for something that '
                 'exists or a new way to do the job.'),
    ('Development', 'Makes the model or the prototype. Finds out whether the '
                    'idea survives contact with material.'),
    ('Production &\nConstruction', 'Works out the order things happen in. '
                                   'Work breakdown structure, then a Gantt chart.'),
    ('Operations', 'Designs the large system and how it is actually run, '
                   'including what happens when it misbehaves.'),
    ('Sales', 'Explains the engineering to someone who has to decide. The ad, '
              'the brochure, the pitch.'),
    ('Management', 'Builds the team and assigns the work so a product gets '
                   'finished by people who are not you.'),
]


def p_roles(c):
    W, H = TABLOID
    y = frame(c, 'Full Scope Project')
    c.setFont('Cond-B', 60); c.setFillColor(NAVY)
    c.drawString(M, y - 50, 'THE SEVEN ROLES')
    c.drawString(M, y - 108, 'OF AN ENGINEER')
    y -= 142
    y = wrap(c, 'Engineering is not one job. Over three weeks you will step into '
                'several of these and produce what a professional in that role '
                'actually produces.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 30
    for name, desc in ROLES:
        h = 92
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(M, y - h, W - 2 * M, h, stroke=1, fill=1)
        c.setFillColor(PURPLE)
        c.rect(M, y - h, 6, h, stroke=0, fill=1)
        c.setFillColor(NAVY)
        lines = name.split('\n')
        c.setFont('Cond-B', 27)
        yy = y - 30 if len(lines) == 1 else y - 26
        for ln in lines:
            c.drawString(M + 22, yy, ln.upper()); yy -= 26
        wrap(c, desc, M + 250, y - 30, W - 2 * M - 272, 'Sans', 15.5, 22, INK2)
        y -= h + 8
    return y


# ------------------------------------------------------- grades and rules
# Weights confirmed against BOTH source documents in Drive, May 2026:
#   "BHR ENG Doc - Grading & Assessment" and the Level-Up Guide agree.
# The 40/30/20/10 split in the Software hub guide is wrong and has been fixed.

WEIGHTS = [
    ('Project Grade', 35, 'Individual rubrics for each project. Productivity, '
                          'creativity, accuracy and timing.'),
    ('Weekly Grade', 30, 'Behaviour and performance: safety, initiative, '
                         'preparation, attitude, work ethic, productivity.'),
    ('Employability', 20, 'Weekly and term soft skills — recurring assignments '
                          'and professionalism in the shop.'),
    ('Classwork', 15, 'Classroom exercises. Pacing your time, staying on task, '
                      'following directions.'),
]

SCALE = [('4', 'Excellent', 100), ('3', 'Good', 92), ('2', 'Fair', 78),
         ('1', 'Unsatisfactory', 52), ('0', 'Poor', 28)]

WEEKLY = [
    ('Safety', 'Follows all safety rules, maintains a clean work area, and '
               'returns all materials to the proper place upon completing a task.'),
    ('Initiative', 'Stays on task, seeks additional work, offers assistance to '
                   'peers, comes for help when needed, uses downtime effectively.'),
    ('Preparation', 'On time to class, agenda present, writing instrument '
                    'present, dressed to shop standards, awake and alert.'),
    ('Attitude', 'Positive attitude, interacts appropriately with others, uses '
                 'appropriate language, maintains self-control at all times.'),
    ('Work Ethic', 'Best efforts, cooperative, demonstrates peer leadership, '
                   'self-starter, never publicly critical of others’ work.'),
    ('Productivity', 'Work of the highest quality, looks for and suggests '
                     'solutions, uses time well, contributes useful ideas.'),
]

PROJECT_RUBRIC = [
    ('Concept', 'Clear understanding of unit concepts. Solves problems '
                'independently.'),
    ('Background knowledge', 'Clear understanding of previously learned '
                             'material. Minimal or no reinforcement required.'),
    ('Technical knowledge', 'Contains all requested requirements. A high level '
                            'of accuracy has been achieved.'),
    ('Participation / teamwork', 'Work performed in a timely manner. On task '
                                 'all of the time. Works very well in the team.'),
    ('Presentation', 'Graphics presented professionally. Technical drawings '
                     'include all specifications. Visually appealing.'),
]

SHOP_RULES = [
    'Cell phones during break and lunch only. Headphones occasionally, during '
    'individual project work.',
    'Proper uniform and PPE are required for your grade.',
    'No eating or drinking in shop common areas.',
    'Respect the teacher, your classmates and the property. Keep the work '
    'environment clean.',
    'Equipment is used only with permission. No writing on or cutting the tables.',
    'Follow the end-of-day cleanup routine. Return things to their proper '
    'places, and clean for yourself and for others.',
    'Stay in your assigned area. Leave only with verbal permission or a pass.',
    'Computers are for educational purposes. If your work is done, ask for more '
    'or help a classmate.',
    'Be on time — for class and for every project deadline.',
    'It is your responsibility to ask questions before the assignment is due.',
]

NOTEBOOK = [
    ('Project title', 'The official name of what you are working on.'),
    ('Tools used', 'Hardware and software. 3D printers, laser, CAD package, '
                   'everything.'),
    ('Daily bullet points', 'What you actually got done this session.'),
    ('Notes, 50+ words', 'A technical description of the work and the reasoning '
                         'behind it.'),
    ('Next class agenda', 'Clear, actionable steps for next time.'),
    ('Labeled images', 'Visual evidence that it progressed.'),
]


def p_grading(c):
    W, H = TABLOID
    y = frame(c, 'How your grade is built')
    c.setFont('Cond-B', 92); c.setFillColor(NAVY)
    c.drawString(M, y - 76, 'YOUR GRADE')
    y -= 122
    for name, pct, desc in WEIGHTS:
        h = 156
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(M, y - h, W - 2 * M, h, stroke=1, fill=1)
        # the bar is the number, drawn to scale
        c.setFillColor(PURPLE)
        c.rect(M, y - h, (W - 2 * M) * pct / 100.0, 9, stroke=0, fill=1)
        c.setFillColor(PURPLE); c.setFont('Cond-B', 78)
        c.drawRightString(W - M - 28, y - 78, '%d%%' % pct)
        c.setFillColor(NAVY); c.setFont('Cond-B', 38)
        c.drawString(M + 26, y - 54, name.upper())
        wrap(c, desc, M + 26, y - 86, W - 2 * M - 240, 'Sans', 18, 26, INK2)
        y -= h + 12
    y -= 40
    c.setFont('Sans-B', 30); c.setFillColor(NAVY)
    c.drawString(M, y, 'What the scores mean'); y -= 54
    col = (W - 2 * M - 4 * 10) / 5.0
    for i, (n, nm, val) in enumerate(SCALE):
        x = M + i * (col + 10)
        bg = GREEN_S if i < 2 else (BLUE_S if i == 2 else WARM_S)
        fg = GREEN if i < 2 else (BLUE if i == 2 else WARM)
        c.setFillColor(bg); c.rect(x, y - 124, col, 124, stroke=0, fill=1)
        c.setFillColor(fg); c.setFont('Cond-B', 56)
        c.drawCentredString(x + col / 2, y - 56, str(val))
        s = fit(c, nm, col - 12, 'Sans-B', 15, 9)
        c.setFont('Sans-B', s)
        c.drawCentredString(x + col / 2, y - 84, nm)
        c.setFillColor(INK3); c.setFont('Mono', 11)
        c.drawCentredString(x + col / 2, y - 106, 'RANK ' + n)
    return y - 124


def p_weekly(c):
    W, H = TABLOID
    y = frame(c, '30% of your grade')
    c.setFont('Cond-B', 66); c.setFillColor(NAVY)
    c.drawString(M, y - 56, 'THE WEEKLY GRADE')
    y -= 92
    y = wrap(c, 'Six things, scored every week. This is the part of your grade '
                'that is about how you work rather than what you make — which '
                'means it is the part you control completely.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 30
    for i, (name, desc) in enumerate(WEEKLY):
        h = 126
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(M, y - h, W - 2 * M, h, stroke=1, fill=1)
        c.setFillColor(GREEN if i < 4 else BLUE)
        c.rect(M, y - h, 6, h, stroke=0, fill=1)
        c.setFillColor(NAVY); c.setFont('Cond-B', 30)
        c.drawString(M + 24, y - 40, name.upper())
        c.setFillColor(INK3); c.setFont('Mono', 11)
        c.drawRightString(W - M - 20, y - 32,
                          'BEHAVIOUR' if i < 4 else 'PERFORMANCE')
        wrap(c, desc, M + 24, y - 68, W - 2 * M - 48, 'Sans', 16, 23, INK2)
        y -= h + 8
    return y


def p_project_rubric(c):
    W, H = TABLOID
    y = frame(c, '35% of your grade')
    c.setFont('Cond-B', 62); c.setFillColor(NAVY)
    c.drawString(M, y - 52, 'THE PROJECT RUBRIC')
    y -= 88
    y = wrap(c, 'Every project is scored on these five, each worth 20 points. '
                'What follows is what EXCELLENT looks like — the standard, not '
                'the average.',
             M, y, W - 2 * M, 'Sans', 18, 26, INK2)
    y -= 32
    for name, desc in PROJECT_RUBRIC:
        h = 150
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(M, y - h, W - 2 * M, h, stroke=1, fill=1)
        c.setFillColor(PURPLE); c.rect(M, y - 42, W - 2 * M, 42, stroke=0,
                                       fill=1)
        c.setFillColor(white); c.setFont('Cond-B', 27)
        c.drawString(M + 20, y - 30, name.upper())
        c.setFont('Cond-B', 27)
        c.drawRightString(W - M - 20, y - 30, '20 pts')
        c.setFillColor(GREEN); c.setFont('Mono-B', 12)
        c.drawString(M + 20, y - 72, 'EXCELLENT')
        wrap(c, desc, M + 20, y - 100, W - 2 * M - 40, 'Sans', 18, 26, NAVY)
        y -= h + 10
    return y


def p_shop_rules(c):
    W, H = TABLOID
    y = frame(c, 'Professional practice')
    c.setFont('Cond-B', 86); c.setFillColor(NAVY)
    c.drawString(M, y - 72, 'SHOP RULES')
    y -= 112
    y = numbered(c, y, SHOP_RULES, W - 2 * M, size=22, gap=16)
    y -= 18
    y = band(c, y, 'Always work to your full potential. Prepare to be '
                   'challenged.', W - 2 * M, PURPLE, white, size=26)
    y -= 18
    return band(c, y, 'And the bonus rule: USE COMMON SENSE.', W - 2 * M,
                GREEN_S, GREEN, size=26)


def p_notebook(c):
    W, H = TABLOID
    y = frame(c, 'Every shop day')
    c.setFont('Cond-B', 60); c.setFillColor(NAVY)
    c.drawString(M, y - 50, 'THE ENGINEER’S')
    c.drawString(M, y - 108, 'LOGBOOK')
    y -= 148
    y = band(c, y, 'Your single source of truth. A legal and technical document.',
             W - 2 * M, BLUE_S, BLUE, size=23)
    y -= 40
    for name, desc in NOTEBOOK:
        h = 88
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(M, y - h, W - 2 * M, h, stroke=1, fill=1)
        c.setFillColor(PURPLE); c.rect(M, y - h, 6, h, stroke=0, fill=1)
        c.setFillColor(NAVY); c.setFont('Cond-B', 26)
        c.drawString(M + 22, y - 34, name.upper())
        wrap(c, desc, M + 22, y - 58, W - 2 * M - 44, 'Sans', 15.5, 22, INK2)
        y -= h + 8
    y -= 34
    c.setFont('Sans-B', 24); c.setFillColor(NAVY)
    c.drawString(M, y, 'Why it matters more than you think'); y -= 38
    return wrap(c, 'Thomas Edison left roughly five million pages of notes. In '
                   '1943 the Supreme Court struck down Marconi’s key radio '
                   'claims because Tesla’s earlier documented work came first. '
                   'The logbook is the evidence that the invention was yours.',
                M, y, W - 2 * M, 'Sans', 17, 25, INK2)


def p_edf_esec(c):
    W, H = landscape(TABLOID)
    y = frame(c, 'Who to ask', page=landscape(TABLOID))
    c.setFont('Cond-B', 70); c.setFillColor(NAVY)
    c.drawString(M, y - 58, 'TWO HALVES OF ONE PROGRAM')
    y -= 96
    y = wrap(c, 'Everything in this shop sits on one of two axes. Both '
                'instructors teach all four years — go to whoever fits the '
                'problem in front of you.',
             M, y, W - 2 * M, 'Sans', 19, 27, INK2)
    y -= 36
    col = (W - 2 * M - 30) / 2.0
    panes = [
        ('EDF', 'Engineering Design & Fabrication', 'Mr. Frank',
         'Turning an idea into a thing that exists, and making it hold up.',
         ['Designing in CAD so it works and looks right',
          'Getting a part ready to print or cut',
          'Structures that carry load',
          'Drawings someone else could build from',
          'Fixing a prototype that came out wrong'], PURPLE),
        ('ESEC', 'Engineering Systems & Emerging Concepts', 'Mr. Dryer',
         'The invisible half — the code and the circuits that make it decide '
         'something.',
         ['Designing or troubleshooting a circuit',
          'Writing and debugging code for a board or robot',
          'Working out why a system misbehaves',
          'Getting sensors and motors working together',
          'Proving with data that it does what you claim'], BLUE),
    ]
    for i, (abbr, full, who, blurb, items, colour) in enumerate(panes):
        x = M + i * (col + 30)
        c.setFillColor(white); c.setStrokeColor(RULE); c.setLineWidth(1)
        c.rect(x, y - 400, col, 400, stroke=1, fill=1)
        c.setFillColor(colour); c.rect(x, y - 92, col, 92, stroke=0, fill=1)
        c.setFillColor(white); c.setFont('Cond-B', 54)
        c.drawString(x + 22, y - 52, abbr)
        c.setFont('Sans-B', 14)
        c.drawString(x + 22, y - 74, full)
        c.setFillColor(NAVY); c.setFont('Cond-B', 34)
        c.drawString(x + 22, y - 132, who.upper())
        yy = wrap(c, blurb, x + 22, y - 162, col - 44, 'Sans', 16, 23, INK2)
        yy -= 18
        for it in items:
            c.setFillColor(colour); c.circle(x + 28, yy + 5, 4, stroke=0, fill=1)
            yy = wrap(c, it, x + 44, yy, col - 66, 'Sans', 15, 21, NAVY) - 10
    return y - 400


# ---------------------------------------------------------------- the driver

POSTERS = [
    ('emergency',            p_emergency,      0),
    ('primary-rules',        p_primary,        0),
    ('ppe-dress-right',      p_ppe,            0),
    ('trained-and-authorized', p_trained,      0),
    ('3d-printer-levels',    p_printers,       1),
    ('laser',                p_laser,          0),
    ('resin-j55',            p_resin,          0),
    ('cobots',               p_cobot,          0),
    ('soldering-hot-glue',   p_solder,         0),
    ('clean-up',             p_cleanup,        0),
    ('seven-pathways',       p_pathways,       1),
    ('roles-of-an-engineer', p_roles,          0),
    ('grading',              p_grading,        0),
    ('weekly-grade',         p_weekly,         0),
    ('project-rubric',       p_project_rubric, 0),
    ('shop-rules',           p_shop_rules,     0),
    ('engineers-logbook',    p_notebook,       0),
    ('edf-and-esec',         p_edf_esec,       1),
]


def main(outdir='posters'):
    import os
    from reportlab.pdfgen import canvas as _canvas
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    over, report = [], []
    for name, fn, land in POSTERS:
        page = landscape(TABLOID) if land else TABLOID
        c = _canvas.Canvas(os.path.join(outdir, name + '.pdf'), pagesize=page)
        c.setTitle('BHR Engineering Technology — ' + name)
        y = fn(c)
        c.save()
        slack = int(y - 54) if y is not None else 0
        report.append('%s %d' % (name, slack))
        if slack < 0:
            over.append(name)
    print('  ' + ' | '.join(report))
    print('OVERFLOW:', over)
    print('total', len(POSTERS))


if __name__ == '__main__':
    main()
