"""
定义类问题
"""


# 构建一个学生类
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 进行初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 一个方法
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8 要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法（驼峰标识）
    # 另一个方法
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


# 主函数
def main():
    # 创建学生对象并指定姓名
    stu1 = Student('罗昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()

    # 创建另一个学生对象并指定姓名
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
