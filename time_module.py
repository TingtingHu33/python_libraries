#!/usr/bin/env python
#-*-coding: utf-8-*-
#python 2.7.6

'all methods for time module'

__author__ = 'AJ Kipper'

import time

#time.time方法，以秒为单位输出当前时间到1970年1月1日的秒数，也就是输出当前时间戳
time.time()

#例子，计算程序运行时间
def sleep():
    time.sleep(3)
start_time = time.time()
sleep()
end_time = time.time()
print "程序运行时间为：%f" % (start_time - end_time)


