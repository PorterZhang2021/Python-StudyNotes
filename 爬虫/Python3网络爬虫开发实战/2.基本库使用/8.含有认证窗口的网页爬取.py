from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# 用户名
username = 'admin'
# 密码
password = 'admin'
# 链接网站
url = 'https://ssr3.scrape.center/'

# 构建基本身份认证
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

# 异常捕获语句
try:
    # 结果 利用身份认证后用户打开网页
    result = opener.open(url)
    # 获取到网页信息
    html = result.read().decode('utf-8')
    # 输出网页信息
    print(html)
except URLError as e:
    print(e.reason)