#!/usr/bin/python
# -*- coding: UTF-8 -*-
print('hello,world')

print('-----------变量使用：-----------------')

name='tom'
sum=100+100
print('sum=%d' %sum)
print('name=%s' %name)



print('-----------if else-----------------')


score = 91
if score  > 90:
    print('good')
else:
    print('normal')


print('-----------for each-----------------')

sum=0
for number in range(11):
    sum = sum + number
print (sum)


print('-----------while-----------------')
sum = 0
number = 1
while number < 11:
    sum = sum + number
    number = number + 1
print(sum)



print('-----------list-----------------')

list1=['a','b','d']
list1.append('d')
print(list1)

# 打出列表的长度
print(len(list1))

#insert
list1.insert(0,'mm')
print(list1)

#删除队尾的元素
list1.pop();
print(list1)




print('-----------tuple-----------------')
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

print(tup1)

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)



print('-----------dictionary字典-----------------')
score ={"jack":"alibaba","pony":"tencent"}
score["willam"]="netease"
print(score)
score.pop('jack')

#获取字段的内的值
print(score.get("jack"))



print('-----------set--------------------------')
s = set(['a','b','c'])
s.add('a')
print(s)
print('c' in s)


print('-----------function--------------------------')
def add(a,b):
    return  a + b

print(add('a',"b"))
print(add(3,4))