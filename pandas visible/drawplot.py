# -*-coding:utf-8 *-*
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import numpy as np


def drawplot(strsql):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows = pd.read_sql_query(strsql, ce)
    df = pd.DataFrame.from_records(rows)
    for i in range(0, len(df)):
        df.loc[i, 'zgqw'] = float(str(df.loc[i, 'zgqw']).split('℃')[0])
        df.loc[i, 'zdqw'] = float(str(df.loc[i, 'zdqw']).split('℃')[0])
    plt.figure(dpi=128, figsize=(10, 5))
    x = np.arange(len(df))
    p1, = plt.plot(df['rq'], df['zgqw'], color='red')
    p2, = plt.plot(df['rq'], df['zdqw'], color='blue')
    plt.legend(handles=[p1, p2], labels=['最高气温', '最低气温'], loc='best')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title('沈阳市6月气温走势')
    plt.xlabel('日期')
    plt.ylabel('气温')
    plt.xticks(x, df['rq'], rotation=45)
    for a, b in zip(x, df['zgqw']):
        plt.text(a, b + 0.5, '%.0f' % b, ha='center')
    for a, b in zip(x, df['zdqw']):
        plt.text(a, b + 0.5, '%.0f' % b, ha='center')

    plt.show()

    print(df)


if __name__ == '__main__':
    strsql = "select * from weather where city='沈阳' and rq>='2020-06-01' and rq <='2020-06-20'"
    drawplot(strsql)