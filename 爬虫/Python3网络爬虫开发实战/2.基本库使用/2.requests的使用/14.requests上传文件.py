import requests

files = {
    'file': open(r'.\爬虫\Python3网络爬虫开发实战\2.基本库使用\res\favicon.ico', 'rb')
}
# 上传文件
r = requests.post('https://www.httpbin.org/post', files=files)
# 输出响应后信息
print(r.text)