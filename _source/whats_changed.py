#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""What do I have to drag to GitHub this time?

    python3 whats_changed.py          list files changed since the last mark
    python3 whats_changed.py --mark   record the site as it is now (do this
                                      right after the site has been uploaded)

Compares every file in site/ against a snapshot of hashes taken at the last
--mark (.last-shipped.json, next to this script). Prints the changed files
grouped by folder and writes the same list to WHAT-CHANGED.txt, with a
suggestion of what to drag: whole folders when most of a folder changed,
single files when not. GitHub's web upload takes at most 100 files per drag.
"""

import os
import sys
import json
import hashlib
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, 'site')
SNAP = os.path.join(HERE, '.last-shipped.json')
OUT = os.path.join(HERE, 'WHAT-CHANGED.txt')


def scan():
    d = {}
    for root, dirs, files in os.walk(SITE):
        for f in files:
            fp = os.path.join(root, f)
            rp = os.path.relpath(fp, SITE).replace(os.sep, '/')
            with open(fp, 'rb') as fh:
                d[rp] = hashlib.sha1(fh.read()).hexdigest()
    return d


def main():
    now = scan()
    if '--mark' in sys.argv:
        with open(SNAP, 'w') as f:
            json.dump(now, f, indent=0, sort_keys=True)
        print('marked %d files as shipped' % len(now))
        return
    old = json.load(open(SNAP)) if os.path.exists(SNAP) else {}
    if not old:
        print('no snapshot yet -- everything is new. Upload the whole site, '
              'then run  python3 whats_changed.py --mark')
        return
    changed = sorted(p for p in now if old.get(p) != now[p])
    gone = sorted(p for p in old if p not in now)

    by = defaultdict(list)
    for p in changed:
        by[os.path.dirname(p) or '(root)'].append(p)
    totals = defaultdict(int)
    for p in now:
        totals[os.path.dirname(p) or '(root)'] += 1

    lines = ['WHAT TO DRAG TO GITHUB', '%d changed, %d removed' % (len(changed), len(gone)), '']
    drag = []
    for folder in sorted(by):
        n, t = len(by[folder]), totals[folder]
        if folder != '(root)' and n >= max(3, t * 0.6):
            drag.append(('folder', folder, n))
        else:
            for p in by[folder]:
                drag.append(('file', p, 1))
        lines.append('%s  (%d of %d files)' % (folder, n, t))
        lines += ['   ' + os.path.basename(p) for p in by[folder]]
        lines.append('')
    lines.append('SUGGESTED DRAGS (each 100 files or fewer):')
    batch, count = [], 0
    for kind, name, n in drag:
        if count + n > 100 and batch:
            lines.append('   drag: ' + ', '.join(batch)); batch, count = [], 0
        batch.append(name + ('/' if kind == 'folder' else '')); count += n
    if batch:
        lines.append('   drag: ' + ', '.join(batch))
    if gone:
        lines += ['', 'REMOVED (delete these on GitHub, or leave them -- they are harmless):']
        lines += ['   ' + p for p in gone]
    lines += ['', 'When the upload is done:  python3 whats_changed.py --mark']
    text = '\n'.join(lines)
    print(text)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    main()
