from math import sqrt


class Triangle(object):
    # 初始化
    def __init__(self, a, b, c):
        # 初始化私有属性
        self._a = a
        self._b = b
        self._c = c

    # 静态方法定义
    @staticmethod
    def is_vaild(a, b, c):
        # 判断是否是三角形
        return a + b > c and b + c > a and a + c > b

    # 返回周长
    def perimeter(self):
        # 返回周长
        return self._a + self._b + self._c

    # 返回面积
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


# 主函数
def main():
    # 三角形三个边
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    # 判断是否是三角形
    if Triangle.is_vaild(a, b, c):
        # 实例化此三角形
        t = Triangle(a, b, c)
        # 获得三角形周长
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法
        # 但是要出入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        # 面积
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main()
