#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path
from urllib.parse import urljoin

# Site configuration
AUTHOR = 'Seh Hui Leong'
SITENAME = "Seh Hui's #DevDiaries"
SITEURL = ''
SITEDESC = 'Site description'
STATICURL = ''

TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = 'en'

LINKS = ()

SOCIAL = (
    ('facebook', 'https://facebook.com/leongsh'),
    ('twitter', 'https://twitter.com/felixleong'),
    ('github', 'https://github.com/felixleong'),
    ('bitbucket', 'https://bitbucket.org/felixleong'),
)

MENUITEMS = (
    ('Blog', urljoin(SITEURL, 'blog/')),
)

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

SUMMARY_MAX_LENGTH = 135

# Pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{name}/', '{name}/index.html'),
    (2, '{name}/page/{number}/', '{name}/page/{number}/index.html'),
)
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'authors', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['archives']

# Categories
DEFAULT_CATEGORY = 'Uncategorized'
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False

# URL routes
RELATIVE_URLS = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
ARCHIVES_URL = 'blog/'
# NOTE: The PAGINATED_DIRECT_TEMPLATES would force an override to the URL for
# ARCHIVES_SAVE_AS, so blog.html would be just fine ;)
ARCHIVES_SAVE_AS = 'blog.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tag/{slug}/'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

# Plugins
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

PLUGINS = [
    'pelican-page-hierarchy',
    'pelican-page-order',
    'assets',
    'post_stats',
    'pelican-minify.minify',
]
