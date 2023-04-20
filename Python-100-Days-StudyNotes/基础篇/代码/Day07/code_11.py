list1 = ['orangel', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)

# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
# 此排序是按照首个字母的顺序排序
# 这里开启了反转
list3 = sorted(list1, reverse=True)
print(list3)

# 通过key关键字参数指定根据字符串长度进行排序
# 而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)

list1.sort(reverse=True)
print(list1)