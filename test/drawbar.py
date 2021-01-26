import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import label


def drawbar(strsql):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows = pd.read_sql_query(strsql, ce)
    df = pd.DataFrame.from_records(rows)
    print(df)
    for i in range(0, len(df)):
        df.loc[i, 'zgqw'] = float(str(df.loc[i, 'zgqw']).split('℃')[0])
        df.loc[i, 'zdqw'] = float(str(df.loc[i, 'zdqw']).split('℃')[0])
    print(df)
    x = np.arange(len(df))
    barwidth = 0.2
    fig = plt.figure(dpi=128, figsize=(10, 5))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.bar(x - barwidth / 2, df['zgqw'], width=barwidth)
    plt.bar(x + barwidth / 2, df['zdqw'], width=barwidth)
    plt.legend(loc='best')
    fig.autofmt_xdate(rotation=60)
    plt.xticks(x, df['rq'])
    plt.show()


if __name__ == '__main__':
    strsql = "select * from weather where city='沈阳' and rq>='2020-06-01' and rq <='2020-06-20'"
    drawbar(strsql)
