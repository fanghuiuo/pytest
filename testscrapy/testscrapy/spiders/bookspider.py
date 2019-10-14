# -*- coding: utf-8 -*-
import scrapy
from testscrapy.items import TestscrapyItem

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    # allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        booklist=response.xpath('//article[@class="product_pod"]')
        for book in booklist:
            bookitem=TestscrapyItem()
            bookitem['name']=book.xpath('./h3/a/@title').get()
            bookitem['price']=book.xpath('./div[@class="product_price"]/p[@class="price_color"]/text()').get()
            print(bookitem)
            pass
        pass
