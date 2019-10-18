# -*- coding: utf-8 -*-
import scrapy
from  scrapyxiaozhu.items import ScrapyxiaozhuItem

class XiaozhuSpider(scrapy.Spider):
    name = 'xiaozhu'
    allowed_domains = ['sy.xiaozhu.com']
    start_urls = ['http://sy.xiaozhu.com/']

    def parse(self, response):
        listurls=response.xpath('//div[@id="page_list"]/ul/li/a/@href').getall()
        for url in listurls:
            fzitem=ScrapyxiaozhuItem()
            
            yield scrapy.Request(url=url,callback=self.parse_detail, meta={'fzitem':fzitem})
                
       
        next_urls = ['http://sy.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(2,13)]  
        for next_url in next_urls:
            yield scrapy.Request(next_url, callback=self.parse)    
    
    def parse_detail(self,response):
        fzitem = response.meta["fzitem"] 
        fzitem['fzmc']=response.xpath('//div[@class="pho_info"]/h4/em/text()').get()
        fzitem['fzdz']=response.xpath('//div[@class="pho_info"]/p/@title').get()
        fzitem['fzjg']=response.xpath('//div[@id="pricePart"]/div/span/text()').get()
        fzitem['fzxm']=response.xpath('//div[@class="w_240"]/h6/a/@title').get()
        print(fzitem)
        yield(fzitem)
