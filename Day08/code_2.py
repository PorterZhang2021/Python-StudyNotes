class Test:
    def __init__(self, foo):
        # 私有属性
        self.__foo = foo

    # 私有方法
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 输出会报错
    test.__bar()
    # 输出会报错
    print(test.__foo)


if __name__ == "__main__":
    main()
