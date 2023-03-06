def foo():
    # 函数内局部变量
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        # 函数内局部变量
        c = True
        print(a)
        print(b)
        print(c)
    # 输出函数
    bar()
    # print(c)
    # NameError: name 'c' is not defined


if __name__ == '__main__':
    # 全局变量
    a = 100
    # print(b)
    # NameError: name 'b' is not defined
    foo()
