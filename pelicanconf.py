#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'epsi'
SITENAME = 'Yet Another Static Blog'
SITEURL = ''

THEME = "tutor-02"

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL           = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS       = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS      = 'archives.html'
YEAR_ARCHIVE_SAVE_AS  = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'

# No slash / at the end, for pagination friendly.

TAG_URL               = 'tag/{slug}'
TAG_SAVE_AS           = 'tag/{slug}.html'

CATEGORY_URL          = 'category/{slug}'
CATEGORY_SAVE_AS      = 'category/{slug}.html'

AUTHOR_URL            = 'author/{slug}'
AUTHOR_SAVE_AS        = 'author/{slug}.html'
