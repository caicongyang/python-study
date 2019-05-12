#!/usr/bin/python
# -*- coding: UTF-8 -*-


import  pandas as pd
from  pandas import  Series,DataFrame



'''
result 
  Unnamed: 0  english  chinese  math
0       jack      100       80    50
1       pony       90       90    90
2     willia      100      100   100

'''



filePath='/Users/caicongyang/PycharmProjects/pandas_test_data.xlsx'
score=DataFrame(pd.read_excel(filePath))
score.to_excel(filePath)
print(score)



