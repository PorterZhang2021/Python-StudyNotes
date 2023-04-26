def main():
    # 异常捕获
    try:
        with open('.\\res\\ball.png', 'rb') as fs1:
            # 获取数据
            data = fs1.read()
            # 打印结构
            print(type(data))
        with open('.\\res\\new.png', 'wb') as fs2:
            # 写入数据
            fs2.write(data)
    except FileNotFoundError as e:
        # 指定的文件无法打开
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
