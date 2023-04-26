import requests

r = requests.get('https://ssr1.scrape.center/')
# 这里用内置判断码进行判断，如果成功就输出Request Successfully
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')