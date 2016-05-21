#!/usr/bin/env python
#-*- coding : utf-8-*-
#Python 3.5

'''从网页获取数据直接存入csv文件里面'''

__author__ = 'AJ Kipper'

from bs4 import BeautifulSoup
import requests
import csv


url = 'http://www.bridestory.com/indonesia?page=1'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

#进行页面数据抓取
vendors = soup.select('div > h2 > a')
views = soup.select('div > span.ico-bs-view > span')
cities = soup.select('div > span.cat_city > a')
reviews = soup.select('.rating')

#首先在这里先写好表头字段,后面就不用重复写了
with open('web_data.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['view','city','review','vendor'])

for vendor,view,city,review in zip(vendors,views,cities,reviews):
    data = {
        'vendor' : vendor.get_text(),
        'view' : view.get_text(),
        'city' : city.get_text(),
        'review' : str(review)[-26:-24]
     }
    #这里要把文件打开模式改为'a',也就是添加模式,否则写入模式会覆盖之前的内容
    with open('web_data.csv','a') as csvfile:
        writer = csv.writer(csvfile)
        #第一,data类型一定是list,里面的一个元素为元组类型,也就是在括号内
        #第二,一定要对应view,city等字段插入,因为字典是无序的,要与表头对应写入
        data_list = [(data['view'],data['city'],data['review'],data['vendor'])]
        writer.writerows(data_list)
