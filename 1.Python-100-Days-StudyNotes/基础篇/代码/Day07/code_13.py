# 斐波那契生成器
def fib(n):
    # 设定初始的两个值
    a, b = 0, 1
    # 循环次数
    for _ in range(n):
        # Fn = Fn-1 + Fn-2
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
