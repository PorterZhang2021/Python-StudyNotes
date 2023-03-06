# 使用集合
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
# 输出集合 集合所有的数只存在一次
print(set1)
# 集合的长度
print('Length = ', len(set1))

# 创建集合的构造器语法 - 面向对象部分会进行详细讲解
# 利用构造器进行构造
set2 = set(range(1, 10))
# 这部分是将元组转化成集合输出
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

# 创建集合的推导式语法 - 推导式也可以用于推导集合
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素
# 增加值
set1.add(4)
# 输出
print(set1)
set1.add(5)
# 输出
print(set1)
# 更新值
set2.update([11, 12])
# 输出
print(set2)

# 丢弃值
set2.discard(5)
# 输出
print(set2)

# 如果有4 那么移除
if 4 in set2:
    set2.remove(4)

print(set1, set2)
# 一个值
print(set3.pop())
print(set3)

# 集合的成员、交集、并集、差集等运算
# 集合的交集
print(set1 & set2)
# 集合的交集另一种形式
print(set1.intersection(set2))

# 集合的并集
print(set1 | set2)
# 集合的并集的另一种形式
print(set1.union(set2))

# 集合的差集
print(set1 - set2)
print(set1.difference(set2))

# 集合的对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))

print(set3 <= set1)
print(set3.issubset(set1))

print(set1 >= set2)
print(set1.issuperset(set2))

print(set1 >= set3)
print(set1.issuperset(set3))



