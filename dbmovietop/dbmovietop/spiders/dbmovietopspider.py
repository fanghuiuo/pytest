import scrapy
from dbmovietop.items import DbmovietopItem


class DbmovietopspiderSpider(scrapy.Spider):
    name = 'dbmovietopspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        divs=response.xpath('//div[@class="info"]')
        for div in divs:
            movieitem=DbmovietopItem()
            print(movieitem)
            movieitem=self.emptyitem(movieitem)
            movieitem['dym']=div.xpath('./div[1]/a/span[1]/text()').get().strip()
            if div.xpath('./div[2]/p[2]/span/text()').get() is not None:
                movieitem['yjhpj']=div.xpath('./div[2]/p[2]/span/text()').get().strip()
            else:
                movieitem['yjhpj']=' '
            movieitem['dbpf']=div.xpath('./div[2]/div/span[2]/text()').get().strip()
            movieitem['pjrs']=div.xpath('./div[2]/div/span[4]/text()').get().strip()
            url=div.xpath('./div[1]/a/@href').get().strip()
            xxurl=response.urljoin(url)
            yield scrapy.Request(url=xxurl,callback=self.detail,meta={'item':movieitem})
        
    def detail(self,response):
        item=response.meta['item']
        urls=response.xpath('//div[@id="info"]//text()').getall()
        if item['imdbpf'] !=' ':
            for imdburl in urls:
                if 'imdb' in imdburl:
                    imdburl=response
                    yield scrapy.Request(url=imdburl,callback=self.getimdb,meta={'item':item})
                
            
        info=response.xpath('//div[@id="info"]//a/@href').getall()
        
        strinfo=''        
        for i in range(0,len(info)):
            strinfo=strinfo+str(info[i])
        list=strinfo.split('\n')
        print(list)
        yield item
    def getimdb(self,response):
        item=response.meta['item']
        yield item
    def emptyitem(self,item):
        for i in range(0,len(item)):
            item[i]=' '
        return item
    
        