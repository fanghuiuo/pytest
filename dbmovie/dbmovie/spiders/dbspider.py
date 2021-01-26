# -*- coding: utf-8 -*-
import scrapy
from dbmovie.items import DbmovieItem


class DbspiderSpider(scrapy.Spider):
    name = 'dbspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        divs = response.xpath('//div[@class="info"]')
        for div in divs:
            ditem = DbmovieItem()
            self.emptyitem(ditem)
            ditem['dym'] = div.xpath('./div[1]/a/span[1]/text()').get().strip()
            url = div.xpath('./div[1]/a/@href').get().strip()
            ll = response.urljoin(url)
            yield scrapy.Request(url=ll,
                                 callback=self.xx,
                                 meta={'item': ditem})
        if response.xpath('//span[@class="next"]/a/@href').get() is not None:
            nexturl = response.xpath(
                '//span[@class="next"]/a/@href').get().strip()
            newnexturl = response.urljoin(nexturl)
            yield scrapy.Request(url=newnexturl, callback=self.parse)
        else:
            return None

    def xx(self, response):
        newitem = response.meta['item']
        newitem['info'] = response.xpath('//div[@id="info"]//text()').getall()
        newitem['jj'] = response.xpath(
            '//span[@property="v:summary"]/text()').get().strip()
        newitem['dbpf'] = response.xpath(
            '//div[@class="rating_self clearfix"]/strong/text()').get().strip(
            )
        newitem['pjrs'] = response.xpath(
            '//div[@class="rating_sum"]/a/span/text()').get().strip()
        yield newitem

    def emptyitem(self, item):
        item['dym'] = ' '
        item['dy'] = ' '
        item['bj'] = ' '
        item['zy'] = ' '
        item['lx'] = ' '
        item['zpgj'] = ' '
        item['yy'] = ' '
        item['syrq'] = ' '
        item['pc'] = ' '
        item['ym'] = ' '
        item['jj'] = ' '
        item['dbpf'] = ' '
        item['pjrs'] = ' '
        return item
