#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/oleg_dudkin_com/")

from app import app as application
application.secret_key = 'Be34onc34r8xcv324#@^gmc947SG43j94fAG9023^8mlfmwefno*4!msnSVE_.QgqGq2'