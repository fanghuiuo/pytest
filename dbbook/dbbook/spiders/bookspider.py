#-*- coding:utf-8 -*-
import scrapy
from dbbook.items import DbbookItem

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/top250/']

    def parse(self, response):
        tds=response.xpath('//tr[@class="item"]')
        for td in tds:
            bookitem=DbbookItem()
            self.emptyitem(bookitem)
            bookitem['bookname']=td.xpath('./td[2]/div[1]/a/text()').get().strip()
            bookitem['yjhpj']=td.xpath('./td[2]/p[2]/span/text()').get().strip()
            bookitem['dbpf']=td.xpath('./td[2]/div[2]/span[2]/text()').get().strip()
            bookitem['pjrs']=td.xpath('./td[2]/div[2]/span[3]/text()').get().replace('\n','').replace('(','').replace(')','').strip()
            url=td.xpath('./td[2]/div[1]/a/@href').get().strip()
            newurl=response.urljoin(url)
            yield scrapy.Request(url=newurl,callback=self.xx,meta={'item':bookitem})
        urls=response.xpath('//div[@class="paginator"]/a/@href').getall()
        for uu in urls:
            ll=response.urljoin(uu)
            yield scrapy.Request(url=ll,callback=self.parse)
    def xx(self,response):
        newitem=response.meta['item']
        newitem['info']=response.xpath('//div[@id="info"]//text()').getall()
        newitem['nrjj']=response.xpath('//div[@id="link-report"]//div[@class="intro"]//text()').getall()
        newitem['zzjj']=response.xpath('//div[@class="indent "]//div[@class="intro"]//text()').getall()
        yield newitem
        pass
    def emptyitem(self,item):
        item['bookname']=' '
        item['yjhpj']=' '
        item['pjrs']=' '
        item['author']=' '
        item['cbs']=' '
        item['cbn']=' '
        item['ys']=' '
        item['dj']=' '
        item['zz']=' '
        item['cs']=' '
        item['isbn']=' '
        item['nrjj']=' '
        item['zzjj']=' '
        item['cpf']=' '
        item['yzm']=' '
        item['fbt']=' '
        item['yz']=' '
        item['info']=' '

        return item
        
