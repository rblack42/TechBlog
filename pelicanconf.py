#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roie R. Black'
SITENAME = u'Roie Black\'s TechBlog'
SITEURL = 'http://www.black-devops.org'
BANNER_SUBTITLE = u"exploring software systems"

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_LANG = u'en'

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
         ('ACC Home Page', 'http://www.austincc.edu/rblack'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/rblack42/'),
        ('LinkedIn', 'https://www.linkedin.com/profile/view?id=103423831&trk=spm_pic'),
        ('Google+', 'https://www.google.com/+RoieBlack'),)

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

YEARLY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

RELATIVE_URLS = False

PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    'extract_toc', 
    'disqus_static', 
]
THEME='themes/bootstrap3'

DISQUS_SITENAME = u'black-devops-blog'
DISCUS_SECRET_KEY= u'InDePGOSUQys3bzScm5eN5SI7O8VImwLprHRP4hcqIm5v7Cu4U1z1UDoSQJVF6MJ'
DISQUS_PUBLIC_KEY = u'xEDxWSlVYcXYVARER1I6cYsRygwZd9RkH3d4pTJcuOtllnFHRgVI9077fTVl5ORl'

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'
SHOW_ARTICLE_CATEGORY = False
FAVICON = 'images/favicon.png'
BANNER = 'images/collingsF4.png'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
TAGS_URL = "tag-{slug}.html"
TAGS_SAVE_A = "tags.html"
TAG_SAVE_AS = "tag-{slug}.html"
TAG_URL = "tag-{slug}.html"

