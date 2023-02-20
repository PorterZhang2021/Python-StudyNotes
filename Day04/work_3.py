"""
*
**
***
****
*****
"""

# 第一层一个
# 第二层2个
# 第三层3个
number = int(input('请输入数字(构建靠左三角形):'))

for i in range(1, number + 1):
    for j in range(0, i):
        # 如何打在同一行，利用end='' 更改分隔符
        print('*', end='')
    print()

"""
    *
   **
  ***
 ****
*****
"""

# 外层用于换行
# 内层需要完成两个问题
# 空格符 和 *
# 首先输出空格，其次输出*

numbers = int(input('请输入数字(构建靠右三角形):'))

for i in range(1, numbers + 1):
    for j in range(0, numbers - i):
        print(' ', end='')
    for j in range(0, i):
        print('*', end='')
    print()


"""

    *
   ***
  *****
 *******
*********

"""

numbers = int(input('请输入数字(构建金字塔):'))

for i in range(1, numbers + 1):
    # 前面两个部分由第二个三角形组成，
    # 最后加上前面的三角形，进行一行的错位完成金字塔
    # 输出空格
    for j in range(0, numbers - i):
        print(' ', end='')
    # 输出字符
    for j in range(0, i):
        print('*', end='')
    # 输出字符
    for j in range(0, i - 1):
        print('*', end='')
    print()
