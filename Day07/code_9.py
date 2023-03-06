list1 = [1, 3, 5, 7, 100]

# 添加元素
list1.append(200)
list1.insert(1, 400)

# 合并两个列表
list1.extend([1000, 2000])
# list1 += [1000, 2000]
print(list1)
print(len(list1))

# 先通过成员运算判断元素是否在列表中
# 如果存在就删除该元素
if 3 in list1:
    # 这个元素在 可以删除
    list1.remove(3)
if 1234 in list1:
    # 这个元素不存在 所以没有进入
    list1.remove(1234)
# 输出删除后的结果
print(list1)

# 从指定的位置删除元素
# 这个删除首元素
list1.pop(0)
# 这个删除尾元素
list1.pop(len(list1) - 1)
print(list1)

# 清空列表元素
list1.clear()
print(list1)
