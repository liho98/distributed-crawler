# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .common import *

BACKEND = 'frontera.contrib.backends.hbase.HBaseBackend'
HBASE_USE_FRAMED_COMPACT = True

MAX_NEXT_REQUESTS = 2048
NEW_BATCH_DELAY = 3.0

STORE_CONTENT = True

HBASE_THRIFT_HOST = 'localhost' # HBase Thrift server host and port
HBASE_THRIFT_PORT = 9090

