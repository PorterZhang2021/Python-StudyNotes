"""
打印杨辉三角
杨辉三角规律
形式可以后面考虑
1
1 1
1 2 1
外层不变 不管如何头与末尾都有1
上一层的值两两组合构成下一层

前两层需要直接给定
后面的通过前面一层获取中间的值
中间值的获取：
循环
"""

# 获取输入值
numbers = int(input('请输入需要的杨辉三角的层数:'))


def getShape(numbers):
    # 杨辉三角情况
    # 构建初始杨辉三角
    # 如果numbers为1输出一层
    if numbers == 1:
        shape = [[1]]
    # 如果numbers为2输出两层
    elif numbers == 2:
        shape = [[1], [1, 1]]
    # 如果numbers为2以上，输出
    else:
        # 给定起始
        shape = [[1], [1, 1]]
        # 剩余层数
        s_number = numbers - 2
        row = 1
        # 层数构建
        while row <= s_number:
            # 拿层数进行循环
            # 获取上一层的长度
            length = len(shape[row])
            # 构建初始情况
            temp_shape = [1]
            for i in range(length - 1):
                num = shape[row][i] + shape[row][i + 1]
                temp_shape.append(num)
            temp_shape.append(1)
            # 将其加入到三角内
            shape.append(temp_shape)
            # 新的一层
            row += 1
    return shape


print(getShape(numbers))
