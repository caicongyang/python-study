#!/usr/bin/python
# -*- coding: UTF-8 -*-

#怎么理解python中的axis rank:https://blog.csdn.net/Babyfatliang/article/details/87721282

import numpy as np

a = np.array([1, 2, 3])
print(a)

#修改数组的元素
a[1]=5
print(a)

#打印数组的类型
print(a.dtype)

#打印数组的大小
print(a.shape)


b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)





print('-----------自定义数据结构--------')
student=np.dtype({'names':['name','age','chinese','math','englist'],'formats':['S32','i','i','i','f']})
students=np.array([('jack',45,80,80,90.5),('pony',40,90,90,90.6)],dtype=student)

ages= students[:]['age']
chineses= students[:]['chinese']

print(students.dtype)

#求语文平均数
result = np.mean(chineses)
print ("语文平均数:",result)



print('-----------矩阵中的最大值最小值--------')

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
#矩阵中的最小值
print(np.amin(a))

#矩阵中0轴的最小值
print(np.amin(a,0))

#最大值与最小值之间的差距
print(np.ptp(a))
print(np.ptp(a,0))





print('--------------排序---------------')

b=np.array([[4,1,3],[1,5,2]])
print(b)

print(np.sort(b))

#按0维排序  按x轴来排序
print(np.sort(b,axis=0))

#按1维来排序   按y轴来排序
print(np.sort(b,axis=1))





