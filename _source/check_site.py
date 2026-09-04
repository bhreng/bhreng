#!/usr/bin/env python3
"""Integrity check for the built site. Run after every build.

Strips <script> and <style> before looking for links, because the search code
contains href= inside a JavaScript string and that is not a link.
"""
import os, re, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')


def markup(html):
    html = re.sub(r'<script\b.*?</script>', '', html, flags=re.S | re.I)
    return re.sub(r'<style\b.*?</style>', '', html, flags=re.S | re.I)


def main():
    os.chdir(OUT)
    pages = [os.path.join(r, f)[2:] for r, d, g in os.walk('.')
             for f in g if f.endswith('.html')]
    bad, linked = [], set()
    for p in pages:
        root = os.path.dirname(p) or '.'
        h = markup(open(p, encoding='utf-8').read())
        for l in re.findall(r'(?:href|src)="(?!https?:|mailto:|data:|#)([^"]+)"', h):
            t = os.path.normpath(os.path.join(root, l.split('#')[0].split('?')[0]))
            linked.add(t)
            if not os.path.exists(t):
                bad.append((p, l))
    # 404.html is reached by the server, never by a link -- being unlinked is
    # the whole point of it.
    orphans = sorted(set(pages) - linked - {'index.html', '404.html'})
    print('%d pages, %d broken links, %d orphans' % (len(pages), len(bad), len(orphans)))
    for p, l in bad:
        print('  BROKEN %s -> %s' % (p, l))
    for o in orphans:
        print('  ORPHAN %s' % o)
    return 1 if bad or orphans else 0


if __name__ == '__main__':
    sys.exit(main())
