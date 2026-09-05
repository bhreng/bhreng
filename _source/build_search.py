# -*- coding: utf-8 -*-
"""
Builds the site-wide search index.

Everything is static: the index is emitted as a .js file that assigns a global,
NOT as .json, because a page opened from disk (file://) cannot fetch() a local
file -- the browser blocks it as cross-origin. A <script src> works everywhere,
which keeps the promise that the site runs identically off disk, off GitHub
Pages and off GitLab Pages.
"""

import json
import re

import build_hubs as B
import pathway_sources as PS
import resources_data as RD
import safety_data as SD
import equipment_data as EQ
import grade_data as GD
import grade_work as GW
import staff_data as STF
import extras_data as ED
import brief_text as BT
import shop_projects as SP

TOPIC_NAMES = {
    'field': 'Explore the Field',
    'learn': 'Learn the Concepts',
    'skills': 'Build Your Skills',
    'build': 'Find a Project',
    'files': 'Get the Files',
}

KIND_LABEL = {
    'video': 'Video', 'course': 'Course', 'site': 'Site', 'tool': 'Tool',
    'read': 'Reading', 'podcast': 'Podcast', 'book': 'Book', 'data': 'Data',
    'comp': 'Competition', 'software': 'Software', 'page': 'Page',
    'rule': 'Rule', 'check': 'Safety check', 'platform': 'Training',
    'sds': 'Safety data', 'pathway': 'Pathway',
    'unit': 'Unit', 'assignment': 'Assignment', 'donow': 'Do Now',
    'run': 'Project (run before)',
    'link': 'Link', 'ask': 'Ask about',
}


def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    s = (s.replace('&mdash;', '—').replace('&rsquo;', '’').replace('&ldquo;', '“')
          .replace('&rdquo;', '”').replace('&nbsp;', ' ').replace('&amp;', '&')
          .replace('&middot;', '·').replace('&le;', '≤').replace('&deg;', '°')
          .replace('&hellip;', '…').replace('&times;', '×'))
    return re.sub(r'\s+', ' ', s).strip()


def build():
    rows = []

    def add(title, url, where, kind, note='', ext=''):
        rows.append({
            't': clean(title)[:120],
            'u': url,
            'w': clean(where)[:60],
            'k': kind,
            'n': clean(note)[:150],
            'x': clean(ext)[:120],
        })

    # --- the fixed pages -------------------------------------------------
    for title, url, where, note in [
        ('The Shop Hub', 'index.html', 'Home', 'Everything for Engineering Technology in one place.'),
        ('Welcome to the shop', 'start/welcome.html', 'Start here',
         'Who to ask for what, what to wear, what you can earn, safety essentials.'),
        ('How this class works', 'start/how-class-works.html', 'Start here',
         'Classroom rules, uniform, and exactly how the grade is calculated.'),
        ('Your engineering logbook', 'logbook/index.html', 'Logbook',
         'Status codes, the three intervals, the rules, and a worked example.'),
        ('Pick your pathway', 'pathways/index.html', 'Pathways',
         'The chooser, and how the seven hubs are organised.'),
        ('Shop safety', 'shop/index.html', 'Safety', 'The safety hub.'),
        ('Makerspace rules', 'shop/makerspace.html', 'Safety',
         'All thirty-two rules, in five groups, with a self-check.'),
        ('Equipment checks', 'shop/equipment.html', 'Safety',
         'One safety check per machine or tool group.'),
        ('Safe and appropriate technology use', 'shop/technology.html', 'Safety',
         'Scanning, cameras, AI, licences and accounts.'),
        ('3D printer certification', 'shop/3d-printing.html', 'Safety',
         'Three access levels across the A1 Mini, X1C and H2D.'),
        ('Safety data sheets', 'shop/sds.html', 'Safety',
         'The SDS library, and how to read a sheet when you need one.'),
        ('Which theme?', 'shop/themes.html', 'Safety',
         'Practice for the shop safety test.'),
        ('Training and credentials', 'resources/index.html', 'Training',
         'Every platform and credential the shop uses or recommends.'),
        ('What engineering actually is', 'start/engineering.html', 'Start here',
         'The design process, the seven roles, and what the job really is.'),
        ('The engineering design process', 'start/engineering.html#process',
         'Start here', 'The eight steps, and what each one has to leave behind.'),
        ('The seven roles of an engineer', 'start/engineering.html#roles',
         'Start here', 'What each role does and what it has to produce.'),
        ('Find your year', 'grades/index.html', 'Your year',
         'The four grade homes: who delivers each year and what it holds.'),
        ('Do Nows and bonus work', 'extras/do-nows.html', 'More',
         'Short skill tasks and the assignments outside the project spine.'),
        ('Links', 'extras/links.html', 'More',
         'Reference, channels, model libraries and career data.'),
    ]:
        add(title, url, where, 'page', note)

    # --- the four grade homes, and every assignment on them --------------
    for g in GD.GRADES:
        add('Grade %d \u2014 %s' % (g['num'], g['course']),
            'grades/%s.html' % g['key'], 'Your year', 'page',
            g['lede'], g['teacher'])
        for i, (ut, _ud) in enumerate(g['units'], 1):
            add(ut, 'grades/%s.html' % g['key'],
                'Grade %d unit %d' % (g['num'], i), 'unit', '', g['course'])
        gb = BT.briefs(g['key'])
        for a in GW.WORK.get(g['key'], []):
            term = ('Term %s' % a['t']) if isinstance(a['t'], int) else \
                   ('End of year' if a['t'] == 'eoy' else 'All year')
            add(a['title'], 'grades/%s.html#term-%s' % (g['key'], a['t']),
                'Grade %d \u00b7 %s' % (g['num'], term),
                'assignment', a['hook'],
                ('Full brief \u00b7 ' if a['title'] in gb else '') + a['tool'])

    # --- the two instructors ---------------------------------------------
    for st in STF.STAFF:
        add(st['name'], 'staff/%s.html' % st['key'], 'Your instructors',
            'page', st['blurb'],
            '%s \u00b7 Grades %s' % (st['axis'],
                                      ' and '.join(str(g) for g in st['grades'])))
        for c in st['covers']:
            add(c, 'staff/%s.html' % st['key'], st['name'], 'ask', '', st['axis'])

    # --- Do Nows, bonus work, and the links shelf ------------------------
    for grp in ED.GROUPS:
        for title, tool, desc, grade, _p in grp['items']:
            add(title, 'extras/do-nows.html#%s' % grp['key'],
                'Grade %s \u00b7 %s' % (grade, grp['title']), 'donow',
                desc, tool)
    for grp in ED.LINKS:
        for title, url, desc in grp['items']:
            add(title, 'extras/links.html', grp['title'], 'link', desc,
                url.split('//')[-1].split('/')[0].replace('www.', ''))

    # --- the seven pathways ----------------------------------------------
    for p in B.P:
        add(p['title'], 'pathways/%s.html' % p['key'], 'Pathway ' + p['std'],
            'pathway', p.get('tag', ''), p.get('lead', ''))

    # --- briefs the shop has really run, offered in the hubs -------------
    for pkey, runs in SP.RUNS.items():
        nav = next((x['nav'] for x in B.P if x['key'] == pkey), pkey)
        for y, title, desc in runs:
            add(title, 'pathways/%s.html' % pkey,
                '%s \u00b7 already run' % nav, 'run', desc, y)
    add('Exploratory week', 'grades/9.html#exploratory', 'Grade 9', 'page',
        SP.EXPLORATORY['lede'], 'Two mini exploratory days, eighteen shops, nine week-long visits')

    # --- every verified source -------------------------------------------
    for key in ('architecture', 'automation', 'mechanical', 'industrial',
                'electrical', 'software', 'project'):
        path = next((x for x in B.P if x['key'] == key), None)
        pname = path['nav'] if path else key
        for topic in ('field', 'learn', 'skills', 'build', 'files'):
            for r in PS.by(key, topic):
                add(r['title'], r['url'], '%s · %s' % (pname, TOPIC_NAMES[topic]),
                    r.get('kind', 'site'), r.get('note', ''))

    # --- training platforms ----------------------------------------------
    for r in RD.R:
        add(r['name'], r['url'], 'Training', 'platform',
            r.get('what', ''), r.get('note', ''))

    # --- the ten primary rules -------------------------------------------
    for r in SD.PRIMARY_RULES:
        add(r, 'shop/makerspace.html', 'Primary rule', 'rule',
            'A condition of entry to the Makerspace.')
    for term, meaning in SD.TRAINED_AUTHORIZED:
        add(term + ' (Makerspace)', 'shop/makerspace.html', 'Primary rule 8',
            'rule', meaning)

    # --- every Makerspace rule -------------------------------------------
    for group, when, items in SD.MAKERSPACE_RULES:
        for it in items:
            add(it, 'shop/makerspace.html', 'Makerspace rule · ' + clean(group),
                'rule', when)

    # --- the equipment checks --------------------------------------------
    for key, name, group, blurb, has in EQ.EQUIPMENT:
        if has:
            add(name, 'shop/check-%s.html' % key, 'Safety check · ' + group,
                'check', blurb)

    # --- SDS categories ---------------------------------------------------
    for name, fid, desc in SD.SDS_FOLDERS if hasattr(SD, 'SDS_FOLDERS') else []:
        add(name + ' safety data sheets', 'shop/sds.html', 'Safety data',
            'sds', desc)

    return rows


def emit(path):
    rows = build()
    js = 'window.BHR_INDEX=%s;' % json.dumps(rows, ensure_ascii=False,
                                             separators=(',', ':'))
    open(path, 'w', encoding='utf-8').write(js)
    return rows, len(js)
