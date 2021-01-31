#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   dbpfbar.py
@Time    :   2021/01/31 17:35:17
@Author  :   Jack Fang
@Version :   1.0
'''
# import lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


def drawbar(strsql):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows = pd.read_sql_query(strsql, ce)
    df = pd.DataFrame.from_records(rows)
    for i in range(0, len(df)):
        df.loc[i, 'pjrs'] = float(str(df.loc[i, 'pjrs']).split('人')[0])
        df.loc[i, 'dbpf'] = float(df.loc[i, 'dbpf'])
        df.loc[i, 'imdbpf'] = float(df.loc[i, 'imdbpf'])
        df.loc[i, 'imdbpjrs'] = float(str(df.loc[i, 'imdbpjrs']).replace(',', ''))
    print(df)
    plt.figure(dpi=128, figsize=(12, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    x = np.arange(len(df))
    width = 0.3
    plt.bar(x - 0.5 * width, df['dbpf'], width=width, color='red', label='豆瓣评分')
    plt.bar(x + 0.5 * width, df['imdbpf'], width=width, color='blue', label='imdb评分')
    #plt.bar(x + 0.5 * width, df['pjrs'], label='豆瓣评价人数')
    #plt.bar(x - 0.5 * width, df['imdbpjrs'], label='imdb评价人数')
    plt.legend(loc='best')
    for a, b in zip(x, df['dbpf']):
        plt.text(a - 0.5 * width, b + 0.2, b, ha='center')
    for a, b in zip(x, df['imdbpf']):
        plt.text(a + 0.5 * width, b + 0.2, b, ha='center')
    plt.title('豆瓣 imdb 评分对比', fontsize=20)
    plt.xlabel('电影名')
    plt.ylabel('评分')
    plt.xticks(x, df['dym'], rotation=70)
    plt.show()


if __name__ == '__main__':
    strsql = "select * from dbmovie limit 20"
    drawbar(strsql)
