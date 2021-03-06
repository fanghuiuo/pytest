#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   middlewares.py
@Time    :   2021/01/30 16:33:47
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib

import scrapy
import selenium
from selenium.webdriver.chrome.options import Options


class DbbookDownloaderMiddleware:
    def process_request(self, request, spider):
        op = Options()
        op.add_argument('--headless')
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-gpu')
        html = None
        driver = selenium.webdriver.Chrome(chrome_options=op)
        if not request.url == 'https://book.douban.com/top250':
            driver.implicitly_wait(30)
            driver.get(request.url)
            html = driver.page_source
            driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request)
        else:
            return None
