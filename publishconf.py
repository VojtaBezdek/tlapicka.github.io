#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.tlapicka.net'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = CATEGORY_FEED_ATOM
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = CATEGORY_FEED_RSS

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# TWITTER_USERNAME = 'TlapickaNet'
DISQUS_SITENAME = "blog-tlapicka"

# GOOGLE_ANALYTICS = ""

