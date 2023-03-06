"""
实现判断一个数是不是回文数的函数
"""


def is_palindrome(num):
    """
    判断是一个数是否是回文数
    :param num: num
    :return: 布尔值
    """
    # 临时存放num值
    temp = num
    # 用于存放反转数
    total = 0
    # 如果临时数还有位
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    # 判断两个值是否相同
    return total == num
