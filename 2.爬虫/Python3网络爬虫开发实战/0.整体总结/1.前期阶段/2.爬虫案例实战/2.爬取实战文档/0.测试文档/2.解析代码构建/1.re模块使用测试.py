import os
import re
from urllib.request import urlopen

# 读取文件并以uft-8的形式返回
def read_files_as_str(filepath):
    # 判断路径文件存在
    if not os.path.exists(filepath):
        raise TypeError(filepath + 'does not exist')
    # 以
    with open(filepath, encoding='utf-8') as f:
        return f.read()

response = urlopen('https://ssr1.scrape.center/detail/1')
html_str = response.read().decode('utf-8')

name_pattern = re.compile('<h2.*?>(.*?)</h2>')
cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
drama_pattern = re.compile('drama.*?<p.*?>(.*?)</p></div>', re.S)
score_pattern = re.compile('score.*?>(.*?)</p>', re.S)

name = re.search(name_pattern, html_str).group(1)
cover = re.search(cover_pattern, html_str).group(1)
published = re.search(published_at, html_str).group(1)
categories = re.findall(categories_pattern, html_str)
drama = re.search(drama_pattern, html_str).group(1)
score = re.search(score_pattern, html_str).group(1)
print(name)
print(cover)
print(published)
print(categories)
print(drama.strip())
print(score.strip())

