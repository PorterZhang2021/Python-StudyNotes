import requests
# 请求SSL证书错误的网站
response = requests.get('https://ssr2.scrape.center/')
# 请求响应后状态码
print(response.status_code)