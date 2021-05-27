import scrapy


class KxspiderSpider(scrapy.Spider):
    name = 'kxspider'
    allowed_domains = ['gsms.csair.com']
    start_urls = ['http://gsms.csair.com/']

    def parse(self, response):
        pass
