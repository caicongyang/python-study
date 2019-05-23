#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  numpy as np
import  pandas as pd


from pandas import Series ,DataFrame

#Series 是一个定长的字典

x1=Series([1,2,3,4])
print(x1)

x2=Series(data=[1,2,3,4],index=['a','b','c','d'])
print(x2)


d={'a':1,'b':2}
x3=Series(d)
print(x3)



print('--------------DateFrame-----------')

#DateFrame是一个二维表，类似于mysql 关系型表

data={'chinese':[99,88,100],'math':[99,100,100],'english':[60,100,100]}
df1=DataFrame(data)
print(df1)
df2=DataFrame(data,index=['jack','pony','william'],columns=['chinese','math','english'])
print(df2)

data2={'science':[100,100,100],'geograpy':[100,100,100]}
df3=DataFrame(data2,index=['jack','pony','william'],columns=['science','geograpy'])

print(df3)

#append
df4=df2.append(df3,sort=False)
print(df4)



#merage
df5=pd.merge(df2,df3,left_index=True, right_index=True, how='outer')
print(df5)

'''
merage result

         chinese  math  english  science  geograpy
jack          99    99       60      100       100
pony          88   100      100      100       100
william      100   100      100      100       100

'''

#删除列
df5=df5.drop(columns=['geograpy'])
print(df5)

#删行
df5=df5.drop(index=['pony'])
print(df5)


#删除重复行
df5=df5.drop_duplicates()
print(df5)

print("-------------------------")

#列重命名
df5=df5.rename(columns={'english':'英语'},inplace=True)
print(df5)





data3={'science':['100 ','100 ','100 '],'geograpy':['100','100','100']}
df6=DataFrame(data3,index=['jack','pony','william'],columns=['science','geograpy'])
print(df6)

#前后去空格
df6['science'] = df6['science'].map(str.strip)
print(df6)

#转换类型
df6['science'] = df6['science'].astype(np.int32);
df6['geograpy'] = df6['geograpy'].astype(np.int32);
print(df6)
#数组长度
print(df6['science'].shape)
#数组类型
print(df6['geograpy'].dtype)

print("----------空值判断-----------------")

data4={'science':['a','a ','b'],'geograpy':['c','d','c']}
df7=DataFrame(data4,index=['jack','pony','william'],columns=['science','geograpy'])
print(df7)
#输出空值
print(df7.isnull)
print(df7.isnull().any())

print(df7['science'].apply(str.upper))



print("--------------apply 函数的使用---------------")
data5={'science':[100,100,100],'geograpy':[100,100,100]}
df8=DataFrame(data3,index=['jack','pony','william'],columns=['science','geograpy'])

def plus(x):
    return int(x)+10

df8['science'] = df8['science'].apply(plus)
print(df8)










