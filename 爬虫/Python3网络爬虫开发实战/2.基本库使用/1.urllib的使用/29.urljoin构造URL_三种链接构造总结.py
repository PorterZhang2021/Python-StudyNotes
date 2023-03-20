# 三种构成链接合并的方法
# urlunparase(), urlunsplit(), urljoin()
# 其中前两个是需要清晰分开各个部分 urlunparase()需要params参数而urlunsplit()构建不需要params参数
# urljoin则是base_url基础链接和新链接合并

from urllib.parse import urljoin

# 两个链接进行拼接
print(urljoin('https://www.baidu.com', 'FAQ.html'))
# https://www.baidu.com/FAQ.html
# 拼接链接 如果链接有shceme,netloc和path使用新连链接
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# https://cuiqingcai.com/FAQ.html?question=2
print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# https://cuiqingcai.com/index.php
print(urljoin('https://www.baidu.com', '?category=2#comment'))
# https://www.baidu.com?category=2#comment
print(urljoin('www.baidu.com', '?category=2#comment'))
# www.baidu.com?category=2#comment
print(urljoin('www.baidu.com#comment', '?category=2'))
# www.baidu.com?category=2 这里拼接的时候将锚点部分去除了因为其拼接是按顺序的，有前置的顺序，那么后置的内容就删除了
# scheme://netloc/path;params?query#fragments