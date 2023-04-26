from urllib.parse import urlencode

# 参数 以字典形式存放
params = {
    'name': 'germey',
    'age': 25
}

# 基础链接
base_url = 'https://www.baidu.com?'
# 进行链接的构造
url = base_url + urlencode(params)
# 输出构造好的GET链接
print(url)