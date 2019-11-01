# -*- coding: utf-8 -*-
import scrapy
from seleniumtest.items import SeleniumtestItem

class AirspiderSpider(scrapy.Spider):
    name = 'airspider'
    allowed_domains = ['https://www.aqistudy.cn/historydata/']
    start_urls = ['https://www.aqistudy.cn/historydata/']



    def parse(self, response):
        urls=response.xpath('//div[@class="panel panel-info"]/div[2]/ul/li[1]/a/@href').getall().strip()
        
        for url in urls:
            cityurl='https://www.aqistudy.cn/historydata/'+url
            cs=url.split('=',1)[1]

            yield scrapy.Request(url=cityurl,callback=self.parse_month,meta={'cs':cs})
        
    def parse_month(self,response):
        cs=response.meta["cs"]
        yfitem=SeleniumtestItem()
        tr_list=response.xpath('//tr')
        tr_list.pop(0)
        for tr in tr_list:
            yfitem['yf']=tr.xpath('./td[1]/a/text()').get().strip()
            yfitem['cs']=cs
            yfitem['aqi']=tr.xpath('./td[2]/text()').get().strip()
            yfitem['aqifw']=tr.xpath('./td[3]/text()').get().strip()
            yfitem['zldj']=tr.xpath('./td[4]/text()').get().strip()
            yfitem['pm2_5']=tr.xpath('./td[5]/text()').get().strip()
            yfitem['pm10']=tr.xpath('./td[6]/text()').get().strip()
            yfitem['so2']=tr.xpath('./td[7]/text()').get().strip()
            yfitem['co']=tr.xpath('./td[8]/text()').get().strip()
            yfitem['no2']=tr.xpath('./td[9]/text()').get().strip()
            yfitem['o3']=tr.xpath('./td[10]/text()').get().strip()

            yfurl=tr.xpath('./td[1]/a/@href').get().strip()
            yield scrapy.Request(url=yfurl,callback=self.parse_day)

        
    def parse_day(self,response):
        pass
