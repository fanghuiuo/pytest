# -*- coding: utf-8 -*-
import scrapy
from doubantop.items import DoubantopItem 

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        
        urls=response.xpath('//div[@class="info"]/div[1]/a/@href').getall()
        for url in urls:
            item=DoubantopItem()
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item})

        #nextpage
        for i in range(1,3):
            i=i*25
            nexturl='https://movie.douban.com/top250?start='+str(i)+'&filter='
            yield scrapy.Request(url=nexturl,callback=self.parse)
            
    def parse_detail(self,response):
        item=response.meta['item']
        item['dymz']=response.xpath('//div[@id="content"]/h1/text()').get()
        dyinfo=response.xpath('//div[@id="info"]//text()').get()#text前用//取包括子节点的text 用/取直接节点text.或用用string()全取
        strlist=dyinfo.split('\n')
        for zd in strlist:
            if '导演' in zd:
                tt=zd.split(':')
                item['dydy']=tt[1]
            if '编剧' in zd:
                tt=zd.split(':')
                item['dybj']=tt[1]
            if '主演' in zd:
                tt=zd.split(':')
                item['dydy']=tt[1]
            if '类型' in zd:
                tt=zd.split(':')
                item['dylx']=tt[1]
            if '制片国家/地区' in zd:
                tt=zd.split(':')
                item['dygj']=tt[1]
            if '语言' in zd:
                tt=zd.split(':')
                item['dyyy']=tt[1]
            if '上映日期' in zd:
                tt=zd.split(':')
                item['dysyrq']=tt[1]
            if '片长' in zd:
                tt=zd.split(':')
                item['dypc']=tt[1]
            if '又名' in zd:
                tt=zd.split(':')
                item['dyym']=tt[1]

        item['dyjj']=response.xpath('//div[@id="link-report"]/span[2]/string()') #string()
        print(item)
        yield item
