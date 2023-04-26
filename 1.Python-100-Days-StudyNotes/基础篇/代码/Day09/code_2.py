class Person(object):  # 定义一个人类
    # 限定Person对象只能绑定_name，_age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    # 初始化 姓名与年龄
    def __init__(self, name, age):
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
    person = Person('王大锤', 22)
    person.play()  # 进行游玩
    # 此属性可以绑定
    person._gender = '男'  # 修改性别
    # 下面一个限定绑定了
    # person._is_gay = True


if __name__ == '__main__':
    main()
