# -*- coding: utf-8 -*-
import scrapy
from doubanmovie import DoubanmovieItem


class Doubanmovie250Spider(scrapy.Spider):
    name = 'doubanmovie250'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['http://https://movie.douban.com/top250/']

    def parse(self, response):
        urls=response.xpath('//div[@class="hd"]/a/@href').getall().strip()
        for url in urls:
            movieitem=DoubanmovieItem()
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={"movieitem":movieitem})
        
    def parse_detail(self,response):
        movieitem=response.meta["movieitem"]
        movieitem['name']=response.xpath('//*[@id="content"]/h1/span[1]/text()').get().strip()
        zys=response.xpath('//*[@id="info"]/span[3]/span[2]/span/a/text()').getall().strip()
        
        movieitem['zy']='/'.join(zys)
        lxs=response.xpath('//*[@id="content"]/h1/span/text()').getall().strip()
        movieitem['lx']='/'.join(lxs)
        movieitem['gj']=response.xpath('//*[@id="info"]/text()[3]').get().strip()




       
