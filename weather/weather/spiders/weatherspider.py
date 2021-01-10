# -*- coding:utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherspider'
    allowed_domains = ['lishi.tianqi.com']
    start_urls = ['http://lishi.tianqi.com/']
    
    def parse(self, response):
        lis=response.xpath('//ul[@class="table_list"]//li')
        cslist=['沈阳','北京','上海','广州','深圳','杭州','西安','三亚','苏州','成都','天津','重庆','武汉','拉萨','昆明','长沙','西宁','乌鲁木齐','合肥']
        for li in lis:
            if li.xpath('./a/@href').get() is not None:
                url=li.xpath('./a/@href').get().strip()
                newurl=response.urljoin(url)
                cs=li.xpath('./a/text()').get().strip()
                if cs in cslist:
                    yield scrapy.Request(url=newurl,callback=self.csxx,meta={'city':cs})
        pass
    def csxx(self,response):
        city=response.meta['city']
        yfurls=response.xpath('//div[@class="linegraphbox"]//div//ul//li/a/@href').getall()
        for yfurl in yfurls:            
            newyfurl=response.urljoin(yfurl)
            yield scrapy.Request(url=newyfurl,callback=self.rqxx,meta={'city':city})
        pass
    def rqxx(self,response):
        city=response.meta['city']
        lis=response.xpath('//div[@class="tian_three"]/ul//li')
        for li in lis:
            item=WeatherItem()
            self.emptyitem(item)
            item['city']=city
            item['rq']=li.xpath('./div[1]/text()').get().strip()
            item['zgqw']=li.xpath('./div[2]/text()').get().strip()
            item['zdqw']=li.xpath('./div[3]/text()').get().strip()
            item['tq']=li.xpath('./div[4]/text()').get().strip()
            item['fx']=li.xpath('./div[5]/text()').get().strip()
            print(item)
            yield item
        pass
               
    def emptyitem(self,item):
        item['city']=' '
        item['rq']=' '
        item['zgqw']=' '
        item['zdqw']=' '
        item['tq']=' '
        item['fx']=' '
        return item
