""" 
获取当当网TOP500
"""
# 导入包
import requests
import re

# 拿到html的源代码
def request_dandan(url):
    # 异常处理
    try:
        # 返回响应
        response = requests.get(url)
        # 如果响应状态正确
        if response.status_code == 200:
            # 返回响应的文本
            return response.text
    except requests.RequestException:
        return None

# 进行解析
def parse_result(html):
    # 正则匹配式
    pattern = re.complie(r'<li>.*?list_num.*?(d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    # 获取元素
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }
        
def main(page):
    # 请求链接
    url = 'https://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    # 获取的html网页
    html = request_dandan(url)
    # 解析过滤我们想要的信息
    items = parse_result(html)

    # 获取信息
    for item in items:
        # 将信息写入文件
        write_item_to_file(item)