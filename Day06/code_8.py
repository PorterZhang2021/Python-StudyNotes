def foo():
    # 此时的a使用的是全局变量
    global a
    a = 200
    # 200
    print(a)


if __name__ == '__main__':
    a = 100
    foo()
    # 200
    print(a)
