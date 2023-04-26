"""

输入三条边长，如果能构成三角形就计算周长和面积

"""

# 输入边
edge_1 = float(input('请输入第一条边:'))
edge_2 = float(input('请输入第二条边:'))
edge_3 = float(input('请输入第三条边:'))

# 验证边
# 如果边能构成三角形 任意两边之和大于第三边
if (edge_1 + edge_2 > edge_3) or (edge_1 + edge_3 > edge_2) or (edge_2 + edge_3 > edge_1):
    # 计算周长 三边之和
    round = edge_1 + edge_2 + edge_3
    # 计算面积 海伦公式
    p = (edge_1 + edge_2 + edge_3) / 2
    area = p * (p - edge_1) * (p - edge_2) * (p - edge_3)
    # 输出结果
    print('边:%.1f，%.1f，%.1f构成的三角形，周长为%.2f，面积为%.2f' %
          (edge_1, edge_2, edge_3, round, area))
# 边不能构成三角形
else:
    print("边不能构成三角形")
