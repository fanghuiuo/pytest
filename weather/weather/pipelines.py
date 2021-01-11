# -*-coding:utf-8 -*-
import pymysql


class WeatherPipeline(object):
    def process_item(self, item, spider):
        return item
class DataPipeling(object):
    def __init__(self):
        self.con=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='root888',db='pytest')
    def open_spider(self,spider):
        self.cursor=self.con.cursor()
    def process_item(self,item,spider):
        insql='insert into weather (city,rq,xq,zgqw,zdqw,tq,fx) values (%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(insql,(item['city'],item['rq'],item['xq'],item['zgqw'],item['zdqw'],item['tq'],item['fx']))
            self.con.commit()
        except:
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()