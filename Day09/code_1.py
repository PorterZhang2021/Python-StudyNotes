class Person(object):  # 定义一个人类
    # 初始化 属性有name和age
    def __init__(self, name, age):
        # 私有属性
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    # play()方法
    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


# 主函数
def main():
    # 定义一个人
    person = Person('王大锤', 12)
    # 玩游戏
    person.play()
    # 年龄
    person.age = 22
    # 玩游戏
    person.play()

    # 置换其姓名
    # person.name = '白元芳'


if __name__ == '__main__':
    # 主函数
    main()
