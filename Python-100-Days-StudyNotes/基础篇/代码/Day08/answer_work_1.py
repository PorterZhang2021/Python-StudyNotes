from time import sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param self: 自生
        :param hour: 时
        :param minute: 分
        :param second: 秒
        :return: 无
        """
        # 私有属性
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        走字
        :param self: 自身
        :return: 无
        """
        # 私有属性 秒自增
        self._second += 1
        # 如果秒为60时
        if self._second == 60:
            # 重置秒
            self._second = 0
            # 增加一分钟
            self._minute += 1
            # 如果分为60时
            if self._minute == 60:
                # 重置分
                self._minute = 0
                # 减少一小时
                self._hour += 1
                # 如果时间为24小时
                if self._hour == 24:
                    # 重置时
                    self._hour = 0

    def show(self):
        """
        显示时间
        :return: 无
        """
        # 返回时间，分钟，秒
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


# 主函数
def main():
    # 时钟
    clock = Clock(23, 59, 58)
    # 循环执行
    while True:
        print(clock.show())
        # 睡眠1秒
        sleep(1)
        # 运行
        clock.run()


if __name__ == '__main__':
    main()
