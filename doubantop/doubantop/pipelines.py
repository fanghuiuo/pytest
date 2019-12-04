# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubantopPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='fh@791204', db='movietop')
        self.strsql='insert into movie (dymz,dydy,dybj,dyzy,dylx,dygj,dyyy,dysyrq,dypc,dyym,dyjj) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    def open_spider(self, spider):
        self.cursor=self.conn.cursor()
        
    
    def process_item(self, item, spider):
        self.cursor.execute(self.strsql,(item['dymz'],item['dydy'],item['dybj'],item['dyzy'],item['dylx'],item['dygj'],item['dyyy'],item['dysyrq'],item['dypc'],item['dyym'],item['dyjj']))
        self.conn.commit()
        print(item)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
    