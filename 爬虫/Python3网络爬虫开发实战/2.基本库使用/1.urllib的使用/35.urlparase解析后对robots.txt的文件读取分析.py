from urllib.request import urlopen
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
# 爬虫文件 获取打开的文件进行解析分析 这里打卡开后要转码成utf-8的形式，并且去除斜杠 -> 实例部分可以更新成此方式
rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))