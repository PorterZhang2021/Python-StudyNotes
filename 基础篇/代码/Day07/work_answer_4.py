def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    # 索引
    for index in range(2, len(x)):
        # 如果索引大于m1
        if x[index] > m1:
            # m2 等于 m1
            m2 = m1
            # m1 等于 现在的索引
            m1 = x[index]
        # 如果索引大于m2
        elif x[index] > m2:
            # m2 等于 索引
            m2 = x[index]
    # 返回m1和m2
    return m1, m2
