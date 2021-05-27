#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import lib

from selenium.webdriver.firefox.options import Options
import scrapy
from selenium import webdriver


class DfbkxDownloaderMiddleware:
    def process_request(self, request, spider):
        op = Options()
        # 设置隐身模式
        op.add_argument("--private")
        # op.AddArgument("-safe-mode")
        # 禁止GPU渲染
        op.add_argument("--disable-gpu")
        # 忽略错误
        op.add_argument("ignore-certificate-errors")
        # 禁止浏览器被自动化的提示
        op.add_argument("--disable-infobars")
        # 不显示浏览器界面
        # op.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=op)
        html = None
        if request.url != 'https://movie.douban.com/top25011':
            driver.implicitly_wait(30)
            driver.get(request.url)
            html = driver.page_source

        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request)
