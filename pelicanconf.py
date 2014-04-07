#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marek No\u017eka'
SITENAME = u'Tlapička.net'
#SITEURL = 'http://tlapicka.net'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'
#LOCALE = ( 'cs_CZ' ,'en_US'  )
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'Blog'

THEME = 'notmytlapicka'
#TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_URL = 'http://github.com/tlapicka'
TWITTER_USERNAME = 'TlapickaNet'

# Blogroll
LINKS = (
    ('www.vojtechkodet.cz', 'http://www.vojtechkodet.cz'),
    ('Mulujte se', 'http://milujte.se'),
    ('Ron Wyatt', 'http://www.b-a-n.cz/informace.html'),
    ('Stvoření?', 'http://www.stvoreni.cz/'),
    ('MatPlotLib', 'http://matplotlib.org'),
    ('NumPy', 'http://www.numpy.org/'),
    ('SciPy', 'http://scipy.org/'),
    ('Zim - A Desktop Wiki', 'http://zim-wiki.org/'),
)

# Social widget
SOCIAL = (
    ('Github', 'http://github.com/tlapicka'),
    ('Twitter', 'http://twitter.com/TlapickaNet'),
    ('G+', 'https://plus.google.com/106541283459415810809'),
    ('Hroch', 'http://hroch.spseol.cz/~nozka/'),
    ('YouTube', 'https://www.youtube.com/user/YouTlapickaTube'),
    ('Wikipedista', 'http://cs.wikipedia.org/wiki/Wikipedista:Tlapicka'),
    ('Wikiobčan',
        'http://commons.wikimedia.org/wiki/Special:ListFiles/Tlapicka'),
    ('Wikispisovatel', 'http://cs.wikibooks.org/wiki/User:Tlapicka'),
    ('VOŠ a SPŠe Olomouc', 'http://www.spseol.cz/'),
)

DEFAULT_PAGINATION = 10

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'headerid(level=3)',
    'toc',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
