#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Przemysław Łada'
SITEDESCRIPTION = 'technology, programming, studies and random stuff'
SITESUBTITLE = 'technology, programming, studies and random stuff'
SITENAME = 'PLUR'
SITEURL = ''
COPYRIGHT = 'PLUR'


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = ['en_US']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/guilherme-toti'),
    ('facebook', 'http://www.facebook.com/guilhermetoti'),
    ('instagram', 'https://www.instagram.com/guilherme_toti'),
    ('youtube', 'https://www.youtube.com/guilhermetoti'),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'

SIDEBAR_DISPLAY = ['categories', 'tags', 'social']
INDEX_SAVE_AS = 'blog.html'

MENUITEMS = (
    ('Blog', '/blog'),
)
