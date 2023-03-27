import requests
import logging
import re
from urllib.parse import urljoin

# logging用于进行日志输出
# 这里定义了日志输出级别和输出格式
# 这里的输出格式 因为多加了一个% 导致出现了错误
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# def scrape_page(url):
#     """
#     页面爬取方法，因为我们要爬取列表页还要爬取详情页，所以定义了一个比较通用的爬取页面方法
#     url: 要爬取的链接
#     return string: 返回一个页面信息以字符串的形式返回
#     """
#     # 这里的是输出信息，输出的是爬取的网页链接
#     logging.info('scraping %s...', url)
#     # 异常捕获操作
#     try:
#         # 获取请求响应
#         response = requests.get(url)
#         # 如果状态码正确
#         if response.status_code == 200:
#             # 输出响应后的页面即抓取到的页面
#             return response.text
#         # 这里的请求日志 说明如果输出的是其他情况下的响应 返回一个日志报错
#         logging.error('get invalid status code %s while scraping %s',
#                       response.status_code, url)
#     # 这里出现请求的异常
#     except requests.RequestException:
#         # 这里的错误日志 是当请求异常时，返回出请求异常的信息
#         logging.error('error ocurred while scraping %s', url,
#                       exc_info=True)

# 爬取详情页
# base_url = 'https://ssr1.scrape.center/detail/1'

# def main():
#     # 爬取一个详情页 - 这部分可以作为一个函数
#     detail_html = scrape_page(base_url)

#     # 正则表达式的构建原则为由小到大,处理复杂程度
#     # 正则表达式的构建要随时注意，可能需要加换行，
#     # 如果得到了匹配对象看不到所有的结果，那么就验证你所需要分组
#     # 看看其结果是否能够取出
#     # 构建图片的正则表达式
#     img_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
#     # 构建名称的正则表达式
#     title_pattern = re.compile('<h2.*?>(.*?)</h2>')
#     # 构建类别的正则表达式
#     categories_pattern = re.compile('category.*?<span>(.*?)</span>', re.S)
#     # 构架上映时间的正则表达式
#     time_pattern = re.compile('<span.*?>(\d{4}-\d{2}-\d{2}) 上映</span>')
#     # 构建评分的正则表达式
#     score_pattern = re.compile('<p.*?class="score.*?">(.*?)</p>', re.S)
#     # 构建剧情简介表达式
#     description_pattern = re.compile('class="drama".*?<p.*?>(.*?)</p>', re.S)

#     # 进行解析获取验证
#     # 验证图片是否能够解析获取到
#     img_match = re.search(pattern=img_pattern, string=detail_html)
#     # 获取到图片的url
#     img= img_match.group(1)

#     # 验证名称是否能够获取到
#     title_match = re.search(pattern=title_pattern, string=detail_html)
#     # 获取所需要的标题
#     title = title_match.group(1)

#     # 验证所需要的类别是否能够获取到
#     categories_match = re.findall(pattern=categories_pattern, string=detail_html)
#     categories_list = categories_match

#     # 验证上映时间是否能够获取到
#     time_match = re.search(pattern=time_pattern, string=detail_html)
#     time = time_match.group(1)

#     # 验证评分表达式是否能够获取
#     score_match = re.search(pattern=score_pattern, string=detail_html)
#     score = float(score_match.group(1))

#     # 验证剧情简介的表达式
#     description_match = re.search(pattern=description_pattern, string=detail_html)
#     # 获取字符串后对字符串进行处理
#     need_handle_description = description_match.group(1)
#     # 这里的操作是截掉左边会出现的空格
#     description = need_handle_description.lstrip()


def main():
    word = """第一次世界大战期间，回国度假的陆军中尉罗伊（罗伯特·泰勒 饰）在滑铁卢桥上邂逅了舞蹈演员玛拉（费雯·丽 饰），两人彼此倾心，爱情迅速升温。就在两人决定结婚之时，罗伊应招回营地，两人被迫分离。由于错过剧团演出，玛拉被开除，只能和好友相依为命。不久玛拉得知罗伊阵亡的消息，几欲崩溃，备受打击。失去爱情的玛拉感到一切都失去了意义，为了生存，她和好友不得不沦为妓女。然而命运弄人，就在此时玛拉竟然再次遇到了罗伊。虽然为罗伊的生还兴奋不已，玛拉却因自己的失身陷入痛苦之中。感到一切难以挽回的玛拉潸然离开，独自来到两人最初相遇的地点——滑铁卢桥上…\n                """
    print(word)


if __name__ == '__main__':
    main()
