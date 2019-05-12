#!/usr/bin/python
# -*- coding: UTF-8 -*-


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
