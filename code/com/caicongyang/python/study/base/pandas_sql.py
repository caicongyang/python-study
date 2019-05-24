#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

'''
如何用sql的方式打开pandas
'''

from pandas import DataFrame, Series
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['jack', 'tony', 'pony'], 'data1': range(3)})
print(df1)

sql = "select * from df1 where name = 'jack'"
pysqldf = lambda sql: sqldf(sql, globals());
print(pysqldf(sql))
