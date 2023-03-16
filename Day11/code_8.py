import requests
import json


def main():
    # 此地方应该有问题
    resp = requests.get(
        'https://apis.tianapi.com/toutiaohot/index')
    data_model = json.load(resp.text)
    for news in data_model['newlist']:
        print(news['title'])


if __name__ == '__main__':
    main()
