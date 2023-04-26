"""
本例子说明了，如果按顺序执行，即使执行两个不相关的任务
那么也需要先等待一个文件下载完成后才能开始下载下一个任务
"""
# 随机整数
from random import randint
# 睡眠
from time import time, sleep

# 下载
def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成!耗费了%d秒' % (filename, time_to_download))

def main():
    # 开始
    start = time()
    # 下载任务
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    # 结束
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()