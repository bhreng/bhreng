# -*- coding: utf-8 -*-
"""Full assignment briefs, converted from the Classroom harvests.

The point of this module is that NOBODY RETYPES A BRIEF. The harvest files hold
what Classroom actually says; this parses them into HTML and the grade pages
render it. If a brief is re-harvested, the site follows automatically, and
there is no second copy to drift.

What gets stripped on the way through, deliberately:

  * Blockquotes. Every "> ..." line in the harvest is my own commentary written
    for Dan, not instructions written for a student. None of it belongs on a
    student-facing page.
  * Live codes. The Arduino class and activation codes and the Gmetrix join
    code are replaced with a line telling the student to get them from
    Classroom. A public page must never carry them.
  * The posting-date line. "Posted 8 Sep 2025" is true of last year's copy and
    misleading on a reference page.
  * The harvest's own header and its trailing meta sections.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# harvest heading  ->  the assignment title used in grade_work.py
MAP_11 = {
    'Term 1 Week 1 — Speaker Design': 'Speaker Design',
    'Term 1 Week 2 — Roles of an Engineer': 'Roles of an Engineer',
    'Term 1 Weeks 2–4 — Full Scope Project': 'Full Scope Project',
    'Term 1 Week 3 — Tiny House': 'Tiny House',
    'Term 2 Week 1 — ADU Design Project': 'ADU Design Project',
    'Term 2 Week 2 — Intro to ESEC: Arduino': 'Intro to ESEC: Arduino',
    'Term 2 Week 3 — VEX V5 Clawbot Project': 'VEX V5 Clawbot Project',
    'Term 2 Week 3 — Intro to CorelDraw': 'Intro to CorelDraw',
    'Term 2 Week 4 — Simple Machines to Functional Mechanisms':
        'Simple Machines to Functional Mechanisms',
    'Term 2 Week 5 — Robotic Arm Build': 'Robotic Arm Build',
    'Term 2 Week 5 — Elegoo Uno Project Kit': 'Elegoo Uno Project Kit',
    'Term 3 Week 2 — Creative Concept Design': 'Creative Concept Design',
    'Term 3 Weeks 3–4 — City Design': 'City Design',
    'Term 3 Week 4 — Learning Revit!': 'Learning Revit!',
    'Term 4 Week 1 — Famous Architect Presentation':
        'Famous Architect Presentation',
    'Term 4 Week 3 — Fusion Review: Drawings and Stress Simulations':
        'Fusion Review: Drawings and Stress Simulations',
    'Term 4 Week 5 — End-of-Year Vibecoding Team Challenge':
        'The End-of-Year Vibecoding Team Challenge',
    'End of year — Grade 11 Capstone': 'Grade 11 Capstone',
    'Final — Reflection Portfolio Presentation':
        'Reflection Portfolio Presentation',
    'Final — Gmetrix': 'Gmetrix',
    'Running all year — Independent Study Project':
        'Independent Focus',
}

MAP_12 = {
    'Term 1 Week 1 — Design a Laptop': 'Design a Laptop',
    'Term 1 Weeks 2–5 — Shop Equipment Project': 'Shop Equipment Project',
    'Term 1 Week 5 — Post-Lecture Reflection: Theory of the Week':
        'Post-Lecture Reflection: Theory of the Week',
    'Term 2 Week 1 — Industrial Design Challenge: The LED Desk Lamp':
        'Industrial Design Challenge: The LED Desk Lamp',
    'Term 2 Week 2 — Try Again! Moon Base 2.0': 'Try Again! Moon Base 2.0',
    'Term 2 Week 2 — Research & Analysis: The LTT Screwdriver':
        'Research &amp; Analysis: LTT Screwdriver',
    'Term 2 Week 3 — Intro to CorelDraw': 'Intro to CorelDraw',
    'Term 2 Week 3 — VEX Robotics': 'VEX Robotics',
    'Term 2 Week 5 — Mars Colony Design': 'Mars Colony Design',
    'Term 2 Week 5 — Bunker House Design': 'Bunker House Design',
    'Term 2 Week 5 through Term 4 — Senior Capstone': 'Senior Capstone',
    'Running all year — Independent Study': 'Independent Focus',
    'Running all year — Platform training': 'Platform training',
}

# headings that are notes to Dan rather than assignments
SKIP = (
    'Do Nows — an important structural finding',
    'What is still missing from this class',
    'A note on the other classes',
    'Independent Study — 3D Printer Shop Training: The Bambu Lab Academy',
    'Welcome to Engineering III — materials',
    'The missing words — a real problem in Classroom, not in this harvest',
    'What was not found',
    'Term 3 Week 1 — Final Concepts and Ideas for Senior Capstone',
    'Term 3 — Senior Capstone: Research Log',
    'Welcome — VEX AIM Bot: Guided Lessons',
    'Welcome — Universal Robots e-Learning',
    'Senior Capstone Week 5 — Stratasys Academy Online Learning',
)

# text that must not reach a public page, and what replaces it
REDACT = [
    (re.compile(r'Opens with three setup lines.*?in Classroom if you need '
                r'them\.', re.S),
     'Sign up through the under-18 route at '
     '`app.arduino.cc/minors`. The class code and the activation '
     'code are with the assignment in Google Classroom.'),
    (re.compile(r'"create an account\.\.\. join a class [A-Za-z]+-\d+"'),
     'Create an account and join the class. The join code is with the '
     'assignment in Google Classroom.'),
    (re.compile(r'That is the entire description\. The class join code is '
                r'recorded here because it\s+is not a credential — but it '
                r'should not be posted publicly either\.', re.S), ''),
    # Belt and braces. If a live code is ever pasted into a harvest again,
    # it does not reach a public page no matter how the sentence is worded.
    (re.compile(r'\bFrank-\d{4,}\b'), '[join code is in Classroom]'),
    (re.compile(r'\b(?:class|activation)\s+code\s*[:=]\s*\S+', re.I),
     'code is in Classroom'),
    # Retired names, normalised to the current instrument. The brief is
    # otherwise Classroom's wording; a student must not be told to keep a
    # document that no longer exists under that name.
    (re.compile(r'Daily Journal Log', re.I), 'Daily Logbook'),
    (re.compile(r'Engineering Daily Journal', re.I), 'Daily Logbook'),
    (re.compile(r'\bDaily journals\b'), 'Logbook entries'),
    (re.compile(r'\bDaily journal\b'), 'Daily Logbook'),
    (re.compile(r'\bdaily journals\b'), 'logbook entries'),
    (re.compile(r'\bdaily journal\b'), 'daily logbook'),
    (re.compile(r'\bweekly journal\b', re.I), 'weekly logbook summary'),
    (re.compile(r'\bindependent study\b', re.I), 'Independent Focus'),
]

# Paragraphs written for Dan during the harvest, not for a student reading the
# brief. Matched on the whole paragraph so a partial phrase cannot swallow a
# real instruction by accident.
HARVEST_NOTE = re.compile(
    r'^[\s*]*(?:'
    r'Week 1 posted .*'
    r'|The three weekly assignments carry identical.*'
    r'|Harvest in progress.*'
    r'|This matches, word for word in substance.*'
    r'|Two class materials, both posted.*'
    r'|Both are attachment-only.*'
    r')[\s*]*$', re.S)

INLINE = [
    (re.compile(r'`([^`]+)`'), r'<code>\1</code>'),
    (re.compile(r'\*\*([^*]+)\*\*'), r'<strong>\1</strong>'),
    (re.compile(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])'), r'<em>\1</em>'),
]


def _esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _inline(t):
    t = _esc(t)
    # the escape above turned the markdown's own tags into entities; the
    # replacements below re-introduce only the ones we want
    for pat, rep in INLINE:
        t = pat.sub(rep, t)
    return t


def _to_html(body):
    """A deliberately small markdown subset: paragraphs, bullets, tables,
    and bold/italic/code. The harvests do not use anything else."""
    out, buf, mode = [], [], None

    def flush():
        if not buf:
            return
        if mode == 'ul':
            out.append('<ul>%s</ul>'
                       % ''.join('<li>%s</li>' % _inline(x) for x in buf))
        elif mode == 'table':
            rows = [[c.strip() for c in r.strip().strip('|').split('|')]
                    for r in buf]
            rows = [r for r in rows
                    if not all(set(c) <= set('-: ') for c in r)]
            if rows:
                head, rest = rows[0], rows[1:]
                out.append(
                    '<div class="tw"><table><thead><tr>%s</tr></thead>'
                    '<tbody>%s</tbody></table></div>'
                    % (''.join('<th>%s</th>' % _inline(c) for c in head),
                       ''.join('<tr>%s</tr>'
                               % ''.join('<td>%s</td>' % _inline(c) for c in r)
                               for r in rest)))
        else:
            para = ' '.join(buf)
            if not HARVEST_NOTE.match(para):
                out.append('<p>%s</p>' % _inline(para))
        buf.clear()

    lines = body.split('\n')
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush(); mode = None; i += 1; continue
        if stripped.startswith('>'):                     # my commentary
            i += 1; continue
        # an italic line that is only a posting date is harvest metadata
        if re.match(r'^\*(?:Posted|Edited|Draft|Week \d+ posted)\b.*\*?\.?$',
                    stripped):
            i += 1; continue
        if stripped == '---':
            flush(); mode = None; i += 1; continue
        if stripped.startswith('|'):
            if mode != 'table':
                flush(); mode = 'table'
            buf.append(stripped); i += 1; continue
        if re.match(r'^[-*] ', stripped):
            if mode != 'ul':
                flush(); mode = 'ul'
            item = re.sub(r'^[-*] ', '', stripped)
            # a wrapped bullet continues on the following indented lines
            while i + 1 < len(lines) and lines[i + 1].startswith('  ') \
                    and lines[i + 1].strip() \
                    and not re.match(r'^\s*[-*] ', lines[i + 1]):
                i += 1
                item += ' ' + lines[i].strip()
            buf.append(item); i += 1; continue
        if mode not in (None, 'p'):
            flush()
        mode = 'p'
        buf.append(stripped)
        i += 1
    flush()
    return '\n'.join(x for x in out if x.strip())


def _sections(path):
    if not os.path.exists(path):
        return {}
    text = open(path, encoding='utf-8').read()
    for pat, rep in REDACT:
        text = pat.sub(rep, text)
    parts = re.split(r'\n## ', text)
    found = {}
    for part in parts[1:]:
        head, _, body = part.partition('\n')
        head = head.strip()
        if head in SKIP:
            continue
        found[head] = body
    return found


def briefs(grade):
    """{assignment title -> full brief as HTML}"""
    if grade == '11':
        secs = _sections(os.path.join(HERE, 'PROJECT-INSTRUCTIONS-class27.md'))
        mapping = MAP_11
    elif grade == '12':
        secs = _sections(os.path.join(HERE, 'PROJECT-INSTRUCTIONS-class26.md'))
        mapping = MAP_12
    else:
        return {}
    out = {}
    for head, body in secs.items():
        title = mapping.get(head)
        if not title:
            continue
        html = _to_html(body)
        if html.strip():
            out[title] = html
    return out


if __name__ == '__main__':
    b = briefs('11')
    print('%d briefs' % len(b))
    for k in sorted(b):
        print('  %-52s %5d chars' % (k, len(b[k])))
    missing = set(MAP_11.values()) - set(b)
    if missing:
        print('MISSING:', sorted(missing))
