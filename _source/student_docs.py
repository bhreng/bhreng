# -*- coding: utf-8 -*-
"""The documents students hand in.

One definition per document, in one place, so every hand-in a student
touches has the same header, the same identity block, the same heading
weights and the same fill-in boxes. Before this, ten documents had been
written at different times by different hands and it showed: some opened
with a bare "Name" on line one, some had the title in the body, some
asked for the project title and some did not, and two of them were the
same instrument under two different names.

WHAT WAS DELIBERATELY CHANGED, and why -- so nobody "fixes" it back:

  * Logbook and Daily Journal were the same document under two names, both
    being distributed to the same class at the same time. They are now one
    document, "Daily Logbook". Whichever one Classroom is handing out, it
    should now hand out this.
  * Four templates were 3.36 MB each because of a full-resolution image.
    That is roughly a thousand times what a text template should weigh, and
    every student copy carried it, every year, in every class. The logo here
    is 64 KB and looks the same on paper.
  * The instruction lines are addressed to the student in plain words.
    "Utilize the following status codes to categorize the current phase of
    engineering activity" says the same thing as "mark which stage of the
    design process you were in", and one of them is readable at 7:45 am.
  * Every document now has the same identity block, so a hand-in is never
    anonymous and never undated.

WHAT WAS NOT CHANGED: the questions themselves. Every prompt below is the
prompt from the existing template, trimmed rather than reworded, because
the wording is Dan's and the questions are the assessment.

FIELD TYPES
  ('h',    text)                     a section heading
  ('note', text)                     one italic line of guidance under it
  ('box',  n_lines)                  a bordered box the student types into
  ('bul',  [placeholders])           a bulleted list to extend
  ('tbl',  [headers], n_rows)        a table to fill in
  ('rule',)                          a hairline separator
"""

import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'logo', 'header.png')

PURPLE = RGBColor(0x6b, 0x47, 0x85)
INK    = RGBColor(0x14, 0x1c, 0x26)
INK2   = RGBColor(0x3f, 0x4e, 0x5d)
INK3   = RGBColor(0x6d, 0x7c, 0x8a)
RULE   = 'c3d0da'
SOFT   = 'f1ebf7'

TEXT_W = 6.8                  # 8.5in page less two 0.85in margins
TEXT_TWIPS = int(TEXT_W * 1440)
TEXT_EMU = int(TEXT_W * 914400)

SCHOOL = 'Blue Hills Regional Technical School  ·  Room E-126'


# ------------------------------------------------------------------ helpers

def _shade(cell, hexfill):
    el = OxmlElement('w:shd')
    el.set(qn('w:val'), 'clear')
    el.set(qn('w:fill'), hexfill)
    cell._tc.get_or_add_tcPr().append(el)


def _borders(table, colour=RULE, size=4, inside=True):
    tblPr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    edges = ['top', 'left', 'bottom', 'right']
    if inside:
        edges += ['insideH', 'insideV']
    for edge in edges:
        e = OxmlElement('w:' + edge)
        e.set(qn('w:val'), 'single')
        e.set(qn('w:sz'), str(size))
        e.set(qn('w:color'), colour)
        borders.append(e)
    tblPr.append(borders)


def _full_width(table):
    """python-docx leaves a one-column table at its default width, which on
    the page reads as a box that stopped short. Force every fill-in area to
    the full text column."""
    table.autofit = False
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn('w:tblW')):
        tblPr.remove(old)
    w = OxmlElement('w:tblW')
    w.set(qn('w:type'), 'dxa')
    w.set(qn('w:w'), str(TEXT_TWIPS))
    tblPr.append(w)
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    tblPr.append(layout)
    # Word and LibreOffice both prefer explicit cell widths over the table
    # width when the layout is fixed, so set them too.
    n = len(table.columns)
    for col in table.columns:
        for c in col.cells:
            c.width = Emu(int(TEXT_EMU / n))


def _no_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        e = OxmlElement('w:' + edge)
        e.set(qn('w:val'), 'none')
        borders.append(e)
    tblPr.append(borders)


def _run(p, text, size=10.5, bold=False, italic=False, colour=INK,
         font='Calibri'):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = colour
    r.font.name = font
    return r


def _para(container, text='', size=10.5, bold=False, italic=False,
          colour=INK, before=0, after=4, align=None):
    p = container.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    if align is not None:
        p.alignment = align
    if text:
        _run(p, text, size, bold, italic, colour)
    return p


# ------------------------------------------------------------------- chrome

def _page_setup(doc):
    s = doc.sections[0]
    s.top_margin = Inches(0.85)
    s.bottom_margin = Inches(0.7)
    s.left_margin = Inches(0.85)
    s.right_margin = Inches(0.85)
    s.header_distance = Inches(0.35)
    s.footer_distance = Inches(0.3)

    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(4)


def _header(doc):
    hdr = doc.sections[0].header
    t = hdr.add_table(1, 2, Inches(6.8))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _no_borders(t)
    t.columns[0].width = Inches(4.4)
    t.columns[1].width = Inches(2.4)

    left = t.cell(0, 0).paragraphs[0]
    left.paragraph_format.space_after = Pt(0)
    if os.path.exists(LOGO):
        left.add_run().add_picture(LOGO, height=Inches(0.30))
        _run(left, '  ', 9)
    _run(left, 'BHR ENGINEERING TECHNOLOGY', 8.5, bold=True, colour=PURPLE)

    right = t.cell(0, 1).paragraphs[0]
    right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    right.paragraph_format.space_after = Pt(0)
    _run(right, SCHOOL, 7.5, colour=INK3)

    # hairline under the header
    p = hdr.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(0)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single')
    b.set(qn('w:sz'), '8')
    b.set(qn('w:color'), '141c26')
    pbdr.append(b)
    pPr.append(pbdr)


def _footer(doc, docname):
    ftr = doc.sections[0].footer
    p = ftr.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    _run(p, docname, 7.5, colour=INK3)
    _run(p, '\t\t', 7.5)
    _run(p, 'Page ', 7.5, colour=INK3)
    # PAGE field
    r = p.add_run()
    r.font.size = Pt(7.5)
    r.font.color.rgb = INK3
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    r._r.addnext(fld)


def _title(doc, title, standfirst):
    p = _para(doc, title, size=19, bold=True, colour=INK, after=2)
    p.paragraph_format.space_before = Pt(0)
    if standfirst:
        _para(doc, standfirst, size=9.5, italic=True, colour=INK2, after=10)


def _identity(doc, fields):
    """The block at the top of every hand-in: who, when, what."""
    rows = (len(fields) + 1) // 2
    t = doc.add_table(rows=rows, cols=4)
    _borders(t)
    _full_width(t)
    for i, label in enumerate(fields):
        c_label = t.cell(i // 2, (i % 2) * 2)
        c_value = t.cell(i // 2, (i % 2) * 2 + 1)
        _shade(c_label, SOFT)
        p = c_label.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        _run(p, label, 8.5, bold=True, colour=PURPLE)
        c_value.paragraphs[0].paragraph_format.space_after = Pt(2)
        c_value.paragraphs[0].paragraph_format.space_before = Pt(2)
    for i, w in enumerate((1.15, 2.25, 1.15, 2.25)):
        for cell in t.columns[i].cells:
            cell.width = Inches(w)
    _para(doc, '', after=6)


# ------------------------------------------------------------------- fields

def _emit(doc, item):
    kind = item[0]

    if kind == 'h':
        p = _para(doc, item[1], size=11.5, bold=True, colour=PURPLE,
                  before=12, after=2)
        pPr = p._p.get_or_add_pPr()
        pbdr = OxmlElement('w:pBdr')
        b = OxmlElement('w:bottom')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), '4')
        b.set(qn('w:color'), RULE)
        pbdr.append(b)
        pPr.append(pbdr)

    elif kind == 'note':
        _para(doc, item[1], size=9, italic=True, colour=INK2, after=4)

    elif kind == 'box':
        t = doc.add_table(rows=1, cols=1)
        _borders(t)
        _full_width(t)
        cell = t.cell(0, 0)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        _run(p, '', 10.5)
        for _ in range(max(0, item[1] - 1)):
            q = cell.add_paragraph()
            q.paragraph_format.space_after = Pt(3)
        _para(doc, '', after=2)

    elif kind == 'bul':
        for text in item[1]:
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2)
            _run(p, text, 10.5, colour=INK3 if text.startswith('…')
                 else INK)

    elif kind == 'tbl':
        heads, nrows = item[1], item[2]
        t = doc.add_table(rows=nrows + 1, cols=len(heads))
        _borders(t)
        _full_width(t)
        for i, h in enumerate(heads):
            c = t.cell(0, i)
            _shade(c, SOFT)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            _run(p, h, 8.5, bold=True, colour=PURPLE)
        for r in range(1, nrows + 1):
            for i in range(len(heads)):
                pp = t.cell(r, i).paragraphs[0]
                pp.paragraph_format.space_before = Pt(3)
                pp.paragraph_format.space_after = Pt(3)
        _para(doc, '', after=2)

    elif kind == 'rule':
        _para(doc, '', after=2)


def build(spec, outdir):
    doc = Document()
    _page_setup(doc)
    _header(doc)
    _footer(doc, spec['name'])
    _title(doc, spec['title'], spec.get('standfirst', ''))
    _identity(doc, spec['identity'])
    for item in spec['body']:
        _emit(doc, item)
    path = os.path.join(outdir, spec['file'])
    doc.save(path)
    return path
