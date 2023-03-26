import requests
import re

# 构建指定索引规律下的页面，并抓取保存其对象
def get_url_to_response(url, start, end, step):
    """
    url: 具有规律性的链接
    start: 起始数字
    end: 终止数字
    step: 增加的步进

    return list: 返回抓取到页面的响应
    """
    # 返回类型为一个列表
    response_list = []
    # 抓取页面
    for i in range(start, end, step):
        # 组合url
        get_url = url + '/page/' + str(i)
        # 这里进行一个请求的判断
        try:
            # 进行请求
            response = requests.get(get_url)
            # 如果请求状态为200存入
            if response.status_code == 200:
                response_list.append(response)
        except requests.RequestException:
            # 输出错误
            print('请求出错')
    return response_list

# 抓取每页中所需要的详情并构建合适的页面
def scrape_link(url, response, pattern):
    """
    url: 具有规则超链接
    response: 响应请求
    pattern: 正则表达式

    return list: 组合成功后的超链接
    """
    # 要抓取的页面
    text = response.text
    # 超链接
    link_list = re.findall(pattern, text)
    # 进行循环
    for i in range(len(link_list)):
        # 组合url
        organize_url = url + link_list[i]
        # 链接列表
        link_list[i] = organize_url
    return link_list


def main():
    # 超链接
    url = 'https://ssr1.scrape.center'
    # 抓取响应后的页面
    response_list = get_url_to_response(url, 1, 11, 1)
    print(response_list)
    # 正则表达式
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    # 获取一页的链接
    # 获取所有的超链接
    all_link_list = []
    for response in response_list:
        # 获取一页的组合链接
        link_list = scrape_link(url, response, pattern)
        for link in link_list:
            # 存入链接
            all_link_list.append(link)
    
    print(all_link_list)

if __name__ == '__main__':
    main()


