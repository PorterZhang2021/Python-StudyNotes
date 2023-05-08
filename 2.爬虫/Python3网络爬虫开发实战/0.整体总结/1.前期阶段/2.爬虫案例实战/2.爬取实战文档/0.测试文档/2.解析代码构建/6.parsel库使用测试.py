import requests

from parsel import Selector

url = 'https://ssr1.scrape.center/detail/1'

response = requests.get(url=url)

html = response.text

selector = Selector(text=html)

name = selector.xpath('//h2[@class="m-b-sm"]/text()').get()
print(name)

cover = selector.css('img.cover::attr(src)').get()
print(cover)

categories = selector.xpath('//button[contains(@class,"category")]/span/text()').getall()
print(categories)

drama = selector.xpath('//div[@class="drama"]/p/text()').get().strip()
print(drama)

published = None

score = selector.xpath('//p[contains(@class, "score")]/text()').get().strip()
print(score)

