#!/usr/bin/env Python
#-*- coding: utf-8 -*-
#--Python_Version:2.7.10

'''
pandas的两个主要数据结构：Series和DataFrame
Series类似一维数组对象，也可看成定长的有序字典
'''

__author__ = 'AJ Kipper'

from pandas import Series
import pandas as pd

#创建一个数组，并且自定义索引 
obj = Series([1,2,3,4],index = ['a','b','c','d'])
print obj
#通过索引查找值
print obj['c']

print '-'*6 + 'text1' + '-'*6

#Series可看成定长的有序字典，因为它是索引值到数据值的一个映射。
#所以它拥有字典的一些操作

#查看是否具有这个索引
print 'a' in obj 

print '-'*6 + 'text2' + '-'*6

#所以呢，如果数据开始是放在字典里面的，则可以通过字典来创建Series
dit = {'aa':11,'bb':22,'cc':33,'dd':44}
obj_1 = Series(dit)
print obj_1

print '-'*6 + 'text3' + '-'*6

#好像不可以自定义索引
#可以通过自定义索引index顺序来映射
stats = ['dd','aa','cc','bb']
obj_2 = Series(dit,index = stats)
print obj_2

print '-'*6 + 'text4' + '-'*6

#如果给定的index值在Series里面没有找到，其结果记为NaN（非数字 not a number）
#表示数据缺失
stats = ['text','aa','cc','bb']
obj_2 = Series(dit,index = stats)
print obj_2

print '-'*6 + 'text5' + '-'*6

#可以用pandas中的isnull和notnull函数用于检测缺失数据
print pd.isnull(obj_2)
print pd.notnull(obj_2)
#用Series属性也可以
print Series.isnull(obj_2)
print Series.notnull(obj_2)

#这个是查找是否重合？合并？
print obj_1 + obj_2

print '-'*6 + 'text6' + '-'*6

#Series对象本身及其索引都有一个name属性
obj_2.name = 'X'
obj_2.index.name = 'Probie'
print obj_2



