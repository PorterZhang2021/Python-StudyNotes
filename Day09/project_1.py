# 导入包
from abc import ABCMeta, abstractclassmethod
from random import randint, randrange

# 战斗者 抽象类


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    # 初始化方法
    def __init__(self, name, hp):
        """
        初始化方法
        :param name: 名字
        :param hp: 生命
        """
        # 初始化名字
        self._name = name
        # 初始化血量
        self._hp = hp

    # 访问器
    @property
    def name(self):
        return self._name

    # 访问器
    @property
    def hp(self):
        return self._hp

    # 设置器
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    # 访问器
    @property
    def alive(self):
        return self._hp > 0

    # 抽象类
    @abstractclassmethod
    def attack(self, other):
        """
        攻击
        :para other: 被攻击的对象
        """
        pass


# 奥特曼类
class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法

        :param name:名字
        :param hp: 生命值
        :param mp: 魔法值
        """

        super().__init__(name, hp)
        # 私有属性魔法值
        self._mp = mp

    # 攻击方法
    def attack(self, other):
        # 攻击力
        other.hp -= randint(15, 25)

    # 必杀技
    def huge_attack(self, other):
        """究极必杀技-打掉对方至少50点或思凡之三的血

        Args:
            other (Fighter): 被攻击的对象
        """

        # 如果魔法值大于等于50
        if self._mp >= 50:
            # 减少魔法值
            self._mp -= 50
            # 伤害
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            # 返回成功
            return True
        else:
            # 攻击
            self.attack(other)
            # 返回没成功
            return False

    # 魔法攻击
    def magic_attack(self, others):
        """ 
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法成功 返回True 否则返回False
        """

        # 如果魔法值大于等于20
        if self._mp >= 20:
            # 魔法值-20
            self._mp -= 20
            # 攻击每一个人
            for temp in others:
                # 如果还活着
                if temp.alive:
                    # 减少hp
                    temp.hp -= randint(10, 15)
            # 返回攻击成功
            return True
        else:
            # 返回攻击失败
            return False

    # 恢复魔法值
    def resume(self):
        """回复魔法值"""
        incr_point = randint(1, 10)
        # 恢复魔法值
        self._mp += incr_point
        # 返回恢复的魔法值数值
        return incr_point

    # 字符显示
    def __str__(self):
        # 返回奥特曼的属性
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


# 小怪兽
class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    # 攻击
    def attack(self, other):
        other.hp -= randint(10, 20)

    # 字符显示
    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


# 判断有没有活着的
def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    # 循环查看每个怪兽
    for monster in monsters:
        # 如果怪兽活着
        if monster.alive > 0:
            # 返回True 只要有一只活着就行
            return True
    # 否则返回false
    return False


# 选中活着的怪兽
def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    # 怪兽的数量
    monsters_len = len(monsters)
    # 循环
    while True:
        # 随机选择索引
        index = randrange(monsters_len)
        # 获取怪兽
        monster = monsters[index]
        # 判断怪兽是否活着
        if monster.alive > 0:
            # 活着就将怪兽输出
            return monster


# 显示奥特曼和小怪兽的信息
def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    # 输出奥特曼
    print(ultraman)
    # 输出小怪兽
    # 循环输出每个怪兽
    for monster in monsters:
        print(monster, end='')  # 分隔每个怪兽


# 主函数
def main():
    # 创建奥特曼
    u = Ultraman('罗浩', 1000, 120)
    # 怪兽1
    m1 = Monster('狄仁杰', 250)
    # 怪兽2
    m2 = Monster('白元芳', 500)
    # 怪兽3
    m3 = Monster('王大锤', 750)
    # 将怪兽放入怪兽堆中
    ms = [m1, m2, m3]
    # 回合数
    fight_round = 1

    # 奥特曼活着并且所有怪兽活着就继续
    while u.alive and is_any_alive(ms):
        # 输出回合信息
        print('========第%02d回合========' % fight_round)
        # 选中一只小怪兽
        m = select_alive_one(ms)
        # 通过随机数选择使用哪个技能
        skill = randint(1, 10)
        # 60%的概率使用普通攻击
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            # 奥特曼攻击
            u.attack(m)
            # 恢复魔法
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        # 30%的概率使用魔法攻击-可能会因为魔法值不足而失败
        elif skill <= 9:
            # 如果魔法足
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            # 如果魔法不足
            else:
                print('%s使用魔法失败.' % u.name)
        # 10%的概率使用究极必杀技-如果魔法值不足则使用普通攻击
        else:
            # 如果魔法足
            if u.huge_attack(m):
                # 使用究极必杀技
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            # 如果魔法不足
            else:
                # 普通攻击
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                # 魔法值恢复
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        # 如果选中的小怪兽没有死就回击奥特曼
        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)

        # 每个回合结束后显示奥特曼和小怪兽的信息
        display_info(u, ms)
        fight_round += 1

    # 输出战斗结束
    print('\n========战斗结束!========\n')
    # 如果奥特曼活着
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    # 否则小怪兽胜利
    else:
        print('小怪兽胜利')


# 主函数调用
if __name__ == '__main__':
    main()
