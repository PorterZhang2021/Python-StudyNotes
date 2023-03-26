"""
爬取目标为一个列表类型的网站
点击进去之后有详细信息
1. 爬取其列表信息的情况
找到每个列表的特征 - 其特征是每个列表卡片由一个div包裹

找到进入链接查看详细信息的特征 - 其特征是在一个div内，这个div中有个h2显示标题，
另一个a标签中显示链接信息

查看翻页的逻辑 - 我们看到翻页的逻辑是网址出现 /page/number number为一个变量的更改

任务1. 爬取所有页码 构造出10页的索引页URL
任务2. 从每个索引页，分析提取出每个电影详情页URL
"""
# request库实现方法
import requests
import re

# 任务1.爬取所有页面，构造出10页的索引页
# 先构造出索引页的形式 由于/page/1也是可以得到的 那么形式如下
# 先构造URL
url = 'https://ssr1.scrape.center/page/'

response_list = []

# 构建出10个索引页的url
for i in range(1, 11):
    # 可以重新更改为抓取
    # print(url + str(i))
    # 进行抓取操作
    req= requests.get(url+str(i))
    # 将抓取的对象保存
    response_list.append(req)

# 输出抓取到的对象
# print(response_list)

# 实现提取出一个页面中的一个
# 需要利用到正则表达式 引入正则表达式
# 去工具分析一下
# 构建一个正则表达式匹配对象
# 这里的正则表达式 构建为什么是这样呢 我在构建其他正则表达式的时候总是会出错
"""这里出错的原因是我自己多考虑了一个问题，加了re.S，其实这个部分并不需要考虑到换行的情况，都是在一行中"""
pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
# 构建list
movie_link_list = []

# 分析提取到详情页
# 先实现提取出一个页面的
# 多页面情况实现
# print(page.text)
for page in response_list:
    a_content_list = re.findall(pattern, page.text)
    movie_link_list += a_content_list

# 将其构建成合适的链接
for i in range(len(movie_link_list)):
    link = 'https://ssr1.scrape.center' + movie_link_list[i]
    movie_link_list[i] = link


