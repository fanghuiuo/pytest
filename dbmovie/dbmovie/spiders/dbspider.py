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
            
        
    def xx(self,response):
        newitem=response.meta['item']
        newitem['pc']= response.xpath('//div[@id="info"]/span[13]/text()').get().strip()
        newitem['dy']=response.xpath('//div[@id="info"]//text()').getall()        
        print(newitem)
        yield newitem
        
