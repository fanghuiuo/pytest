# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class airMiddleware(object):
    def process_request(self,request,spider):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
        #chrome_options.add_argument('--hide-scrollbars')#隐藏滚动条, 应对一些特殊页面
        # 指定谷歌浏览器路径
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        if request.url != 'https://www.aqistudy.cn/historydata/':#不是第一页
            self.driver.get(request.url)
            time.sleep(1)
            print(self.driver.title)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',request=request)

    