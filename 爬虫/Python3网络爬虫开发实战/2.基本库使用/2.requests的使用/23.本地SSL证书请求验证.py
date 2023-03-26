import requests

# 这里是指定本地证书用作客户端证书，后面两个是文件信息，此方式没有验证
response = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', '/path/server.key'))
print(response.status_code)