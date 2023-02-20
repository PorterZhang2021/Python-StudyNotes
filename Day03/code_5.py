"""

百分制成绩转换为等级制成绩

"""

num = int(input('请输入你的成绩:'))

if num >= 90:
    print('恭喜你获得了A,继续保持哦')
elif num >= 80:
    print('恭喜你获得了B，还不赖嘛')
elif num >= 70:
    print('你获得了C，要努力啊')
elif num >= 60:
    print('你获得了D，要加油了')
else:
    print('E，最近的你要好好学习了')