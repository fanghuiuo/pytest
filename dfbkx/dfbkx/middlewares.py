#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import lib

from selenium.webdriver.firefox.options import Options
import scrapy
from selenium import webdriver
import pytesseract
from PIL import Image
import time
import re


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
        if request.url != 'https://gsms.csair.com':
            driver.implicitly_wait(30)
            driver.get(request.url)
            html = driver.page_source
        else:
            driver.implicitly_wait(30)
            driver.get(request.url)
            username = driver.find_element_by_id('j_username')
            username.clear()
            username.send_keys('your username')
            # 找到password的input标签，填入密码。如果再次点击验证码时密码被清空，那么这段代码要放到while循环内部
            password = driver.find_element_by_id('j_password')
            password.clear()
            password.send_keys('your password')
            # 进行20次尝试
            times = 0
            while True:
                try:
                    yzm = driver.find_element_by_id('inputRand')
                    yzm.clear()
                    element = driver.find_element_by_id('imgCode')
                    # 11111 element.click()
                    # 每次请求的验证码图片都不一样，所以只能截图，保存至本地。
                    driver.save_screenshot('login.png')
                    # windows系统要注意页面缩放比例，如果是150%，那么每项都*1.5。linux系统不需要
                    left = element.location['x'] * 1.0
                    top = element.location['y'] * 1.0
                    right = element.location['x'] * 1.0 + element.size['width'] * 1.0
                    bottom = element.location['y'] * 1.0 + element.size['height'] * 1.0

                    im = Image.open('login.png')
                    im = im.crop((left, top, right, bottom))  # 抠图
                    im.save('validImage.png')
                    im = Image.open('validImage.png')
                    # 进行灰度处理
                    im = im.convert('L')
                    # 设置二值化阈值
                    threshold = 120
                    table = []
                    for i in range(256):
                        if i < threshold:
                            table.append(0)
                        else:
                            table.append(1)
                    # 通过表格转换成二进制图片，1的作用是白色，0就是黑色
                    im = im.point(table, '1')

                    code = pytesseract.image_to_string(im)
                    code = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", code)
                    if len(code) != 4:  # 未识别
                        print('no result')
                    print("ocr识别结果", code)
                    valid_code = driver.find_element_by_id('inputRand')
                    valid_code.clear()
                    valid_code.send_keys(code)

                    time.sleep(1)
                    btnLogin = driver.find_element_by_class_name('submitBtn')
                    btnLogin.click()

                    # 获取cookie
                    login_cookie = driver.get_cookie('ASP.NET_SessionId')
                    total_cookie = 'ASP.NET_SessionId={}; autoLogin=null; user=null; pwd=null'.format(login_cookie['value'])
                    print("total_cookie,{}".format(total_cookie))
                    break

                except Exception:
                    time.sleep(2)
                    times += 1
                    print("破解验证码失败，重试第{}次".format(times))
                    if times == 20:
                        raise RuntimeError

        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8', request=request)
