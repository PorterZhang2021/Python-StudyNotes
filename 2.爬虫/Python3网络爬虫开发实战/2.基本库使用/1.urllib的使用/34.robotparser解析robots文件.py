from urllib.robotparser import RobotFileParser

# 爬虫文件解析对象
rp = RobotFileParser()
# 设置解析的文件地址
rp.set_url('https://www.baidu.com/robots.txt')
# 读取robots.txt文件
rp.read()
# User-Agent 以及 抓取URL
# 判断此网页是否可以被抓取
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
# 谷歌爬虫不能抓取homepage页面
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))