#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Python 2.7.10

__author__ = 'AJ Kipper'

import pymongo

#这里连接数据库
client = pymongo.MongoClient("localhost", 27017)

#这里连接数据库名字
db = client.Blog

post = {
	'title':'My Blog',
	'content':'This is a test!'
}

#插入数据
db.posts.insert(post)

#把数据读取出来
for item in db.posts.find():
	print '%s , %s' % (item['title'],item['content'])