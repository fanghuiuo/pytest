/#-*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

def mysqltodf(strsql):
    ce=create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows=pd.read_sql_query(strsql,ce)
    df=pd.DataFrame.from_records(rows)
    df.drop('id',axis=1,inplace=True)
    print(df.info())
    print(df.duplicated())
    print(df['zpgj'])
    print(df['zpgj'].value_counts())
if __name__ == "__main__":
    strsql='select * from dbmovie'
    mysqltodf(strsql)