""" 
获取当当网TOP500
"""
# 导入包
import requests
import re
import json




def request_dandan(url):
    """
    拿到网站的源码
    """
    # 异常处理
    try:
        # 利用requests库分析出响应
        response = requests.get(url)
        # 如果响应状态正确
        if response.status_code == 200:
            # 返回响应的文本
            return response.text
    except requests.RequestException:
        # 如果响应错误则为None
        return None




def parse_result(html):
    """
    进行相关的解析
    """

    # 正则匹配式 这里的正则表达式需要自己分析一下
    # 这里的正则匹配式需要理解一下
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    # 获取元素 利用正则匹配式获取元素
    items = re.findall(pattern, html)
    for item in items:
        # 这里是生成式函数
        yield {
            # 排名
            'range': item[0],
            # 图片地址
            'image': item[1],
            # 书名
            'title': item[2],
            # 推荐
            'recommend': item[3],
            # 作者
            'author': item[4],
            # 五星评分次数
            'times': item[5],
            # 价格
            'price': item[6]
        }

def write_item_to_file(item):
    # 写入数据
    print('开始写入数据 ===>' + str(item))
    with open('C:\\Users\\LENOVO\\Desktop\\book.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()

def main(page):
    # 请求链接 这里的请求链接是网页会发生变化
    # 这里的请求使用的是http模式 而 https模式可能会有强加密
    url = 'http://bang.dangdang.com/books/fivestars/1-' + str(page)
    # 获取的html网页
    html = request_dandan(url)
    # 解析过滤我们想要的信息
    items = parse_result(html)

    # 获取信息
    for item in items:
        # print(item)
        # 将信息写入文件
        write_item_to_file(item)


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
