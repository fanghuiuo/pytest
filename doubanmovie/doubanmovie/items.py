# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #片名
    zy = scrapy.Field() #主演
    lx = scrapy.Field() #类型
    gj = scrapy.Field() #国家
    yy = scrapy.Field() #语言
    syrq = scrapy.Field() #上映日期
    pc = scrapy.Field() #片长
    bm = scrapy.Field() # 别名
    pf = scrapy.Field() #评分
    jq = scrapy.Field() #剧情
    pass
