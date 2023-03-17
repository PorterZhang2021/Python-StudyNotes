"""
CRAPS赌博游戏
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

解决方案：
给出两个随机值，组合成筛子的值
玩家摇色子次数
第一次 7或11 玩家直接胜利 2，3或12 庄家胜利 其他点数 继续
后面次数 如果是7点那么庄家胜，如果是和第一次点数一样，玩家胜利，
否则继续
"""
import random

print('CRAPS游戏开始:')

count = 1
# 游戏持续进行
while True:
    input('请开始摇色子 - 按ENTER确认')

    # 此为闭区间
    number_1 = random.randint(1, 6)
    number_2 = random.randint(1, 6)
    # 获取到点数
    number = number_1 + number_2

    print('第%d次摇筛子，一筛子%d，二筛子%d，本次结果为:%d' % (count, number_1, number_2, number))

    # 第一次
    if count == 1:
        # 如果是7或11 玩家胜利
        if number == 7 or number == 1:
            print('恭喜玩家，您获胜了')
            break
        # 如果是2，3或12 庄家胜利
        elif number == 2 or number == 3 or number == 12:
            print('玩家您输了，庄家获胜')
            break
        # 记录数值
        else:
            re_number = number
    # 其他情况
    else:
        # 如果要出7点 庄家胜
        if number == 7:
            print('玩家您输了，庄家获胜')
            break
        # 如果摇出第一次相同的点数 玩家胜
        elif number == re_number:
            print('恭喜玩家，您获胜了')
            break
    count += 1
