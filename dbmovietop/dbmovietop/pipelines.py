#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   pipelines.py
@Time    :   2021/01/30 16:36:47
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib

import pymysql


class DbmovietopPipeline:
    def process_item(self, item, spider):
        info = item['info']
        strinfo = ''
        for i in range(0, len(info)):
            strinfo = strinfo + str(info[i])
        list = strinfo.split('\n')
        for nr in list:
            nr = nr.strip()
            if '导演' in nr and nr.split(':')[0] == '导演':
                item['dy'] = nr.split(':')[1]
            if '编剧' in nr:
                item['bj'] = nr.split(':')[1]
            if '主演' in nr:
                item['zy'] = nr.split(':')[1]
            if '类型' in nr:
                item['lx'] = nr.split(':')[1]
            if '官方网站' in nr:
                item['gfwz'] = nr.split(':')[1]
            if '制片国家' in nr:
                item['zpgj'] = nr.split(':')[1]
            if '语言' in nr:
                item['yy'] = nr.split(':')[1]
            if '上映日期' in nr:
                item['syrq'] = nr.split(':')[1]
            if '片长' in nr:
                item['pc'] = nr.split(':')[1]
            if '又名' in nr:
                item['ym'] = nr.split(':')[1]

        jqjj = item['jqjj']
        jq = ''
        for jj in jqjj:
            jq = jq + jj.strip()
        if '展开全部' in jq:
            item['jqjj'] = jq.split('展开全部')[1]
        else:
            item['jqjj'] = jq

        pfzb = item['pfzb']
        zb = ''
        for ss in pfzb:
            if '星' in ss:
                zb = zb + ss.rstrip()
            if '%' in ss:
                zb = zb + ss
        listpfzb = zb.split('\n')
        listpfzb.pop(0)
        ll = ''
        for tt in listpfzb:
            ll = ll + tt.strip() + ':'
        item['pfzb'] = ll[0:-1]

        cybqlist = item['cybq']
        cybq = ''
        for tt in cybqlist:
            cybq = cybq + tt.strip() + ':'
        item['cybq'] = cybq[0:-1]
        item['info'] = ''
        print(item)
        return item


class datapipeline(object):
    def open_spider(self, spider):
        self.con = pymysql.connect(host='127.0.0.1', user='root', password='root888', db='pytest')
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        insql = 'insert into dbmovie (dym,dy,bj,zy,lx,zpgj,yy,syrq,pc,ym,jqjj,dbpf,pjrs,gfwz,pfzb,imdbpf,hjqk,cybq,yjhpj,imdbpjrs) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(insql, (item['dym'], item['dy'], item['bj'], item['zy'], item['lx'], item['zpgj'], item['yy'], item['syrq'], item['pc'], item['ym'], item['jqjj'], item['dbpf'], item['pjrs'], item['gfwz'], item['pfzb'], item['imdbpf'], item['hjqk'], item['cybq'], item['yjhpj'], item['imdbpjrs']))
            self.con.commit()
        except Exception:
            self.con.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.con.close()
