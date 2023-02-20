"""

英制单位与公制单位互换

1 in = 2.54 cm

"""

# 输入类型
str = input('请输入你要输入的类型: 英寸(in) or 厘米(cm):')

# 接受类型并计算
# 如果是英制
if str == '英寸' or str == 'in':
    inch = float(input('请输入英寸数:'))
    meter = 2.54 * inch
    print('%.2f英寸 = %.2f厘米' % (inch, meter))
# 如果是公制
elif str == '厘米' or str == 'cm':
    meter = float(input('请输入厘米数:'))
    inch = meter / 2.54
    print('%.2f厘米 = %.2f英寸' % (meter, inch))
# 如果是其他
else:
    print('请输入正确的类型')
