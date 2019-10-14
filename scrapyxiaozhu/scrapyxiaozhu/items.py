# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyxiaozhuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fzmc = scrapy.Field()
    fzdz = scrapy.Field()
    fzjg = scrapy.Field()
    fzxm = scrapy.Field()
    pass
