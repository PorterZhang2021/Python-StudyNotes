from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

# 这个部分可能需要重新构建，可以换一个新的网站内容进行爬虫 b站现在爬取难度较大

# 浏览器
browser = webdriver.Chrome()
# 时间等待
WAIT = WebDriverWait(browser, 10)
# 设置大小
browser.set_window_size(1400, 900)

def search():
    try:
        print('开始访问b站...')
        browser.get('https://www.bilibili.com/')

        # 登录遮罩取出
        index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-searchform > nav-search-btn')))
        index.click()
    except TimeoutException:
        return search()


def main():
    search()

if __name__ == '__main__':
    main()

# 实现浏览器不自动关闭
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)