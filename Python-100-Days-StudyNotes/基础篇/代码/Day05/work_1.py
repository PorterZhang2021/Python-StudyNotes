"""
生成斐波那契数列的前20个数
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

非递归形式：
如果是第一个或者第二个都输出1
如果是第三个的时候将前两个数字相加

起始: number_1 = 1, number_2 = 1
从2开始循环，每次循环更改number
"""

print('1 1 ', end='')
# 两个更改的数放在外面
number_1 = 1
number_2 = 1
for i in range(2, 20):
    number = number_1 + number_2
    print(number, end=' ')
    number_1 = number_2
    number_2 = number

"""
高级版本
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
"""
