# -*- coding: utf-8 -*-
"""Build the student hand-in set.

    python3 make_student_docs.py

Ten Word documents and three spreadsheets, into ./student-docs/.

Word and Excel because these are the ones students TYPE INTO. Upload a
.docx to Drive and Google converts it to a Doc; upload an .xlsx and it
becomes a Sheet. Everything else the shop hands out is a PDF, because
nobody types into it.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import student_docs as SD

def _unent(v):
    """The data file is shared with the website builders, which want HTML
    entities. Word wants the characters."""
    if isinstance(v, str):
        for a, b in (('&amp;', '&'), ('&rsquo;', '\u2019'),
                     ('&mdash;', '\u2014'), ('&ldquo;', '\u201c'),
                     ('&rdquo;', '\u201d'), ('&hellip;', '\u2026')):
            v = v.replace(a, b)
        return v
    if isinstance(v, (list, tuple)):
        return type(v)(_unent(x) for x in v)
    if isinstance(v, dict):
        return {k: _unent(x) for k, x in v.items()}
    return v

import student_doc_data as DATA

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'student-docs')

PURPLE = '6B4785'
SOFT = 'F1EBF7'
RULE = 'C3D0DA'
INK = '141C26'
INK3 = '6D7C8A'

THIN = Side(style='thin', color=RULE)
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def _sheet_head(ws, title, subtitle, ncols):
    ws['A1'] = 'BHR ENGINEERING TECHNOLOGY'
    ws['A1'].font = Font(name='Calibri', size=8.5, bold=True, color=PURPLE)
    ws['A2'] = title
    ws['A2'].font = Font(name='Calibri', size=16, bold=True, color=INK)
    ws['A3'] = subtitle
    ws['A3'].font = Font(name='Calibri', size=9.5, italic=True, color='3F4E5D')
    for r in (1, 2, 3):
        ws.merge_cells(start_row=r, start_column=1, end_row=r,
                       end_column=ncols)
    ws.row_dimensions[2].height = 22
    ws.freeze_panes = 'A1'


def _header_row(ws, row, headers, widths):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = Font(name='Calibri', size=9, bold=True, color=PURPLE)
        c.fill = PatternFill('solid', fgColor=SOFT)
        c.border = BOX
        c.alignment = Alignment(vertical='center', wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = widths[i - 1]
    ws.row_dimensions[row].height = 26


def _blank_rows(ws, first, last, ncols, height=20):
    for r in range(first, last + 1):
        ws.row_dimensions[r].height = height
        for i in range(1, ncols + 1):
            ws.cell(row=r, column=i).border = BOX


def _identity_rows(ws, row, fields):
    for i, label in enumerate(fields):
        c = ws.cell(row=row + i, column=1, value=label)
        c.font = Font(name='Calibri', size=9, bold=True, color=PURPLE)
        c.fill = PatternFill('solid', fgColor=SOFT)
        c.border = BOX
        v = ws.cell(row=row + i, column=2)
        v.border = BOX
    return row + len(fields) + 1


# ------------------------------------------------------------- research log
def research_log(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Research Log'
    heads = ['Date', 'Source type', 'Why this source',
             'Source (author, title, year)', 'Link', 'What you took from it']
    widths = [11, 15, 20, 38, 34, 44]
    _sheet_head(ws, 'Research Log',
                'One new source a day is the target. In brainstorming and '
                'research it should be more than that.', len(heads))
    _identity_rows(ws, 5, ['Name', 'Project'])
    ws.column_dimensions['A'].width = widths[0]
    _header_row(ws, 9, heads, widths)
    _blank_rows(ws, 10, 90, len(heads))

    lists = wb.create_sheet('Lists')
    lists['A1'] = 'Source type'
    lists['B1'] = 'Why this source'
    for c in ('A1', 'B1'):
        lists[c].font = Font(bold=True, color=PURPLE)
    types = ['Article', 'Book', 'Web video', 'TV or film', 'Podcast',
             'Datasheet or manual', 'Standard or code', 'Patent',
             'Person I spoke to', 'Misc.']
    reasons = ['Technical — skill', 'Educational — knowledge',
               'Informational', 'Inspirational', 'Motivational']
    for i, v in enumerate(types, start=2):
        lists.cell(row=i, column=1, value=v)
    for i, v in enumerate(reasons, start=2):
        lists.cell(row=i, column=2, value=v)
    lists.column_dimensions['A'].width = 24
    lists.column_dimensions['B'].width = 26

    dv1 = DataValidation(type='list',
                         formula1='=Lists!$A$2:$A$%d' % (len(types) + 1),
                         allow_blank=True)
    dv2 = DataValidation(type='list',
                         formula1='=Lists!$B$2:$B$%d' % (len(reasons) + 1),
                         allow_blank=True)
    ws.add_data_validation(dv1)
    ws.add_data_validation(dv2)
    dv1.add('B10:B90')
    dv2.add('C10:C90')
    wb.save(path)


# --------------------------------------------------------- order request form
def order_request(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Order Request'
    heads = ['Qty', 'Item description', 'Unit cost', 'Total cost',
             'Why you need it', 'Vendor link', 'Alternative link']
    widths = [6, 40, 11, 11, 40, 34, 34]
    _sheet_head(ws, 'Order Request Form',
                'One row per item. The "why you need it" column is the one '
                'that gets the order approved.', len(heads))
    nxt = _identity_rows(ws, 5, ['Name', 'Project', 'Date submitted'])
    ws.column_dimensions['A'].width = widths[0]
    ws.column_dimensions['B'].width = widths[1]
    hrow = 10
    _header_row(ws, hrow, heads, widths)
    _blank_rows(ws, hrow + 1, hrow + 25, len(heads))
    for r in range(hrow + 1, hrow + 26):
        ws.cell(row=r, column=4).value = '=IF(A%d="","",A%d*C%d)' % (r, r, r)
        ws.cell(row=r, column=3).number_format = '$#,##0.00'
        ws.cell(row=r, column=4).number_format = '$#,##0.00'
    tot = hrow + 27
    c = ws.cell(row=tot, column=3, value='Total')
    c.font = Font(name='Calibri', size=10, bold=True, color=PURPLE)
    c.alignment = Alignment(horizontal='right')
    t = ws.cell(row=tot, column=4,
                value='=SUM(D%d:D%d)' % (hrow + 1, hrow + 25))
    t.font = Font(name='Calibri', size=11, bold=True, color=INK)
    t.number_format = '$#,##0.00'
    t.border = BOX
    ws.cell(row=tot + 2, column=1,
            value='Approved by: ________________________     '
                  'Date: ____________     PO / account: ____________'
            ).font = Font(name='Calibri', size=9, color=INK3)
    wb.save(path)


# ---------------------------------------------------------------- gantt chart
def gantt(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Gantt'
    heads = ['WBS', 'Task title', 'Work type', 'Status', 'Start', 'Due',
             'Days']
    widths = [7, 34, 15, 14, 11, 11, 7]
    WEEKS = 10
    ncols = len(heads) + WEEKS * 5
    _sheet_head(ws, 'Project Gantt Chart',
                'Break the project into tasks, then put them on a calendar. '
                'The point is to find out where two tasks collide.', 12)

    nxt = _identity_rows(ws, 5, ['Project title', 'Project manager'])

    hrow = 9
    # week banner across the day columns
    for w in range(WEEKS):
        first = len(heads) + 1 + w * 5
        ws.merge_cells(start_row=hrow - 1, start_column=first,
                       end_row=hrow - 1, end_column=first + 4)
        c = ws.cell(row=hrow - 1, column=first, value='Week %d' % (w + 1))
        c.font = Font(name='Calibri', size=9, bold=True, color=PURPLE)
        c.alignment = Alignment(horizontal='center')
        c.fill = PatternFill('solid', fgColor=SOFT)

    _header_row(ws, hrow, heads, widths)
    for w in range(WEEKS):
        for i, d in enumerate(['M', 'T', 'W', 'R', 'F']):
            col = len(heads) + 1 + w * 5 + i
            c = ws.cell(row=hrow, column=col, value=d)
            c.font = Font(name='Calibri', size=8, bold=True, color=PURPLE)
            c.fill = PatternFill('solid', fgColor=SOFT)
            c.border = BOX
            c.alignment = Alignment(horizontal='center')
            ws.column_dimensions[get_column_letter(col)].width = 3.2

    seed = [
        ('1', 'Initiating', '', '', '', '', ''),
        ('1.1', 'Define the problem', 'Research', 'Not started', '', '', ''),
        ('1.2', 'Create design requirements', 'Written', 'Not started',
         '', '', ''),
        ('2', 'Planning', '', '', '', '', ''),
        ('2.1', 'Scope and goal setting', 'Brainstorming', 'Not started',
         '', '', ''),
        ('3', 'Design', '', '', '', '', ''),
        ('3.1', 'Conceptual design', 'Drawing', 'Not started', '', '', ''),
        ('3.2', 'Detailed design', 'CAD', 'Not started', '', '', ''),
        ('4', 'Development', '', '', '', '', ''),
        ('4.1', 'Build the prototype', 'Construction', 'Not started',
         '', '', ''),
        ('4.2', 'Test and evaluate', 'Model', 'Not started', '', '', ''),
        ('4.3', 'Optimise and redesign', 'CAD', 'Not started', '', '', ''),
        ('5', 'Closing', '', '', '', '', ''),
        ('5.1', 'Presentation', 'Written', 'Not started', '', '', ''),
    ]
    r = hrow + 1
    for row in seed:
        for i, v in enumerate(row, start=1):
            c = ws.cell(row=r, column=i, value=v or None)
            c.border = BOX
            if not row[2] and i <= 2:          # a phase heading row
                c.font = Font(name='Calibri', size=10, bold=True, color=INK)
                c.fill = PatternFill('solid', fgColor=SOFT)
        for i in range(len(heads) + 1, ncols + 1):
            ws.cell(row=r, column=i).border = BOX
        ws.row_dimensions[r].height = 18
        r += 1
    for extra in range(16):
        for i in range(1, ncols + 1):
            ws.cell(row=r, column=i).border = BOX
        ws.row_dimensions[r].height = 18
        r += 1
    last = r - 1

    for rr in range(hrow + 1, last + 1):
        ws.cell(row=rr, column=5).number_format = 'm/d/yy'
        ws.cell(row=rr, column=6).number_format = 'm/d/yy'
        ws.cell(row=rr, column=7).value = (
            '=IF(OR(E%d="",F%d=""),"",F%d-E%d+1)' % (rr, rr, rr, rr))

    lists = wb.create_sheet('Lists')
    lists['A1'] = 'Work type'
    lists['B1'] = 'Status'
    for c in ('A1', 'B1'):
        lists[c].font = Font(bold=True, color=PURPLE)
    types = ['Research', 'Brainstorming', 'Drawing', 'CAD', 'Model',
             'Written', 'Construction', 'Testing', 'Learn']
    stat = ['Not started', 'In progress', 'Blocked', 'Complete']
    for i, v in enumerate(types, start=2):
        lists.cell(row=i, column=1, value=v)
    for i, v in enumerate(stat, start=2):
        lists.cell(row=i, column=2, value=v)
    lists.column_dimensions['A'].width = 20
    lists.column_dimensions['B'].width = 18

    dv1 = DataValidation(type='list',
                         formula1='=Lists!$A$2:$A$%d' % (len(types) + 1),
                         allow_blank=True)
    dv2 = DataValidation(type='list',
                         formula1='=Lists!$B$2:$B$%d' % (len(stat) + 1),
                         allow_blank=True)
    ws.add_data_validation(dv1)
    ws.add_data_validation(dv2)
    dv1.add('C%d:C%d' % (hrow + 1, last))
    dv2.add('D%d:D%d' % (hrow + 1, last))
    ws.freeze_panes = ws.cell(row=hrow + 1, column=len(heads) + 1)
    wb.save(path)


# ------------------------------------------------------------------ part list
def part_list(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Part List'
    heads = ['Item', 'Part name', 'Qty', 'Material or spec',
             'Made or bought', 'Source / part number', 'Unit cost',
             'Total', 'Notes']
    widths = [6, 32, 6, 26, 15, 30, 11, 11, 34]
    _sheet_head(ws, 'Part List',
                'Every part in the design, including the fasteners. If it is '
                'not on this list it does not exist when you go to build.',
                len(heads))
    _identity_rows(ws, 5, ['Name', 'Project', 'Revision', 'Date'])
    hrow = 11
    _header_row(ws, hrow, heads, widths)
    last = hrow + 40
    _blank_rows(ws, hrow + 1, last, len(heads))
    for r in range(hrow + 1, last + 1):
        ws.cell(row=r, column=1).value = r - hrow
        ws.cell(row=r, column=1).font = Font(name='Calibri', size=9,
                                             color=INK3)
        ws.cell(row=r, column=8).value = (
            '=IF(OR(C%d="",G%d=""),"",C%d*G%d)' % (r, r, r, r))
        ws.cell(row=r, column=7).number_format = '$#,##0.00'
        ws.cell(row=r, column=8).number_format = '$#,##0.00'

    tot = last + 2
    c = ws.cell(row=tot, column=7, value='Total')
    c.font = Font(name='Calibri', size=10, bold=True, color=PURPLE)
    c.alignment = Alignment(horizontal='right')
    t = ws.cell(row=tot, column=8,
                value='=SUM(H%d:H%d)' % (hrow + 1, last))
    t.font = Font(name='Calibri', size=11, bold=True, color=INK)
    t.number_format = '$#,##0.00'
    t.border = BOX

    ws.cell(row=tot + 2, column=1,
            value='Count the fasteners. A part list that says "screws" '
                  'instead of "M3 x 12 socket head, 8 off" is not finished.'
            ).font = Font(name='Calibri', size=9, italic=True, color=INK3)

    lists = wb.create_sheet('Lists')
    lists['A1'] = 'Made or bought'
    lists['A1'].font = Font(bold=True, color=PURPLE)
    kinds = ['Make — 3D print', 'Make — laser', 'Make — CNC',
             'Make — hand/shop', 'Buy — stock', 'Buy — order',
             'Reuse — salvaged']
    for i, v in enumerate(kinds, start=2):
        lists.cell(row=i, column=1, value=v)
    lists.column_dimensions['A'].width = 22
    dv = DataValidation(type='list',
                        formula1='=Lists!$A$2:$A$%d' % (len(kinds) + 1),
                        allow_blank=True)
    ws.add_data_validation(dv)
    dv.add('E%d:E%d' % (hrow + 1, last))
    ws.freeze_panes = ws.cell(row=hrow + 1, column=1)
    wb.save(path)


SHEETS = [
    ('BHR-ENG-Research-Log.xlsx', research_log),
    ('BHR-ENG-Order-Request-Form.xlsx', order_request),
    ('BHR-ENG-Project-Gantt-Chart.xlsx', gantt),
    ('BHR-ENG-Part-List.xlsx', part_list),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []
    for spec in DATA.DOCS:
        made.append(SD.build(_unent(spec), OUT))
    for name, fn in SHEETS:
        p = os.path.join(OUT, name)
        fn(p)
        made.append(p)
    for p in made:
        print('  %-56s %7d' % (os.path.basename(p), os.path.getsize(p)))
    print('\n%d files -> %s' % (len(made), OUT))


if __name__ == '__main__':
    main()
