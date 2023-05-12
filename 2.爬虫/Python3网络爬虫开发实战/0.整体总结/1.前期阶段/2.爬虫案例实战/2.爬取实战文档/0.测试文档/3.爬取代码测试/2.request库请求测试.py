import requests

response = requests.get('https://spa1.scrape.center/api/movie/19')
# 获取到整体的结果
response_result = response.json()
print(response_result)

 # 电影标题获取
name = response_result.get('name', None)
print(name)
# 电影图片url获取
cover = response_result.get('cover', None)
print(cover)
# 电影上映时间获取
published_at = response_result.get('published_at', None)
print(published_at)
# 电影分类内容获取
categories = response_result.get('categories', [])
print(categories)
# 电影评分获取
score = response_result.get('score', None)
print(score)
# 电影剧情简介
drama = response_result.get('drama', None)
print(drama)