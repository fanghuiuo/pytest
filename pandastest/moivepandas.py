#-*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

def mysqltoexcel():
    eg=create_engine('mysql+pymysql://root:root888@1227.0.0.1:3306/pytest')
    strsql='select * from dbmoive'
    rows=pd.read_sql_query(strsql,eg)
    df=pd.DataFrame.from_records(rows)
    df.to_excel('d:\\dbmoive.xlsx')