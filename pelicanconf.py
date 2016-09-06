#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = 'Seh Hui Leong'
SITENAME = "Seh Hui's #DevDiaries"
SITEURL = ''
SITEDESC = 'Site description'
STATICURL = ''

TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = 'en'

# Paths
THEME = 'themes/breeze/'
PATH = 'content'
PLUGIN_PATHS = [
    'plugins/',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/', 'The static site generator'),
         ('Python.org', 'http://python.org/', ''),
         ('Jinja2', 'http://jinja.pocoo.org/', ''),)

# Social widget
SOCIAL = (
    ('facebook', 'https://facebook.com/leongsh'),
    ('twitter', 'https://twitter.com/felixleong'),
    ('github', 'https://github.com/felixleong'),
    ('bitbucket', 'https://bitbucket.org/felixleong'),
)

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 120

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAUT_CATEGORY = 'Uncategorized'
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

# URL routes
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''


# Plugins
PLUGINS = [
    'pelican-page-hierarchy',
    'pelican-page-order',
    'assets',
    'post_stats',
]
TYPOGRIFY = True

ASSET_CONFIG = (
    ('COMPASS_BIN', os.path.abspath('bin/compass')),
    ('COMPASS_PLUGINS', ['bootstrap-sass']),
    ('COMPASS_CONFIG', {
        'http_path': '/',
        'http_fonts_dir': 'theme/fonts',
        'relative_assets': False,
    }),
)

MD_EXTENSIONS = [
    'extra',
    'codehilite(css_class=codehilite)',
    'oembed',
    'plugins.markdownext.mdx_unimoji',
    'plugins.markdownext.mdx_del_ins',
    'plugins.markdownext.pelican_image(static={})'.format(STATICURL),
]
