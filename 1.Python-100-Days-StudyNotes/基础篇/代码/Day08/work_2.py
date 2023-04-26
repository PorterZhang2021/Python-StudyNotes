"""
定义一个类描述平面上的点
并提供移动点和计算到另一个点距离的方法

定义一个点：
    初始化一个点x,y
    移动点 x,y
    指定移动量 dx, dy
    计算两点间的距离
"""
import math


class Point:
    # 初始化 设置一个默认值
    def __init__(self, x=0, y=0):
        # 初始化点x
        self.x = x
        # 初始化点y
        self.y = y

    # 移动点
    def set_post(self, x, y):
        # 设置点x
        self.x = x
        # 设置点y
        self.y = y

    # 移动增量dx, dy
    def move_post(self, dx, dy):
        self.x += dx
        self.y += dy

    # 计算两点之间的距离
    def count_distance(self, point=None):
        # 判断两者哪个大
        x1, x2 = (self.x, point.x) if self.x > point.x else (point.x, self.x)
        y1, y2 = (self.y, point.y) if self.y > point.y else (point.y, self.y)
        # 计算x
        distance_x = x1 - x2
        # 计算y
        distance_y = y1 - y2
        # 计算距离
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        # 输出距离
        return distance

    # 输出其量
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


# 主函数
def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_post(-1, 2)
    print(p2)
    print(p1.count_distance(p2))


if __name__ == '__main__':
    main()
