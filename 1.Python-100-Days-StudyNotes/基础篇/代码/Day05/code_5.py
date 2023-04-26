"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""
# 导入包 用于随机
from random import randint

# 总共的钱数
money = 1000

# 如果还有钱的话
while money > 0:
    # 输出现在的资产
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    # 如果为7或者11
    if first == 7 or first == 11:
        # 输出玩家胜利
        print('玩家胜!')
        # 奖金修改
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        # 奖金修改
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True

print('你破产了，游戏结束!')
