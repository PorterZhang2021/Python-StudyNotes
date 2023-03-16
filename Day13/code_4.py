from random import randint # 随机
from threading import Thread # 线程
from time import time, sleep # 测试时间和睡眠

# 模拟下载函数
def download(filename):
    print('开始下载%s...' % filename)
    # 随机设定时间
    time_to_download = randint(5, 10)
    # 进行睡眠
    sleep(time_to_download)
    # 下载
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

# 主函数
def main():
    # 开始
    start = time()
    # 线程1
    t1 = Thread(target=download, args=('Python从入门到住院.pdf', ))
    # 开启线程
    t1.start()
    # 线程2
    t2 = Thread(target=download, args=('Peking Hot.avi', ))
    # 开启线程
    t2.start()
    # 线程运行
    t1.join()
    t2.join()
    # 结束
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()