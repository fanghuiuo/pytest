#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   debug.py
@Time    :   2021/01/30 16:37:37
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib

from scrapy.cmdline import execute
import os
# 获取当前文件路径
dirpath = os.path.dirname(os.path.abspath(__file__))
# 切换到scrapy项目路径下
os.chdir(dirpath[:dirpath.rindex("\\")])
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy', 'crawl', 'weatherspider'])
