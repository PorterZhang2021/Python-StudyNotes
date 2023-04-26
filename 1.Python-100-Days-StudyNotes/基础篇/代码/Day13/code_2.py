"""
不同进程下的下载
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    # 开始
    start = time()
    # 进程1
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    # 进程1开启
    p1.start()
    # 进程2
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    # 进程2开启
    p2.start()
    # 加入进程
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()