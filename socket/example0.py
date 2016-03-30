#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'all methods for socket module'

__author__ = 'AJ Kipper'

#创建一个socket连接
host = ''
port = ''
#family_argv参数socket.XXXX是地址家族
#socket.AF_UNIX用于同一台机器间的进程通信
#socket.AF_INET用于IPv4的TCP和UDP协议
#socket.AF_INET6
socket_object = socket.socekt(family_argv,type_argv)
socekt_object.connect(host,port)
