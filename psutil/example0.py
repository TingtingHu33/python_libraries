#!/usr/bin/env python
#-*-coding: utf-8-*-
#python 2.7.6

'some methods for psutil module'

__author__ = 'AJ Kipper'

import psutil as p

#CPU info
print u'cpu counts:%s' % p.cpu_count() 
