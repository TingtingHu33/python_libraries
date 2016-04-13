#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

__author__ = 'AJ Kipper'

import re

#String example
string = 'Hello,I\'m AJ Kipper'

re_pattern = r'AJ.*'

#search(pattern,string,flags = 0)
'''
Scan through string looking for a match to the pattern,returning
a match object, or None if no match was found.
'''
result = re.search(re_pattern,string)
print result.group(0)
#Output:AJ Kipper

#match(pattern,string,flags = 0)
'''
Try to apply the pattern at the start of the string,returning
a match object,or None if no match was found.
'''


#What's the difference between re.match and re.search?
'''
Python offers two different primitive operations based on regular expressions:
    match checks for a match only at the beginning of the string, while search
    checks for a match anywhere in the string (this is what Perl does by
            default).

    Note that match may differ from search even when using a regular expression
    beginning with '^': '^' matches only at the start of the string, or in
    MULTILINE mode also immediately following a newline. The 'match'
    operation succeeds only if the pattern matches at the start of the string
    regardless of mode, or at the starting position given by the optional pos
    argument regardless of whether a newline precedes it.
    '''


