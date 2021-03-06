import pandas as pd
from sqlalchemy import create_engine


def mysqltoexcel(strsql):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows = pd.read_sql_query(strsql, ce)
    df = pd.DataFrame.from_records(rows)
    df.to_excel('d:/movie.xlsx', encoding='utf-8')


if __name__ == '__main__':
    strsql = "select * from dbmovie "
    mysqltoexcel(strsql)
