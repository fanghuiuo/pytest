# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapybookPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='fh@791204', db='book')
    def open_spider(self,spider):
        self.cursor=self.conn.cursor()

    def process_item(self, item, spider):
        insql='insert into book (bookname,bookprice,booklb,booksl) values (%s,%s,%s,%s)'
        self.cursor.execute(insql,(item['bookname'],item['bookprice'],item['booklb'],item['booksl']))
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        
    
    
        