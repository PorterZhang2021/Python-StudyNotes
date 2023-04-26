def foo():
    # 这里的a只是局部变量
    a = 200
    # 200
    print(a)


if __name__ == '__main__':
    a = 100
    foo()
    # 100
    print(a)
