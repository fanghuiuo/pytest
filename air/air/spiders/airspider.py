import scrapy
from air.items import AirDayItem
from air.items import AirMonthItem


class AirspiderSpider(scrapy.Spider):
    name = 'airspider'
    allowed_domains = ['www.aqistudy.cn/historydata']
    start_urls = ['http://www.aqistudy.cn/historydata/']

    def parse(self, response):
        urls=response.xpath('//div[@class="panel panel-info"]/div[2]/ul//li/a/@href').getall()
        for url in urls:
            yfitem=AirMonthItem()
            self.emptyitem(yfitem,'yf')
            newurl=response.urljoin(url)
            yield scrapy.Request(url=newurl,callback=self.yfxx,meta={'item':yfitem})
        
    def yfxx(self,response):
        
        pass
    
    def emptyitem(self,item,fl):
        item['aqi']=' '
        item['zldj']=' '
        item['pm2']=' '
        item['pm10']=' '
        item['so2']=' '
        item['co']=' '
        item['no2']=' '
        item['o38h']=' '
        if fl=='yf':
            item['yf']=' '
        else:
            item['rq']=' '
        return item        
        
