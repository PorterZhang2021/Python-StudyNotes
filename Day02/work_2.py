"""

输入圆的半径计算周长和面积

"""
import math

# 获取面积
radius = int(input('请输入圆的半径 = '))

# 运算部分
# 周长
round = 2 * radius * math.pi
# 面积
area = math.pi * radius * radius

# 结果输出
print("半径为%d的圆，周长为%d，面积为%d" % (radius, round, area))

