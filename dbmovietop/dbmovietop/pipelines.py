
class DbmovietopPipeline:
    def process_item(self, item, spider):
        info=item['info']
        strinfo=''        
        for i in range(0,len(info)):
            strinfo=strinfo+str(info[i])
        list=strinfo.split('\n')
        for nr in list:
            if '导演' in nr and nr.split(':')[0]=='导演':
                item['dy']=nr.split(':')[1]
            if '编剧' in nr:
                item['bj']=nr.split(':')[1]
            if '主演' in nr:
                item['zy']=nr.split(':')[1]
            if '类型' in nr:
                item['lx']=nr.split(':')[1] 
            if '官方网站' in nr:
                item['gfwz']=nr.split(':')[1]
            if '制片国家' in nr:
                item['zpgj']=nr.split(':')[1] 
            if '语言' in nr:
                item['yy']=nr.split(':')[1]
            if '上映日期' in nr:
                item['syrq']=nr.split(':')[1]
            if '片长' in nr:
                item['pc']=nr.split(':')[1]
            if '又名' in nr:
                item['ym']=nr.split(':')[1]
                              
        jqjj=item['jqjj']
                
        print(list)
        return item
class datapipeline(object):
    def process_item(self,item,spider):
        return item
