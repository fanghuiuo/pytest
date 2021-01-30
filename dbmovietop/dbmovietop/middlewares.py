#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   middlewares.py
@Time    :   2021/01/30 16:36:38
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib

import selenium
from selenium.webdriver.chrome.options import Options
import scrapy


class DbmovietopDownloaderMiddleware:
    def process_request(self, request, spider):
        op = Options()
        op.add_argument('--headless')
        op.add_argument('--disable-gpu')
        op.add_argument('--no-sandbox')
        #op.add_argument('--ignore-certificate-errors')
        #op.add_argument('--ignore-ssl-errors')
        op.add_argument('--log-level = 3')
        driver = selenium.webdriver.Chrome(chrome_options=op)
        html = None
        if request.url != 'https://movie.douban.com/top25011':
            driver.implicitly_wait(30)
            driver.get(request.url)
            html = driver.page_source

        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request)
