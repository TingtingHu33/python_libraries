#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7.6

'all methods for socket module'

__author__ = 'AJ Kipper'

#创建一个socket连接
host = ''
port = ''
#family_argv参数socket.XXXX是地址家族
#type_argv是类型参数
#protocol默认为0
socket_object = socket.socekt(family_argv,type_argv,protocol = 0)

#--------服务器端-----------

#端口绑定
socket_object.bind()

#端口监听
socket_object.listen()

#被动接收客户端的连接，直到连接成功(blocking)
socket_object.accept()


#--------客户端--------------

#连接socket
socket_object.connect()

#--------一般方法------------

#接收TCP信息
socket_object.recv()

#发送TCP信息
socket_object.send()

#接收UDP信息
socket_object.recvfrom()

#发送UDP信息
socket_object.sendto()

#关闭socket
socket_object.close()

#返回主机名字
socket_object.gethostname()

#根据主机名返回IP
socket_object.gethostbyname('hostname')

