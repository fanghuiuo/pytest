# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DbmoviePipeline:
    def process_item(self, item, spider):
        info=item['dy']
        tt=''
        for ss in info:
            tt=tt+str(ss).strip()  
        ls=tt.split('\n')
        for xx in ls:
            if '导演' in xx:
                item['dy']=xx.split(':')[1]
            pass             
        return item
    
class dataPipline(object):
    def __init__(self):
        self.con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='fh@791204',db='pytest')
    def process_item(self,item,spider):
        
        return item