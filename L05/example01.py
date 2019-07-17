import numpy as np
import pandas as pd
from pandas import Series, DataFrame
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x3) 

data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'])
print(df1)
print(df2)

df2.to_excel('df2.xlsx')
df2 = df2.drop(index = ['GuanYu', 'DianWei'])
print(df2)


df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)
print(df2)
print(df2['YuWen'])

df2['YuWen'].astype('str') 
# df2['YuWen'].astype(np.int64) 
print(df2)
print(df2['YuWen'])
