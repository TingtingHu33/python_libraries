#!/usr/bin/env python
#-*-coding: utf-8-*-
#python 2.7.6

'some methods for psutil module'

__author__ = 'AJ Kipper'

import psutil

#CPU info
print psutil.cpu_times()
print u'cpu counts:%s' % psutil.cpu_count()


#Get system process list
for p in psutil.process_iter():
    try:
        print p
    except psutil.Error:
        pass
