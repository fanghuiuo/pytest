# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapybookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    bookprice = scrapy.Field()
    booklb = scrapy.Field() #类别
    booksl = scrapy.Field()  #数量
    pass
