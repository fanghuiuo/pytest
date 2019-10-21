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
            ss='catalogue'
            if ss in url:
                newurl='http://books.toscrape.com/'+url
            else:
                newurl='http://books.toscrape.com/'+ss+'/'+url

           
            yield scrapy.Request(url=newurl,callback=self.parse_detail,meta={'bookitem':bookitem})
        
    #翻页
        nexturls=['http://books.toscrape.com/catalogue/page-{}.html'.format(number) for number in range(2,50)]
        for nexturl in nexturls:
            yield scrapy.Request(url=nexturl,callback=self.parse)

    def parse_detail(self,response):
        bookitem=response.meta['bookitem']
        bookitem['bookname']=response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get().strip()
        bookitem['bookprice']=response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get().strip()
        #bookitem['bookprice']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get()
        bookitem['booklb']=response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get().strip()
        bookitem['booksl']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()').get().strip()
        #bookitem['booksl']=response.xpath('//p[@class="instock availability"]/text()').get().strip()
        #bookitem['booksl']=str(re.findall(r"\d+\.?\d*",bookitem['booksl'])) #筛选数字
        print(bookitem)
        yield bookitem

