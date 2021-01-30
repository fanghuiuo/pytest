#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   middlewares.py
@Time    :   2021/01/30 16:37:56
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib

import selenium
from selenium.webdriver.chrome.options import Options
import scrapy


class WeatherDownloaderMiddleware:
    def process_request(self, request, spider):
        op = Options()
        op.add_argument('--headless')
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-gpu')
        driver = selenium.webdriver.Chrome(chrome_options=op)
        html = None
        if request.url != 'lishi.tianqi.com/shenyang/index.html':
            driver.implicitly_wait(10)
            driver.get(request.url)
            html = driver.page_source
            driver.quit()

        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request)
