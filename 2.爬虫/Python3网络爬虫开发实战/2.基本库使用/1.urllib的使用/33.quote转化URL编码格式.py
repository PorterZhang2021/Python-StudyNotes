from urllib.parse import quote

keyword = '壁纸'
# 利用quote转换编码将其变成url编码格式
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# 输出编码后的url
print(url)