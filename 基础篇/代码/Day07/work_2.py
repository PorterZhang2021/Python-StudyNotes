"""
设计一个函数，产生指定长度的验证码
验证码由大小写字母和数字构成

# 指定长度 函数 getCode
# 每次随机获取一个数 -> 如何做
# ASCII码 直接输入对应的ASCII码
# 打表 直接存入内存中打表 -> 实现方式较为容易
"""

import random

def getCode(n):
    # 字符码
    code = ''
    # 打表
    # 小写字符
    sub_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    # 大写字符
    sup_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G'
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    # 数字
    numbers = ['1', '2', '3', '4', '5',
               '6', '7', '8', '9', '0']

    # 进行随机取数
    # 进行循环
    while n > 0:
        # 取出去哪一个表格
        tables = random.randint(0, 2)
        # 取出随机数
        if tables == 0:
            sub_chars_num = random.randint(0, 25)
            code += sub_chars[sub_chars_num]
        elif tables == 1:
            sup_chars_num = random.randint(0, 25)
            code += sup_chars[sup_chars_num]
        elif tables == 2:
            numbers_num = random.randint(0, 9)
            code += numbers[numbers_num]

        # 取完后n--
        n-=1

    # 返回随机码
    return code

