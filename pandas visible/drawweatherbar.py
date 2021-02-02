#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   drawweatherbar.py
@Time    :   2021/02/02 08:56:02
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
        df.loc[i, 'zgqw'] = float(str(df.loc[i, 'zgqw']).split('℃')[0])
        df.loc[i, 'zdqw'] = float(str(df.loc[i, 'zdqw']).split('℃')[0])
    print(df)
    plt.figure(dpi=128, figsize=(12, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    x = np.arange(len(df))
    width = 0.2
    plt.bar(x - 0.5 * width, df['zgqw'], width=width, color='red', label='最高气温')
    plt.bar(x + 0.5 * width, df['zdqw'], width=width, color='blue', label='最低气温')
    plt.xticks(x, df['rq'], rotation=45)
    plt.xlabel('日期')
    plt.ylabel('温度')
    plt.title('沈阳市气温走势')
    for a, b in zip(x, df['zgqw']):
        plt.text(a - 0.5 * width, b + 0.2, b, ha='center')
    for a, b in zip(x, df['zdqw']):
        plt.text(a + 0.5 * width, b + 0.2, b, ha='center')
    plt.show()


if __name__ == '__main__':
    strsql = "select * from weather where city='沈阳' and rq>='2020-05-06' and rq <='2020-05-20'"
    drawbar(strsql)