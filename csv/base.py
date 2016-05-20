#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 3.5

'some methods for csv module'

__author__ = 'AJ Kipper'

import csv

'''
进行csv文件的读取,并且输出
'''

with open('ReadCsvFile.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(row)

'''
输出:
['1,2,3,4,5,6']
['7,8,9,10,11,12']
'''


'''
进行csv文件的写入
'''
with open('WriteCsvFile.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	#写入数据必须是list类型
	spamwriter.writerow(['A'] * 5 + ['B'])
	spamwriter.writerow(['Hello', 'This is a test', 'Not bad'])

'''
WriteCsvFile.csv 文件内容:
A A A A A B
Hello |This is a test| |Not bad|
'''