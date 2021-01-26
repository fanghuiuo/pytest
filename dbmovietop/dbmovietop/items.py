import scrapy


class DbmovietopItem(scrapy.Item):
    dym = scrapy.Field()  # 电影名
    yjhpj = scrapy.Field()  # 一句话评价
    dy = scrapy.Field()  # 导演
    bj = scrapy.Field()  # 编剧
    zy = scrapy.Field()  # 主演
    lx = scrapy.Field()  # 类型
    gfwz = scrapy.Field()  # 官方网站
    zpgj = scrapy.Field()  # 制片国家
    yy = scrapy.Field()  # 语言
    syrq = scrapy.Field()  # 上映日期
    pc = scrapy.Field()  # 片长
    ym = scrapy.Field()  # 又名
    jqjj = scrapy.Field()  # 剧情简介
    dbpf = scrapy.Field()  # 豆瓣评分
    pfzb = scrapy.Field()  # 评分占比
    imdbpf = scrapy.Field()  # imdb评分
    imdbpjrs = scrapy.Field()  # imdb评价人数
    pjrs = scrapy.Field()  # 评价人数
    hjqk = scrapy.Field()  # 获奖情况
    cybq = scrapy.Field()  # 豆瓣成员常用标签
    info = scrapy.Field()
