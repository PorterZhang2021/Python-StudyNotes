# 类测试
class Test:
    # 初始化
    def __init__(self, foo):
        self.__foo = foo

    # 私有方法
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 私有输出
    test._Test__bar()
    # 私有输出
    print(test._Test__foo)


if __name__ == "__main__":
    main()
