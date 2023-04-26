"""
设计一个函数返回给定文件名的后缀名
我给定一个文件的名字然后它进行截取
截取的部分主要是.后面的内容
找到.的位置，然后进行截取
"""


def getSuffix(filename):
    # 找到点的索引
    suffix_index = filename.index('.')
    # 对点后面的值开始切割字符
    suffixName = filename[suffix_index + 1:]
    # 返回切割后的字符
    return suffixName
