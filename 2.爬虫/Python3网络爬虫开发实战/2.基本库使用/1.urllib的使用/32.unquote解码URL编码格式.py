from urllib.parse import unquote

# 编码格式后的url
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))