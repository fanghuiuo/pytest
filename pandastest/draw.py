#-*-coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def draw(strsql):
    ce=create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows=pd.read_sql_query(strsql,ce)
    df=pd.DataFrame.from_records(rows)
    df.drop('id',axis=1,inplace=True)
    df.drop('city',axis=1,inplace=True)
    df.drop('tq',axis=1,inplace=True)
    df.drop('fx',axis=1,inplace=True)
    df.drop('xq',axis=1,inplace=True)
    for i in range(0,len(df)):
        df.loc[i,'zgqw']=str(df.loc[i,'zgqw']).split('℃')[0]
        df.loc[i,'zdqw']=str(df.loc[i,'zdqw']).split('℃')[0]
        tt=str(df.loc[i,'rq']).split('-')
        df.loc[i,'rq']=tt[0]+tt[1]+tt[2]
    print(df)
    df=df.astype(float)
    df.plot(x='rq',y='zgqw')
    plt.show()

if __name__ == "__main__":
    strsql='select * from weather'
    draw(strsql)
    