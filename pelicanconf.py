#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path
from urllib.parse import urljoin

# Site configuration
SITENAME = "Seh Hui's Journals"
SITEDESC = """
    Covering a multitude of topics: overcoming technical programming
    challenges, working on tabletop game design, showcasing creative art and
    ponders about life.
"""

AUTHOR = 'Seh Hui Leong'
AUTHOR_BIO = """
    Python programmer by trade, interested in a broad range of creative fields:
    illustrating, game design, writing, choreography and most recently building
    physical things. Described by a friend as a modern renaissance man.
"""

SITEURL = ''
STATICURL = SITEURL
LOGO_URL = urljoin(SITEURL, '/images/logo.png')
FAVICON_URL = urljoin(SITEURL, '/images/favicon.png')

TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = 'en'
LOCALE = 'en_GB'

LINKS = ()

SOCIAL = (
    ('facebook', 'https://facebook.com/leongsh'),
    ('twitter', 'https://twitter.com/felixleong'),
    ('github', 'https://github.com/felixleong'),
    ('bitbucket', 'https://bitbucket.org/felixleong'),
)

PROJECTS = (
    (
        'Pasaraya: Supermarket Manager',
        '201609-pasaraya.jpg',
        'Open supermarket + serve community shoppers + ??? = PROFIT!'),
)

SKILLS = (
    (
        'Python Programming', 'python',
        'Specializes in API design and server-side development with Django '
        'and CherryPy'),
    (
        'Tabletop Game Design', 'dice',
        'Loves card and euro-style strategy games. Loves to add twists to '
        'established game mechanics.'),
    (
        'Web Development', 'website',
        'Fascinated by data-driven programming: APIs, semantic web, data '
        'processing and visualization.'),
    (
        'Creative Arts', 'palette-color',
        'Primarily draws in style of Japanese manga, occassionally indulges '
        'in photography, writing and videography.'),
)

MENUITEMS = (
    ('Blog', urljoin(SITEURL, '/blog/')),
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
FEED_MAX_ITEMS = 200

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
DISPLAY_PAGES_ON_MENU = True
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
CATEGORIES_URL = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAGS_SAVE_AS = 'tag/index.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Plugins
PLUGINS = [
    'pelican-page-hierarchy',
    'pelican-page-order',
    'assets',
    'post_stats',
    'pelican-minify.minify',
    'sitemap',
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

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'oembed': {},
        'plugins.markdownext.mdx_unimoji': {},
        'plugins.markdownext.mdx_del_ins': {},
        'plugins.markdownext.pelican_image': {'static': STATICURL},
    },
    'output_format': 'html5',
}

JINJA_ENVIRONMENT = {}

SITEMAP = {
    'format': 'xml',
}
