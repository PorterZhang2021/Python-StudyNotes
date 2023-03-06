from random import randint


# 定义一个摇色子函数
def roll_dice(n=2):
    """ 摇色子 """
    # 筛子值的总和
    total = 0
    # 摇筛子的次数
    for _ in range(n):
        # 摇色子的次数与总数相加
        total += randint(1, 6)
    # 返回摇色子的总值
    return total


def add(a=0, b=0, c=0):
    """ 三个数相加 """
    # 返回三个数相加
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗筛子
print(roll_dice())
# 摇三颗筛子
print(roll_dice(3))
# 这里模拟的算是一种重载
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
