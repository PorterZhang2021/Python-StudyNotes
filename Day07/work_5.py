"""
计算指定的年月日是这一年的第几天
年：
先判断是闰年还是平年
月：
闰年：366 29
平年：365 28
日：
直接加
"""


def getDays(times):
    # 年份产生的影响主要是对2月起作用
    # 字符截取 0:4
    year = int(times[0:4])
    # 字符截取 4:6
    month = int(times[4:6])
    # 字符截取 6:8
    day = int(times[6:])
    # 记录天数
    days = 0
    # 月份需要进行打表
    months = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

    # 判定闰年
    if (year % 4 == 0 and year % 100 != 0) or \
            (year % 400 == 0):
        # 当闰年的时候改变2月的表
        months[1] = 29
    else:
        months[1] = 28
    # 前面的月份按顺序进行累加
    for i in range(month - 1):
        days += months[i]
    # 最后一个月直接将日加上
    days += day

    # 返回天数
    return days


print(getDays('19990722'))
