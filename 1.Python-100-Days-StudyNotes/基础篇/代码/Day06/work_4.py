# 引用前两个的包即可完成此任务
from work_3 import is_prime
from work_2 import is_circle


def is_circle_and_prime(number):
    # 判断是否满足回文与素数
    if is_circle(number) and is_prime(number):
        # 满足
        return True
    # 不满足
    return False


# 输入相关的数
number = int(input('请输入一个数-验证是否满足回文与素数:'))

# 输出情况
print('此数满足回文素数的情况为:' + str(is_circle_and_prime(number)))
