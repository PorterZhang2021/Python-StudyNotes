"""
设计一个函数返回传入的列表中
最大的第二大的元素的值
"""


def getSecondNum(list):
    # 列表排序 从大到小
    list = sorted(list, reverse=True)
    # 获取列表中的最大与最小的值
    num1, num2 = list[0], list[1]
    # 第二序列即最大的值
    return num1, num2
