# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rq = scrapy.Field() #日期
    zgqw = scrapy.Field() #最高气温
    zdqw = scrapy.Field() #最低气温
    tq = scrapy.Field() #天气
    fx = scrapy.Field() #风向
    pass
