import pandas as pd
import numpy as np

exfile = r'C:\Users\Administrator\Desktop\test数据.xls'
df = pd.DataFrame(pd.read_excel(exfile))
df['使用月份'][df['使用月份'] == '二月'] = 2
df['使用月份'][df['使用月份'] == '三月'] = 3
df.to_excel(r'C:\Users\Administrator\Desktop\test数据.xls')

print(df)