#-*-coding:'utf-8'-*-
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import matplotlib

def test(strsql):
    ce=create_engine('mysql+pymysql://root:root888@127.0.0.1:3306/pytest')
    rows=pd.read_sql_query(strsql,ce)
    df=pd.DataFrame.from_records(rows)    
    df=df.drop(['id','tq','fx'],axis=1)
    print(df)
    for i in range(0,len(df)):
        df.loc[i,'zgqw']=float(str(df.loc[i,'zgqw']).split('℃')[0])
        df.loc[i,'zdqw']=float(str(df.loc[i,'zdqw']).split('℃')[0])
    print(df)
    #df.plot(x='yzm',y='pjrs',kind='bar',title='测试用')   
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号   
    #plt.xticks(df['yzm'],df['yzm'], rotation=90)
    #plt.xlabel("yzm")
    # 画图（折线图）
    # 设置画布大小及比例
    fig = plt.figure(dpi=128,figsize=(8,6))
    # 设置最高温最低温线条颜色及宽度等信息
    #L1,=plt.plot(df['rq'],df['zdqw'],label='最低气温')
    p1,=plt.plot(df['rq'],df['zdqw'],label='最低气温')
    #L2,=plt.plot(df['rq'],df['zgqw'],label='最高气温')
    p2,=plt.plot(df['rq'],df['zgqw'],label='最高气温')
    #plt.legend(handles=[L1,L2],labels=['最高气温','最低气温'], loc='best')# 添加图例
    plt.legend(handles=[p1,p2],labels=['最高气温','最低气温'], loc='best')# 添加图例
    # 图表格式
    # 设置图形格式
    plt.title('2020年5月上旬大同天气',fontsize=25)  # 字体大小设置为25
    plt.xlabel('日期',fontsize=10)   # x轴显示“日期”，字体大小设置为10
    fig.autofmt_xdate() # 绘制斜的日期标签，避免重叠
    plt.ylabel('气温',fontsize=10)  # y轴显示“气温”，字体大小设置为10
    plt.tick_params(axis='both',which='both',labelsize=10)
    
    # plt.plot(highs,lows,label = '最高气温')
    # 修改刻度
    plt.xticks(df['rq'])  # 由于数据不多，将每天的数据全部显示出来

    plt.show()
if __name__ == "__main__":
    strsql="SELECT * FROM weather where city='沈阳' and rq>'2020-06-01' and rq <'2020-06-30'"
    test(strsql)