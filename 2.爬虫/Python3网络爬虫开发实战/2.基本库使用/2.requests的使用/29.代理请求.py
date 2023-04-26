import requests

# 代理
# 这里代理服务器，会出现ProxyError 且 和之前的百度代理请求访问一样，会出现链接失败或者拒绝访问的情况
proxies = {
    'http': 'http://59.58.80.79:4780',
    'https': 'https://59.58.80.79:4780',
}

# 伪装头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 我用代理的时候会触发SSL证书验证的异常 这是什么原因呢？- 在Stackoverflow也没找到相关的解决方案，后期试试看
# 这里关闭证书验证 
requests.get('https://www.httpbin.org/get', proxies=proxies, headers=headers, verify=False)