#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'some methods for time module'

__author__ = 'AJ Kipper'

import time

#获取时间戳，返回的是从1970年1月1日到现在的秒数
print 'time stamp is %f' % time.time()

#获取系统当前时间
print 'system time is ',time.ctime()

#睡眠
time.sleep(4)
