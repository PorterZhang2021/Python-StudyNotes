# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)

# 获取元组中的元素
print(t[0])
print(t[3])

# 遍历元组中的值
for member in t:
    print(member)

# 重新给元组赋值
# t[0] = '王大锤'

# 变量t重新引用了新的元组
# 原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)

# 将元组转换成列表
person = list(t)
print(person)

# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_list = tuple(fruits_list)
print(fruits_list)
