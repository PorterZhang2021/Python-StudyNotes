"""
打印杨辉三角
"""


def main():
    # 输入行数
    num = int(input('Number of rows: '))
    # 杨辉三角
    yh = [[]] * num
    # 用于生成杨辉三角
    for row in range(len(yh)):
        # 杨辉三角的行数 每层元素赋值
        yh[row] = [None] * (row + 1)
        # 用于生成杨辉三角每行的值
        for col in range(len(yh[row])):
            # 头或尾的情况
            if col == 0 or col == row:
                # 这个时候都为1
                yh[row][col] = 1
            else:
                # 其余部分的值
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            # 打印值
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
