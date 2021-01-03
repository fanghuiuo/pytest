#-*- coding:utf-8 -*-
import pymysql
class DbbookPipeline(object):
    
    def process_item(self, item, spider):
        
        info=item['info']
        ss=''       
        for tt in info:
            ss=ss+str(tt)        
        jj=ss.split()
        for yy in jj:
            if '出版社' in yy and len(yy)<5:
                               
                item['cbs']=jj[(jj.index(yy) + 1)]
                zzi=''
                for i in range(1,(jj.index(yy))):
                    
                    zzi=zzi+jj[i]
                item['author']=zzi
            if '出版年' in yy:
                item['cbn']=jj[(jj.index(yy) + 1)]
            if '页数' in yy:
                item['ys']=jj[(jj.index(yy) + 1)]
            if '定价' in yy:
                if jj[(jj.index(yy) + 1)]=='CNY':
                    item['dj']=jj[(jj.index(yy) + 2)]
                else:
                    item['dj']=jj[(jj.index(yy) + 1)]
            if '装帧' in yy:
                item['zz']=jj[(jj.index(yy) + 1)]
            if '丛书' in yy:
                item['cs']=jj[(jj.index(yy) + 1)]
            if 'ISBN' in yy:
                item['isbn']=jj[(jj.index(yy) + 1)]
            if '出品方' in yy:
                item['cpf']=jj[(jj.index(yy) + 1)]
            if '副标题' in yy:
                item['fbt']=jj[(jj.index(yy) + 1)]
            if '原作名' in yy:
                item['yzm']=''
                for i in range(1,10):
                    if ':' not in jj[jj.index(yy)+i]:
                        item['yzm']=item['yzm']+' '+jj[jj.index(yy)+i]
                    else:
                        break  
                print(item['yzm'])
            if '译者' in yy:
                item['yz']=jj[(jj.index(yy) + 1)]
        
        nrjj=item['nrjj']       
        bbt=''               
        for vv in nrjj:
            bbt=bbt+vv.strip()
        if '(展开全部)' in bbt:
            item['nrjj']=bbt.split('(展开全部)')[1]
        else:
            item['nrjj']=bbt 
        kk=''
        zzjj=item['zzjj']
        for hh in zzjj:
            kk=kk+hh.strip()
        if '(展开全部)' in kk:
            item['zzjj']=kk.split('(展开全部)')[1]
        else:
            item['zzjj']=kk                 
        return item

class dataPipeline(object):
    def __init__(self):
        self.con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root888',db='book')
    def open_spider(self,spider):
        self.cursor=self.con.cursor()
    def process_item(self,item,spider):
        insql='insert into dbbook (bookname,yjhpj,dbpf,pjrs,author,cbs,cbn,ys,dj,zz,cs,isbn,nrjj,zzjj,cpf,fbt,yzm,yz) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(insql,(item['bookname'],item['yjhpj'],item['dbpf'],item['pjrs'],item['author'],item['cbs'],item['cbn'],item['ys'],item['dj'],item['zz'],item['cs'],item['isbn'],item['nrjj'],item['zzjj'],item['cpf'],item['fbt'],item['yzm'],item['yz']))
            self.con.commit()
        except:
            self.con.rollback()
        return item,
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()
        
