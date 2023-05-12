import json
from urllib.request import urlopen


url = 'https://spa1.scrape.center/api/movie/1/'

response = urlopen(url)

# 获取请求得到的信息
#print(response.read().decode('utf-8'))
response_text = response.read()
# print(type(response_text))
response_dict = json.loads(response_text)
# print(type(response_dict))
print(response_dict)
name = response_dict['name']
print(name)
cover = response_dict['cover']
print(cover)
categories = response_dict['categories']
print(categories)
score = response_dict['score']
print(score)
published_at = response_dict['published_at']
print(published_at)
drama = response_dict['drama']
print(drama)
# 获取我们需要的信息
# response_result = response_dict['results']
