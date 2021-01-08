# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirDayItem(scrapy.Item):#日数据
   
    rq = scrapy.Field()#日期
    aqi = scrapy.Field()
    zldj = scrapy.Field()#质量等级
    pm2 = scrapy.Field()
    pm10 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o38h = scrapy.Field()

class AirMonthItem(scrapy.Item):#月数据
    
    yf = scrapy.Field()#月份
    aqi = scrapy.Field()
    zldj = scrapy.Field()#质量等级
    pm2 = scrapy.Field()
    pm10 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o38h = scrapy.Field()    
