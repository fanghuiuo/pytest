# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DfbkxItem(scrapy.Item):
    gs = scrapy.Field()  # 公司
    hbh = scrapy.Field()  # 航班号
    qfsj = scrapy.Field()  # 起飞时间
    ddsj = scrapy.Field()  # 到达时间
    qfz = scrapy.Field()  # 起飞站
    ddz = scrapy.Field()  # 到达站
    cw = scrapy.Field()  # 舱位
    xm = scrapy.Field()  # 姓名
    xb = scrapy.Field()  # 性别
    age = scrapy.Field()  # 年龄
    gj = scrapy.Field()  # 国籍
    zjh = scrapy.Field()  # 证件号
    tflx = scrapy.Field()  # 特服类型
    pnr = scrapy.Field()  # pnr号
    zwh = scrapy.Field()  # 座位号
