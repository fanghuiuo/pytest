#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   dbmovieplt.py
@Time    :   2021/01/30 16:39:22
@Author  :   Jack Fang
@Version :   1.0
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def dbmovieplt(strsql):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows = pd.read_sql_query(strsql, ce)
    df = pd.DataFrame.from_records(rows)
    # df = df.drop(['dy', 'bj', 'jqjj', 'zy'], axis=1)
    for i in range(0, len(df)):
        df.loc[i, 'pjrs'] = float(str(df.loc[i, 'pjrs']).split('人')[0])
    print(df)
    print(df['zpgj'].value_counts().head(30))

    df = df.groupby(['zpgj'], as_index=False).count()
    for i in range(0, len(df)):
        gj = str(df.loc[i, 'zpgj'])
        if '/' in gj:
            lgj = gj.split('/')
            for tt in lgj:
                tt = tt.strip()
                for j in range(0, len(df)):
                    yy = str(df.loc[j, 'zpgj']).strip()
                    if tt == yy:
                        df.loc[j, 'dym'] = float(df.loc[j, 'dym']) + float(df.loc[i, 'dym'])
    for i in range(0, len(df)):
        if '/' in str(df.loc[i, 'zpgj']):
            df.drop(i, inplace=True)

    plt.figure(dpi=128, figsize=(110, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    x = np.arange(len(df))
    width = 0.2
    plt.bar(x, df['dym'], width=width, label='数量')
    for a, b in zip(x, df['dym']):
        plt.text(a, b + 0.5, '%.0f' % b, ha='center')
    plt.title('制片国家')
    plt.xlabel('国家')
    plt.ylabel('数量')
    plt.xticks(x, df['zpgj'], rotation=45)
    plt.show()

    print(df.head(30))
    print(df.columns)


if __name__ == '__main__':
    strsql = "select dym,lx,zpgj,dbpf,pjrs,imdbpf,imdbpjrs from dbmovie "
    dbmovieplt(strsql)
