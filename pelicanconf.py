#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

import sys
sys.path.append('.')

AUTHOR = 'epsi'
SITENAME = 'Yet Another Static Blog'
SITEURL = ''

THEME = "tutor-07"

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 1

# Feed generation is usually not desired when developing
FEED_RSS              = 'feed.xml'
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_URL             = 'blog/'
INDEX_SAVE_AS         = 'blog/index.html'

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

# Custom Theme Variables

CURRENTYEAR = date.today().year

# Plugins

#from plugins.jinja2content import jinja2content

#PLUGINS = [
    # ...
#    "plugins.jinja2content",
#]

# Filter
# https://linkpeek.com/blog/how-to-add-a-custom-jinja-filter-to-pelican.html

# https://stackoverflow.com/questions/31607710/randomize-elements-of-a-list-in-jinja-2

import random

def filter_shuffle(seq):
  try:
    result = list(seq)
    random.shuffle(result)
    return result
  except:
    return seq

def filter_split(text, separator):
  return text.split(separator)

def filter_navigation(articles_by_dates, article):
  result = {'has_prev': False, 'has_next': False, 'id': -1}

  for index, post in enumerate(articles_by_dates):
    if post.url == article.url: result['id'] = index

  if result['id'] + 1 > 1:
    result['has_prev'] = True

    for index, post in enumerate(articles_by_dates):
      if index == result['id'] - 1:
        result['prev_url']   = post.url
        result['prev_title'] = post.title

  if result['id'] + 1 < len(articles_by_dates):
    result['has_next'] = True

    for index, post in enumerate(articles_by_dates):
      if index == result['id'] + 1:
        result['next_url']   = post.url
        result['next_title'] = post.title

  return result

def filter_keyjoin(tags, category, keywords):
  terms = []
  terms.append(category)
  terms.extend(tags)
  terms.extend(keywords)
  return terms


# import lib.libfilter
JINJA_FILTERS = {
  'shuffle'    : filter_shuffle,
  'split'      : filter_split,
  'navigation' : filter_navigation,
  'keyjoin'    : filter_keyjoin,
}

# Data

# Blogroll: Helper for friends widget
from lib.friends import *
from lib.archives_gitlab import *
from lib.archives_github import * 
from lib.archives_pelican import *

# Opengraph
OG_LOCALE = "en_US"
OG_LOGO   = "/assets/images/logo-gear-opengraph.png"

# Service

# GOOGLE_ANALYTIC_KEY = ""
# DISQUS_KEY = ""
