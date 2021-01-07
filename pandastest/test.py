# -*-coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

def mysqltoexcel(strsql):
    eg=create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/book')
    rows=pd.read_sql_query(strsql,eg)
    df=pd.DataFrame.from_records(rows)
    df.to_excel('d:\\test2.xlsx')
if __name__ == "__main__":
    strsql='select * from dbbook '
    mysqltoexcel(strsql)