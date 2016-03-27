#!/usr/bin/env pyhton
#-*-coding:utf-8-*-
#python 2.7.6

'all methods for sys module'

__author__ = 'AJ Kipper'

import sys

#argv[]函数，获取命令行参数，其中要运行的python文件名是第一个参数
def hello():
    try:
        print 'Hello, %s' % sys.argv[1]
    except:
        print 'Hello'
hello()
#----------------------------------
