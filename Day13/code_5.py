# 导入包
from random import randint
from threading import Thread
from time import time, sleep

# 设计下载类
class DownloadTask(Thread):

    # 初始化
    def __init__(self, filename):
        # 初始化
        super().__init__()
        self._filename = filename

    # 运行
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成!耗费了%d秒' % (self._filename, time_to_download))

# 主函数
def main():
    # 开始
    start = time()
    # 下载文件
    t1 = DownloadTask('Python从入门到住院.pdf')
    # 开启线程
    t1.start()
    # 下载文件
    t2 = DownloadTask('Peking Hot.avi')
    # 开启线程
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
