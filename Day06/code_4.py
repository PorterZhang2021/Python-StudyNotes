# 在参数名前的*表示args是一个可变参数
def add(*args):
    # 总和
    total = 0
    # 计算多个参数的和
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
# 计算1的和
print(add(1))
# 计算1与2的和
print(add(1, 2))
print(add(1, 2, 3))
# 计算1-9中奇数的和
print(add(1, 3, 5, 7, 9))