"""

输入年份判断是不是闰年

条件1：公历年份是4的倍数且不是100的倍数
条件2：公历年份是整百数，且必须是400的倍数才是世纪闰年。

"""

# 输入年份
year = int(input('请输入年份 = '))

# 条件判断
# 是否是普通闰年
# 这个写法中 year % 100 == 1 是错误的没有判断完全
# 可以改成 year % 100 != 0 也就说明了其不为100倍数
# flag_year_1 = (year % 4 == 0) and (year % 100 == 1)
flag_year_1 = (year % 4 == 0) and (year % 100 != 0)
# 是否是世纪闰年
flag_year_2 = (year % 400 == 0)

# 结果输出
print("%d是闰年吗？" % year)
print('', flag_year_1 or flag_year_2)
