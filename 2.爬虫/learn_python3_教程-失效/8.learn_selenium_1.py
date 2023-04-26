# selenium4有了新的特性 因此这里需要利用By
# web驱动模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 创建一个Chrome驱动
driver = webdriver.Chrome()
# 利用get方法打开百度
driver.get('https://www.baidu.com')

# selenium4新特性
# 写入搜索内容
input = driver.find_element(By.ID, 'kw')
input.send_keys('苍老师照片')

# 按钮点击
button = driver.find_element(By.ID, 'su')
button.click()
 
# selenium4新特性 单个元素获取
# find_element(By.ID)
# find_element(By.NAME)
# find_element(By.XPATH)
# find_element(By.LINK_TEXT)
# find_element(By.PARTIAL_LINK_TEXT)
# find_element(By.TAG_NAME)
# find_element(By.CLASS_NAME)
# find_element(By.CSS_SELECTOR)

# 多个元素获取
# find_elements(By.NAME)
# find_elements(By.XPATH)
# find_elements(By.LINK_TEXT)
# find_elements(By.PARTIAL_LINK_TEXT)
# find_elements(By.TAG_NAME)
# find_elements(By.CLASS_NAME)
# find_elements(By.CSS_SELECTOR)

html_doc = """
<html>
    <body>
        <form id="loginForm">
            <input name="username" type="text" />
            <input name="password" type="password" />
            <input class="login" name="continue" type="submit" value="Login" />
        </form>
    </body>
<html>
"""

# 通过id获取form表单
login_form = driver.find_element(By.ID, 'loginForm')
# 通过name获取相应的输入框
username = driver.find_element(By.NAME, 'username')
# 通过xpath获取表单
password = driver.find_element(By.NAME, 'password')
# 通过标签获取相应的输入框
input1 = driver.find_element(By.TAG_NAME, 'input')
# 通过class获取相应元素
logini = driver.find_element(By.CLASS_NAME, 'login')
# 如果要找相关的元素
# 直接利用Chorme浏览器审核元素，方便快捷获取相应的属性

# 获取请求连接
driver.current_url
# 获取cookies
driver.get_cookies()
# 获取源代码
driver.page_source
# 获取文本的值
input.text


