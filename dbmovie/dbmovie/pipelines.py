# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DbmoviePipeline:
    def process_item(self, item, spider):
        info=item['info']
        tt=''
        for ss in info:
            tt=tt+str(ss)
        ls=tt.split('\n')
        for xx in ls:
            if '导演' in xx and xx.split(':')[0].strip()=='导演':
                item['dy']=xx.split(':')[1]
            if '编剧' in xx:
                item['bj']=xx.split(':')[1]
            if '主演' in xx:
                item['zy']=xx.split(':')[1]
            if '类型' in xx:
                item['lx']=xx.split(':')[1]
            if '制片国家' in xx:
                item['zpgj']=xx.split(':')[1]
            if '语言' in xx:
                item['yy']=xx.split(':')[1]
            if '上映日期' in xx:
                item['syrq']=xx.split(':')[1]
            if '片长' in xx:
                item['pc']=xx.split(':')[1]
            if '又名' in xx:
                item['ym']=xx.split(':')[1]        
                         
        return item
    
class dataPipline(object):
    def __init__(self):
        self.con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='fh@791204',db='pytest')
    def open_spider(self,spider):
        self.cursor=self.con.cursor()
    def process_item(self,item,spider):
        intsql='insert into dbmovie (dym,dy,bj,zy,lx,zpgj,yy,syrq,pc,ym,jj,dbpf,pjrs) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'     
        print(item)
        try:
            self.cursor.execute(intsql,(item['dym'],item['dy'],item['bj'],item['zy'],item['lx'],item['zpgj'],item['yy'],item['syrq'],item['pc'],item['ym'],item['jj'],item['dbpf'],item['pjrs'],))
            self.con.commit()
        except:
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()