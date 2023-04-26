"""
定义一个类描述平面上的点
并提供移动点和计算到另一个点距离的方法
"""

from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return: 无
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        :return: 无
        """

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        :return: 无
        """
        # 横坐标增量
        dx = self.x - other.x
        # 纵坐标增量
        dy = self.y - other.y
        # 返回距离
        return sqrt(dx ** 2 + dy ** 2)

    # 字符串
    def __str__(self):
        # 返回字符串
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()
