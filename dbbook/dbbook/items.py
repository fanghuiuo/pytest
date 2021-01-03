# -*- coding:utf-8 -*-

import scrapy


class DbbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname=scrapy.Field()#书名
    yjhpj=scrapy.Field()#一句话评价
    dbpf=scrapy.Field()#豆瓣评分
    pjrs=scrapy.Field()#评价人数
    author=scrapy.Field()#作者
    cbs=scrapy.Field()#出版社
    cbn=scrapy.Field()#出版年
    ys=scrapy.Field()#页数
    dj=scrapy.Field()#定价
    zz=scrapy.Field()#装帧
    cs=scrapy.Field()#丛书
    isbn=scrapy.Field()#版号
    nrjj=scrapy.Field()#内容简介
    zzjj=scrapy.Field()#作者简介
    cpf=scrapy.Field()#出品方
    yzm=scrapy.Field()#原作名
    fbt=scrapy.Field()#副标题
    yz=scrapy.Field()#译者
    info=scrapy.Field()
    
    pass
