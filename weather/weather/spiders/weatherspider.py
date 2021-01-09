import scrapy
from weather.items import WeatherItem

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherspider'
    allowed_domains = ['lishi.tianqi.com']
    start_urls = ['http://lishi.tianqi.com/shenyang/index.html/']

    def parse(self, response):
        urls=response.xpath('//div[@class="linegraphbox"]//div[@class="lishifengxiang"]//ul//li/a/@href').getall()
        for url in urls:
            rqitem=WeatherItem()
            self.emptyitem(rqitem)
            newurl=response.urljoin(url)
            scrapy.Request(url=newurl,callback=self.xx,meta={'item':rqitem})
            pass
        pass
    def xx(self,response):
        pass
    def emptyitem(self,item):
        item['rq']=' '
        item['zgqw']=' '
        item['zdqw']=' '
        item['tq']=' '
        item['fx']=' '
        return item
