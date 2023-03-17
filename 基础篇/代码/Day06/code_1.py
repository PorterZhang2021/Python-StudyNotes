"""
计算4个未知数=8，有多少个正整数解的情况
实际上是分成四组每组至少一个苹果共有多少种方案
"""

# 输入两个数
m = int(input('m = '))
n = int(input('n = '))

# 实现阶乘
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)
