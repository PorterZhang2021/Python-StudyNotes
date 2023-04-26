list1 = [1, 3, 5, 7, 100]
print(list1)

# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)

# 计算列表长度(元素个数)
print(len(list1))

# 下标(索引)运算
print(list1[0])
print(list1[4])
# print(list1[5])
print(list[-1])
print(list1[-3])

list1[2] = 300
print(list1)

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)

# 通过enumerate函数处理列表之后再遍历也可以
# 同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
