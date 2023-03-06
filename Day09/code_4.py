from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    # 初始化
    def __init__(self, hour=0, minute=0, second=0):
        # 小时
        self._hour = hour
        # 分钟
        self._minute = minute
        # 秒
        self._second = second

    # 类方法
    @classmethod
    def now(cls):
        # 获取本地时间
        ctime = localtime(time())
        # 返回时间
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        # 秒加1
        self._second += 1
        # 如果秒 == 60
        if self._second == 60:
            # 秒重置
            self._second = 0
            # 分钟加1
            self._minute += 1
            # 如果分钟 == 60
            if self._minute == 60:
                # 分钟重置
                self._minute = 0
                # 小时加1
                self._hour += 1
                if self._hour == 24:
                    # 小时重置
                    self._hour

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
            (self._hour, self._minute, self._second)


# 主函数
def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        # 睡眠
        sleep(1)
        # 走字
        clock.run()


if __name__ == '__main__':
    # 函数
    main()
