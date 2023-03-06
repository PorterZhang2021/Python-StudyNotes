"""
输入一个正整数判断是不是素数
素数指的是只能被1和自身整除的大于1的数
"""

# 输入一个数
number = int(input('请输入一个数（大于1）- 是否是素数:'))


# 循环1到这个数的值 -> 每个都可以被1和其自身整除
# 那么我只需要验证范围(2, number)即可了
def is_prime(number):
    flag = 0
    for i in range(2, number):
        # 求余运算如果出现相等
        if number % i == 0:
            # 那么就将flag标记为1
            flag = 1

    # 如果flag为1 不是素数
    if flag == 1:
        return False
    # 如果flag为0 是素数
    else:
        return True


print("此数是否是素数:" + str(is_prime(number)))
