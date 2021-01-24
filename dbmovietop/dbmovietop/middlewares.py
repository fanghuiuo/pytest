import selenium
from selenium.webdriver.chrome.options import Options
import scrapy

class DbmovietopDownloaderMiddleware:
   
    def process_request(self, request, spider):
        op=Options()
        op.add_argument('--headless')
        op.add_argument('--disable-gpu')
        op.add_argument('--no-sandbox')
        driver=selenium.webdriver.Chrome(chrome_options=op)
        if request.url !='https://movie.douban.com/top250':
            driver.implicitly_wait(30)
            driver.get(request.url)
            html=driver.page_source
            driver.quit()
        
        return scrapy.http.HtmlResponse(url=request.url,body=html.encode('utf-8'),encoding='utf-8',request=request)

    