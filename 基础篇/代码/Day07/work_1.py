"""
跑马灯文字
字符串和常用数据结构
字符串
实现跑马灯
从头到尾每次输出一个字符
输出完字符后重置
继续从头到尾每次输出一个字符
控制跑马灯输出时间
"""
from time import sleep

# 获取字符
strings = input('请输入你要进行跑马灯的文字:')
second = int(input('请输入跑马灯的速度(s):'))

# 一直重复循环
while True:
    # 实现输出字符
    for str in strings:
        print(str)
        sleep(second)
