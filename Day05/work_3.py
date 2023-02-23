"""
输出100以内的所有素数
素数指的是只能被1和自身整除的正整数（不包括1）。

获取一个数 -> 循环
拿2到其本身进行求余操作，看是否整除 -> 循环
如果整除就跳过，否则输出
"""

# 增加效率
import math

# 输出1到101
for i in range(1, 101):
    # 标记
    flag = False
    # 拿2到其本身进行求余

    for j in range(2, int(math.sqrt(i)) + 1):
    # for j in range(2, i):
        # 如果整除那么退出循环
        if i % j == 0:
            flag = True
            break
    if not flag:
        # 输出素数
        print(i, end=' ')
