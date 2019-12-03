# -*- coding: utf-8 -*-
import scrapy
from doubantop.items import DoubantopItem 

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['http://https://movie.douban.com/top250/']

    def parse(self, response):
        
        urls=response.xpath('//div[@class="info"]/div[1]/a/@href').getall()
        for url in urls:
            item=DoubantopItem()
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item})

        starturl='https://movie.douban.com/top250?start=0&filter='
        for i in range(1,11):
            
    def parse_detail(self,response):
        pass
