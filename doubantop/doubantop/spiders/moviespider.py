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

        #nextpage
        for i in range(0,11):
            i=i*25
            nexturl='https://movie.douban.com/top250?start='+str(i)+'&filter='
            yield scrapy.Request(url=nexturl,callback=self.parse)
    def parse_detail(self,response):
        pass
