from time import time

def main():
    # 总数
    total = 0
    # 数量
    number_list = [x for x in range(1, 100000001)]
    # 开始
    start = time()
    for number in number_list:
        total += number
    print(total)
    # 结束
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
