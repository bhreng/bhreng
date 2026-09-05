# -*- coding: utf-8 -*-
"""Where things are, relative to this folder. Nothing in the builders should
name an absolute path; they ask here. Move the folder anywhere and it works."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, 'fonts')
SITE_OUT = os.path.join(HERE, 'site')
BINDER = os.path.join(HERE, 'binder')
RUBRIC_SOURCES = os.path.join(HERE, 'rubric-sources')

def font(name):
    """Return the bundled font file; fall back to the system copy if the
    bundle is missing so an old checkout still builds."""
    p = os.path.join(FONTS, name)
    if os.path.exists(p):
        return p
    for d in ('/usr/share/fonts/truetype/google-fonts',
              '/usr/share/fonts/truetype/dejavu'):
        q = os.path.join(d, name)
        if os.path.exists(q):
            return q
    return p
