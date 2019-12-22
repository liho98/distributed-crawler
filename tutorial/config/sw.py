# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .worker import *

CRAWLING_STRATEGY = 'frontera.strategy.basic.BasicCrawlingStrategy' # path to the crawling strategy class
LOGGING_CONFIG='logging-sw.conf' # if needed
MAX_PAGES_PER_HOSTNAME = 10