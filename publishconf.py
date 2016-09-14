#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://felixleong.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

ASSET_CONFIG = (
    ('COMPASS_BIN', os.path.abspath('bin/compass')),
    ('COMPASS_PLUGINS', ['bootstrap-sass']),
    ('COMPASS_CONFIG', {
        'http_path': '/',
        'http_fonts_dir': 'theme/fonts',
        'relative_assets': False,
        'output_style': ':compressed',
    }),
)
# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
