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





