# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DbmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dym=scrapy.Field()#电影名
    dy=scrapy.Field()#导演
    bj=scrapy.Field()#编剧
    zy=scrapy.Field()#主演
    lx=scrapy.Field()#类型
    zpgj=scrapy.Field()#制片国家
    yy=scrapy.Field()#语言
    syrq=scrapy.Field()#上映日期
    pc=scrapy.Field()#片长
    ym=scrapy.Field()#又名
    jj=scrapy.Field()#简介
    dbpf=scrapy.Field()#评分
    pjrs=scrapy.Field()#评价人数
    info=scrapy.Field()
    
    pass
