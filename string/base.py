#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 3.5

'some methods for string module'

__author__ = 'AJ Kipper'

import string

'''
string.punctuation的用法
string.punctuation里面放入了所有的标点符号,可以判断一个字符串是否为标点符号
'''

#一个小例子
a = ['a','-','b','@','v','!',',','8']

b = [i for i in a if i not in string.punctuation]

print('a is :',a)
print('b is :',b)

'''
------输出结果--------
a is : ['a', '-', 'b', '@', 'v', '!', ',', '8']
b is : ['a', 'b', 'v', '8']

'''

