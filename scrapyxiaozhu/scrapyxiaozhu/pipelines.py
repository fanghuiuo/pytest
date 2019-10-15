# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyxiaozhuPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='fh@791204', db='xiaozhu')
        self.strsql='insert into fz (fzmc,fzdz,fzjg,fzxm) values (%s,%s,%s,%s)'
    def open_spider(self, spider):
        self.cursor=self.conn.cursor()
        pass
    
    def process_item(self, item, spider):
        self.cursor.execute(self.strsql,(item['fzmc'],item['fzdz'],item['fzjg'],item['fzxm']))
        self.conn.commit()
        print(item)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        pass

