#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

__author__ = 'AJ Kipper'

import re

#String example
string = 'Hello,I\'m AJ Kipper'

re_pattern = r'AJ.*'

#Search(pattern,string,flags = 0)
'''
Scan through string looking for a match to the pattern,returning
a match object, or None if no match was found.
'''
result = re.search(re_pattern,string)
print result.group(0)
#Output:AJ Kipper
