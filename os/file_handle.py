#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'Python中os模块提供了很多文件，目录操作的接口，这个文件主要介绍这些用法'

__author__ = 'AJ Kipper'

import os

'''
os模块包含了一些目录处理的函数
'''
#listdir函数，返回给定目录中所有的文件列表
for file_name in os.listdir('//Users/Jason')
    print file_name


#输出当前目录
print os.getcwd()

#参数是下一级目录
os.chdir('Python')
print os.getcwd()

#返回上级目录
os.chdir(os.pardir)
print os.getcwd()

#创建一个新的目录
os.makedirs('//Users/Jason/Python/base/osdir')
#结果会在base目录下创建一个osdir文件夹

#删除一个文件夹,注意，只能删除空文件夹
os.removedirs('//Users/Jason/Python/base/osdir')

#如果要删除非空文件夹，要使用shutil模块中的rmtree函数
import shutil
shutil.rmtree('//Users/Jason/Python/base/osdir')

#删除一个文件
os.remove('.....filename')



