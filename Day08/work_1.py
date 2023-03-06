"""
定义一个类描述的数字时钟
"""

# 导入sleep
from time import sleep


# 定义时钟类
class Clock:
    # 初始化时钟
    # 时，分，秒
    def __init__(self, hour=0, minute=0, second=0):
        # 使用保护属性
        self._hour = hour
        self._minute = minute
        self._second = second

    # 走字
    def run(self):
        # 如何走字
        # 每次增加一秒
        self._second += 1
        # 当second == 60 进位
        if self._second == 60:
            # 重置second
            self._second = 0
            # minute自增一次
            self._minute += 1
            # 当minute == 60 进位
            if self._minute == 60:
                # 重置minute
                self._minute = 0
                # hour自增一次
                self._hour += 1
                # 当hour == 24
                if self._hour == 24:
                    # 直接重置
                    self._hour = 0

    # 显示时间
    def show(self):
        # 输出时间
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


# 主函数
def main():
    # 定义一个时钟类
    clock = Clock(23, 58, 58)
    # 进行循环
    while True:
        # 开始走字
        clock.run()
        # 线程暂停1秒
        sleep(1)
        # 显示倒计时
        clock.show()


# 进行输出
if __name__ == '__main__':
    main()
