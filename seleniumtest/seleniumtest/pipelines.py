# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from seleniumtest.items import yfItem
from seleniumtest.items import rqItem


class SeleniumtestPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='fh@791204', db='air')
        self.yfsql='insert into airmonth (yf,cs,aqi,aqifw,zldj,) values (%s,%s,%s,%s)'
    def open_spider(self,spider):
        self.cursor=self.conn.cursor()

    def process_item(self,item,spider):
        if isinstance(item,yfItem):
            self.cursor.execute(self.yfsql,(item['fzmc'],item['fzdz'],item['fzjg'],item['fzxm']))
            self.conn.commit()
            print(item)
            return item
        elif isinstance(item,rqItem):
            return item
           
        
    
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
