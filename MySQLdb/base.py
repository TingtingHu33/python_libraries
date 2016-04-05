#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'all methods for MySQLdb module'

__author__ = 'AJ Kipper'

import MySQLdb as mdb

#数据库地址
database_adr = 'localhost'
#用户名和密码
username = 'root'
password = 'test'
#数据库
database_name = 'Pydb'

#连接数据库
con = mdb.connect(database_adr,username,password,database_name)
#创建游标
cur = con.cursor()
#数据库操作语句，与SQL语言一样
order = 'select* from TABLE_NAME'
#执行操作
cur.execute(order)
#得到查询结果，以list返回
values = cur.fetchall()
#对操作进行commit，不commit，程序结束对操作无效
con.commit()


