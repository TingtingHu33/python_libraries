#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'some methods for os module'

__author__ = 'AJ Kipper'

import os

'''查看系统环境变量'''

for i in os.environ:
	print i

print os.environ['LOGNAME']

print type(os.environ)
print type(os._Environ)