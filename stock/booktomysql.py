import pandas as pd
from sqlalchemy import create_engine


def exceltomysql(file):
    ce = create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/djbook')
    df = pd.read_excel(file)
    print(df)
    '''
    导入到mysql，这里有几个关键点，name是Table的名称，if_exists是指Table如果存在的几
    个处理办法，默认是报错，replace是先删后写入，append是添加，chunksize很关键，如
    果数据量较大，可以分批写入，chunksize后的数字就是每次写入的行数，可以加快运行速
    度，而且如果Table不存在，语句能自动创建，还能根据源数据自动调整Table字段的属
    性，效果很好
    '''
    df.to_sql(name='book_dbbook', con=ce, if_exists="append", index=False, chunksize=100)
    print('success')
if __name__ == '__main__':
    file = 'd:/book.xlsx'
    exceltomysql(file)
