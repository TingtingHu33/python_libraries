#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'some methods for sys module'

__author__ = 'AJ Kipper'

import sys

#获取终端参数，其中当前文件名为第一个参数argv[0]
def Hello():
    try:
        print 'Hello,%s' % argv[1]
    except:
        print 'Hello!'

#获得Python解释器的版本
print sys.copyright

#使用import时查找的所有模块路劲，是一个list类型，可以进行list相关操作
print sys.path
sys.path.append('your module path')

