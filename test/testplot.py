import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def drawplot(strsql):
    ce=create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows=pd.read_sql_query(strsql,ce)
    df=pd.DataFrame.from_records(rows)
    for i in range(0,len(df)):
        df.loc[i,'zgqw']=float(str(df.loc[i,'zgqw']).split('℃')[0])
        df.loc[i,'zdqw']=float(str(df.loc[i,'zdqw']).split('℃')[0])
        df.loc[i,'rq']=str(df.loc[i,'rq'])[5:]
    print(df)
    fig=plt.figure(dpi=128,figsize=(8,6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号   
    p1,=plt.plot(df['rq'],df['zgqw'],label='最高气温',color='red')
    p2,=plt.plot(df['rq'],df['zdqw'],label='最低气温',color='blue')
    plt.legend(handles=[p1,p2],labels=['最高气温','最低气温'],loc='best')
    fig.autofmt_xdate(rotation=45)
    plt.title('沈阳市2020年1月上旬气温走势',fontsize=20)
    plt.xlabel('日期',fontsize=15)
    plt.ylabel('气温',fontsize=15)
    plt.show()
if __name__=="__main__":
    strsql="select * from weather where city='沈阳' and rq <='2020-01-15' and rq>='2020-01-01'"
    drawplot(strsql)