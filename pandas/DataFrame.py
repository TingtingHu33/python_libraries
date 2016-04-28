#!/usr/bin/env Python
#-*- coding: utf-8 -*-
#--Python_Version:2.7.10

'''
DataFrame是一个表格型数据结构，含有一组有序的列，可以看做由Series组成的字典
构建DataFrame的方法有很多，最常用的是直接传入一个由等长列表或NumPy数组组成的字典
'''

__author__ = 'AJ Kipper'

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

data = {'name':['Cat','Dog','Bug'],
        'age':[3,5,2],
        'pop':[1.4,4.5,2.3]}

frame = DataFrame(data)
print frame

print '-'*30

#同样的，如果数据缺失会用NaN来表示
frame_1 = DataFrame(data,columns = ['age','name','pop','what'])
print frame_1
#属性
print frame_1.columns
#提取一个Series
print frame_1.age
#通过索引来查询
print frame_1.ix[1]

print '-'*30
#当然，也可以赋值
#example_1
frame_1['what'] = 'TF'
print frame_1
#example_2
frame_1['what'] = np.arange(3)
print frame_1

print '-'*30
#为不存在的列赋值会创造一个新列
frame_1['new'] = 'new'
print frame_1
#或者可以判断某一列是否有某个值
frame_1['<Name is Cat?>'] = frame_1.name == 'Cat'
print frame_1

print '-'*30
#可以用del删除列
#el frame_1['new']
print frame_1


print '-'*30
#还有一种常见的数据形式是嵌套字典（也就是字典中的字典）
test_data = {'Cat':{'age':1,'pop':1.2},'Dog':{'age':2,'pop':2.3}}
#传给DataFrame的话，外层字典key作为列，内层字典key作为行
frame_2 = DataFrame(test_data)
print frame_2 
print '\n转置之后：'

#可以用obj.T对结果进行转置
print frame_2.T