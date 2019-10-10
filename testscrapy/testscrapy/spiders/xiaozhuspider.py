# -*- coding: utf-8 -*-
import scrapy


class XiaozhuspiderSpider(scrapy.Spider):
    name = 'xiaozhuspider'
    allowed_domains = ['sy.xiaozhu.com']
    start_urls = ['http://sy.xiaozhu.com/']

    def parse(self, response):
        pass
