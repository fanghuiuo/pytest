import scrapy
from ..items import DbmovietopItem


class DbmovietopspiderSpider(scrapy.Spider):
    name = 'dbmovietopspider'
    allowed_domains = ['movie.douban.com', 'www.imdb.com']  # 允许多个网站
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        divs = response.xpath('//div[@class="info"]')
        for div in divs:
            movieitem = DbmovietopItem()
            print(movieitem)
            movieitem = self.emptyitem(movieitem)
            movieitem['dym'] = div.xpath('./div[1]/a/span[1]/text()').get().strip()
            if div.xpath('./div[2]/p[2]/span/text()').get() is not None:
                movieitem['yjhpj'] = div.xpath('./div[2]/p[2]/span/text()').get().strip()
            else:
                movieitem['yjhpj'] = ' '
            movieitem['dbpf'] = div.xpath('./div[2]/div/span[2]/text()').get().strip()
            movieitem['pjrs'] = div.xpath('./div[2]/div/span[4]/text()').get().strip()
            url = div.xpath('./div[1]/a/@href').get().strip()
            xxurl = response.urljoin(url)
            yield scrapy.Request(url=xxurl, callback=self.detail, meta={'item': movieitem})
        '''if response.xpath('//span[@class="next"]/a/@href').get() is not None:
            nexturl = response.xpath('//span[@class="next"]/a/@href').get().strip()
            newnexturl = response.urljoin(nexturl)
            yield scrapy.Request(url=newnexturl, callback=self.parse)'''

    def detail(self, response):
        item = response.meta['item']

        detailurl = response.url
        if item['imdbpf'] == ' ':
            urls = response.xpath('//div[@id="info"]//a/@href').getall()
            for imdburl in urls:
                if 'imdb' in imdburl:
                    yield scrapy.Request(url=imdburl, callback=self.getimdb, meta={'item': item, 'url': detailurl})

        else:
            item['info'] = response.xpath('//div[@id="info"]//text()').getall()
            item['jqjj'] = response.xpath('//div[@id="link-report"]//span/text()').getall()
            item['pfzb'] = response.xpath('//div[@class="ratings-on-weight"]//div//text()').getall()
            item['cybq'] = response.xpath('//div[@class="tags-body"]//a/text()').getall()
            yield item

    def getimdb(self, response):
        item = response.meta['item']
        url = response.meta['url']
        item['imdbpf'] = response.xpath('//div[@class="ratingValue"]/strong/span/text()').get().strip()
        item['imdbpjrs'] = response.xpath('//div[@class="imdbRating"]/a/span/text()').get().strip()
        yield scrapy.Request(url=url, callback=self.detail, meta={'item': item}, dont_filter=True)  # 防止scrapy过滤重复网址

    def emptyitem(self, item):
        item['dym'] = ' '
        item['yjhpj'] = ' '
        item['dy'] = ' '
        item['bj'] = ' '
        item['zy'] = ' '
        item['lx'] = ' '
        item['gfwz'] = ' '
        item['zpgj'] = ' '
        item['yy'] = ' '
        item['syrq'] = ' '
        item['pc'] = ' '
        item['ym'] = ' '
        item['jqjj'] = ' '
        item['dbpf'] = ' '
        item['pfzb'] = ' '
        item['imdbpf'] = ' '
        item['imdbpjrs'] = ' '
        item['pjrs'] = ' '
        item['pjrs'] = ' '
        item['hjqk'] = ' '
        item['cybq'] = ' '
        return item
