"""
方法重写
"""
# 获取抽象方法
from abc import ABCMeta, abstractclassmethod

# 定义抽象方法


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    # 初始化
    def __init__(self, nickname):
        # 昵称
        self._nickname = nickname

    # 抽象方法
    @abstractclassmethod
    def make_voice(self):
        """发出声音"""
        pass


# 定义狗类
class Dog(Pet):
    """狗"""

    # 重写方法
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


# 定义猫类
class Cat(Pet):
    """猫"""

    # 重写方法
    def make_voice(self):
        print('%s:喵...喵...' % self._nickname)


# 主函数
def main():
    # 宠物
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    # 循环输出宠物
    for pet in pets:
        # 宠物发出声音
        pet.make_voice()


# 主函数调用
if __name__ == '__main__':
    main()
