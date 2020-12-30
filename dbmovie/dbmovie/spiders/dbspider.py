# -*- coding: utf-8 -*-
import scrapy
from dbmovie.items import DbmovieItem

class DbspiderSpider(scrapy.Spider):
    name = 'dbspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        divs=response.xpath('//div[@class="info"]')
        for div in divs:
            ditem=DbmovieItem()
            ditem['dym']=div.xpath('./div[1]/a/span[1]/text()').get().strip()
            url=div.xpath('./div[1]/a/@href').get().strip()
            ll=response.urljoin(url)
            yield scrapy.Request(url=ll,callback=self.xx,meta={'item':ditem})
            
        urls=response.xpath('//div[@class="paginator"]/a/@href').getall()
        for ul in urls:
            newul=response.urljoin(ul)
            yield scrapy.Request(url=newul,callback=self.parse)
    def xx(self,response):
        newitem=response.meta['item']
        newitem['info']=response.xpath('//div[@id="info"]//text()').getall()     
        newitem['jj']=response.xpath('//span[@property="v:summary"]/text()').get().strip()
        newitem['dbpf']=response.xpath('//div[@class="rating_self clearfix"]/strong/text()').get().strip()
        newitem['pjrs']=response.xpath('//div[@class="rating_sum"]/a/span/text()').get().strip()
        
        yield newitem
        
