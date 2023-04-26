from urllib.parse import urlunsplit

# 构造URL这种方式少了params参数
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# 输出构造的URL
print(urlunsplit(data))