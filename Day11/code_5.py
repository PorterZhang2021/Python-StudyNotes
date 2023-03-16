from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    # 判断素数
    for factor in range(2, int(sqrt(n)) + 1):
        # 如果求余之后等于0
        if n % factor == 0:
            # 返回错误
            return False
    # 不为1则返回True
    return True if n != 1 else False

def main():
    # 创建文件
    filenames = ('.\Day11\\res\\a.txt', '.\Day11\\res\\b.txt','.\Day11\\res\\c.txt')
    fs_list = []
    # 异常捕获
    try:
        # 文件遍历
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            # 是素数
            if is_prime(number):
                if number < 100:
                    # 文件1写入
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    # 文件2写入
                    fs_list[1].write(str(number) + '\n')
                else:
                    # 文件3写入
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


if __name__ == '__main__':
    main()
