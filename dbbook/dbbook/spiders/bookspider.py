# -*- coding:utf-8 -*-
import scrapy
from dbbook.items import DbbookItem


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        tds = response.xpath('//tr[@class="item"]')
        for td in tds:
            bookitem = DbbookItem()
            self.emptyitem(bookitem)
            try:
                bookitem['bookname'] = td.xpath(
                    './td[2]/div[1]/a/text()').get().strip()
                if td.xpath('./td[2]/p[2]/span/text()').get() is not None:
                    bookitem['yjhpj'] = td.xpath(
                        './td[2]/p[2]/span/text()').get().strip()
                else:
                    bookitem['yjhpj'] = ' '
                bookitem['dbpf'] = td.xpath(
                    './td[2]/div[2]/span[2]/text()').get().strip()
                bookitem['pjrs'] = td.xpath(
                    './td[2]/div[2]/span[3]/text()').get().replace(
                        '\n', '').replace('(', '').replace(')', '').strip()
                url = td.xpath('./td[2]/div[1]/a/@href').get().strip()
                newurl = response.urljoin(url)
                yield scrapy.Request(url=newurl,
                                     callback=self.xx,
                                     meta={'item': bookitem})
            except Exception:
                return None
        if response.xpath('//span[@class="next"]/a/@href').get() is not None:
            nexturl = response.xpath(
                '//span[@class="next"]/a/@href').get().strip()
            newnexturl = response.urljoin(nexturl)
            yield scrapy.Request(url=newnexturl, callback=self.parse)
        else:
            return None

    def xx(self, response):
        try:
            newitem = response.meta['item']
            newitem['info'] = response.xpath(
                '//div[@id="info"]//text()').getall()
            newitem['nrjj'] = response.xpath(
                '//div[@id="link-report"]//div[@class="intro"]//text()'
            ).getall()
            newitem['zzjj'] = response.xpath(
                '//div[@class="indent "]//div[@class="intro"]//text()').getall(
                )
            yield newitem
        except Exception:
            return None

    def emptyitem(self, item):
        item['bookname'] = ' '
        item['yjhpj'] = ' '
        item['pjrs'] = ' '
        item['author'] = ' '
        item['cbs'] = ' '
        item['cbn'] = ' '
        item['ys'] = ' '
        item['dj'] = ' '
        item['zz'] = ' '
        item['cs'] = ' '
        item['isbn'] = ' '
        item['nrjj'] = ' '
        item['zzjj'] = ' '
        item['cpf'] = ' '
        item['yzm'] = ' '
        item['fbt'] = ' '
        item['yz'] = ' '
        item['info'] = ' '

        return item
