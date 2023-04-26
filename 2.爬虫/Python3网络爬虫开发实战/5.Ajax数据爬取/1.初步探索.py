import requests

proxies = {
    # 此部分在v2rayN代理中找到系统代理部分找到对应端口
	'http': '127.0.0.1:10809',
	'https': '127.0.0.1:10809'
}


url = 'https://spa1.scrape.center/'
html = requests.get(url, proxies=proxies).text
print(html)