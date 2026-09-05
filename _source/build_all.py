#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild everything, in order, from this folder alone.

    python3 build_all.py            everything
    python3 build_all.py site       just the website
    python3 build_all.py docs       just the student documents
    python3 build_all.py admin      just the teacher/admin PDFs

Order matters: the student documents are copied into the site as downloads,
so they build first; the admin PDFs pull the hub report that the site build
regenerates, so they build last.

Needs: python3 with python-docx, openpyxl, reportlab, markdown, Pillow;
node with playwright (for the admin PDFs only -- everything else builds
without it). See requirements.txt and HANDOFF.md.
"""

import os
import sys
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)


def run(script, label):
    print('\n== %s (%s)' % (label, script))
    r = subprocess.run([sys.executable, script], capture_output=True, text=True)
    tail = (r.stdout.strip().splitlines() or [''])[-1]
    if r.returncode != 0:
        print(r.stdout[-2000:])
        print(r.stderr[-2000:])
        raise SystemExit('FAILED: ' + script)
    print('   ' + tail)


def docs():
    run('make_student_docs.py', 'student templates (.docx / .xlsx)')
    run('make_docs_guide.py', 'Which document, and when')
    run('make_families_handout.py', 'families handout')
    run('make_pathway_record.py', 'Independent Focus record')
    run('make_rubrics.py', 'rubrics (.xlsx for Classroom, .pdf for students)')
    run('make_posters.py', 'posters')
    # stage every built document as a site download
    att = os.path.join(HERE, 'attachments')
    os.makedirs(att, exist_ok=True)
    for f in os.listdir(att):
        os.remove(os.path.join(att, f))
    n = 0
    for f in os.listdir(os.path.join(HERE, 'student-docs')):
        if f.endswith(('.docx', '.xlsx', '.pdf')):
            shutil.copy2(os.path.join(HERE, 'student-docs', f),
                         os.path.join(att, f))
            n += 1
    print('   %d documents staged for the site' % n)


def site():
    run('build_hubs.py', 'pathway hubs (also writes eep-guides.html)')
    run('build_site.py', 'website')
    run('check_site.py', 'link check')


def admin():
    run('make_admin_pdfs.py', 'teacher and admin PDFs')


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('all', 'docs'):
        docs()
    if what in ('all', 'site'):
        site()
    if what in ('all', 'admin'):
        admin()
    print('\ndone.')
