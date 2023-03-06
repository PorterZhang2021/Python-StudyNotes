"""
判断一个数是不是回文的函数

1. 判定奇数偶数的情况 -> 此方法过于复杂不适用
2. 对于回文数，从后往前和从前往后最终的结果可能一致
将这个数获得其相反数，验证相反数与原数是否一致
"""


def is_circle(number):
    count = number
    re_number = 0
    # 如果数大于0那么继续
    while count > 0:
        # 将数计算放入
        re_number = re_number * 10 + count % 10
        # 消减一个位数
        count = count // 10

    # 判断两个位数是否相同
    if re_number == number:
        return True
    else:
        return False


# 获取相关的数
number = int(input('请输入一个正整数-判断是否是回文数:'))
# 输出回文情况
print("此数的情况是:" + str(is_circle(number)))
