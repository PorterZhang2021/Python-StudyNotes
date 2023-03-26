import requests

# 这里设置不验证证书
response = requests.get('https://ssr2.scrape.center/', verify=False)
# 输出状态码
print(response.status_code)