# -*- coding: utf-8 -*-
import scrapy
from scrapybook.items import ScrapybookItem
import re

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        urls=response.xpath('//article[@class="product_pod"]/h3/a/@href').getall()
        for url in urls:
            bookitem=ScrapybookItem()
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'bookitem':bookitem})
        
    #翻页
        nexturls=['http://books.toscrape.com/catalogue/page-{}.html'.format(number) for number in range(2,50)]
        for nexturl in nexturls:
            yield scrapy.Request(url=nexturl,callback=self.parse)

    def parse_detail(self,response):
        bookitem=response.meta['bookitem']
        bookitem['bookname']=response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        bookitem['bookprice']=response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get()
        bookitem['booklb']=response.xpath('////ul[@class="breadcrumb"]/li[3]/a/text()').get()
        bookitem['booksl']=response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()').get()
        bookitem['booksl']=re.findall(r"\d+\.?\d*",bookitem['booksl']) #筛选数字
        yield bookitem

