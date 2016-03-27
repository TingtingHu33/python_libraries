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

#platform函数，可以获取程序运行的操作系统类型，在跨平台运行的时候可用
print sys.platform
#以下是平台和对应的输出值
'''
Linux (2.x and 3.x)        'linux2'   
Windows                    'win32'   
Windows/Cygwin             'cygwin'   
Mac OS X                   'darwin'   
OS/2                       'os2'   
OS/2 EMX                   'os2emx'   
RiscOS                     'riscos'   
AtheOS                     'atheos'
'''
#sys.path函数，当在程序中使用import导入模块的时候，其实import就会从sys.path路径里面去寻找，如果找不到也就导入不成功，当然你也可以自己添加模块
sys.path.append('My module path')


