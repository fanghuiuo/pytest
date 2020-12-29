# -*- coding: utf-8 -*-

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DbmovieDownloaderMiddleware:
   

    def process_response(self, request, response, spider):
        op=Options()
        op.add_argument('--headless')
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-gpu')
        self.driver=webdriver.Chrome(chrome_options=op)
        if not request.url=='movie.douban.com/top250':
            self.driver.implicitly_wait(10)
            self.driver.get(request.url)
            html=self.driver.page_source
            self.driver.quit()        
        
        return scrapy.http.HtmlResponse(url=request.url,body=html.encode('utf-8'),encoding='utf-8',request=request)

    