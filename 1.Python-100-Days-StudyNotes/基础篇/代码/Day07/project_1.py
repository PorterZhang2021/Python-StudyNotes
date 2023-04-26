"""
双色球 选号
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    :param balls: 球
    :return: 号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        # 输出选中的号码
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return: 返回一组号码
    """
    # 利用生成器构造函数
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # 随机选择6个值
    selected_balls = sample(red_balls, 6)
    # 选择的球进行排序
    selected_balls.sort()
    # 将选择的结果放入其中
    selected_balls.append(randint(1, 16))
    # 返回
    return selected_balls


def main():
    n = int(input('机选几注: '))
    # 输出供选择多少次双色球
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
