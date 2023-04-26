from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    # 打开的页面
    browser.get('https://www.baidu.com')
    # 查找元素
    input = browser.find_element(by=By.ID,value='kw')
    # 发送关键字
    input.send_keys('Python')
    # 进行查询
    input.send_keys(Keys.ENTER)
    # 等待操作
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    # 获取连接
    print(browser.current_url)
    # 获取cookies
    print(browser.get_cookies())
    # 获取页面资源
    print(browser.page_source)
finally:
    browser.close()
