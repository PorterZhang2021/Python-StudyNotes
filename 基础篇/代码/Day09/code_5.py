"""
继承和多态
"""

# 人类


class Person(object):
    """人"""

    # 初始化
    def __init__(self, name, age):
        # 私有属性
        self._name = name
        # 私有属性
        self._age = age

    # 装饰器 getter
    @property
    def name(self):
        # 获取姓名
        return self._name

    # 装饰器 getter
    @property
    def age(self):
        # 获取年龄
        return self._age

    # 设置年龄
    @age.setter
    def age(self, age):
        # 设置年龄
        self._age = age

    # 玩耍
    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    # 看电视
    def watch_av(self):
        # 当年龄大于等于18的时候
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

# 学生类


class Student(Person):
    """学生"""

    # 初始化 多态
    def __init__(self, name, age, grade):
        # 继承
        super().__init__(name, age)
        # 私有属性
        self._grade = grade

    # 装饰器 getter
    @property
    def grade(self):
        return self._grade

    # 设置器 年级设置
    @grade.setter
    def grade(self, grade):
        # 年级设置
        self._grade = grade

    # 学习设置 课程
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


# 老师
class Teacher(Person):
    """老师"""

    # 初始化继承
    def __init__(self, name, age, title):
        super().__init__(name, age)
        # 私有属性
        self._title = title

    # 访问器
    @property
    def title(self):
        return self._title

    # 设置器
    @title.setter
    def title(self, title):
        self._title = title

    # 教课
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


# 主函数
def main():
    # 学生
    stu = Student('王大锤', 15, '初三')
    # 学习
    stu.study('数学')
    # 看电视
    stu.watch_av()

    # 老师
    t = Teacher('罗浩', 38, '专家')
    # 教课
    t.teach('Python程序设计')
    # 看电视
    t.watch_av()


# 主函数
if __name__ == '__main__':
    main()
