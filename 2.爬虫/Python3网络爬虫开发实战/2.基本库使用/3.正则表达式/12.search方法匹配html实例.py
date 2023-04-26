import re

# html文本
html = '''<div id="song-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一生笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
<div>'''

# 匹配第三个li结点下a结点的singer属性和文本
# result = re.search('<li.*?active.*?singer="(*.?)"(.*?)</li>', html)
# 这个报错，修饰符没有加，因此没有办法匹配带有换行符的文本

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, flags=re.S)
# 输出找到的匹配文本 这里输出的匹配是最先找到的一个贪婪匹配
print(result)
# 如果有这个匹配的结果，那么就输出
if result:
    # 这里很神奇，按道理匹配的正则表达式对象并不是这个结果，但它可以多次匹配得到需要的情况
    print(result.group(1), result.group(2))
