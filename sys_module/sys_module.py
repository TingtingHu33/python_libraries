#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 'a test module'
  
  __author__ = 'Jason'
   
   import sys
   print '脚本名字：',sys.argv[0]
   print '参数个数：',len(sys.argv)
   for i in range(len(sys.argv)):
        print '第%i个参数是：%s' % ((i+1),sys.argv[i])
