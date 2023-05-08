import time
import re
import tesserocr

from selenium import webdriver
from io import BytesIO
from PIL import Image
from retrying import retry

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import numpy as np

def preprocess(image):
    # 图片类型转换
    image = image.convert('L')
    # 数组化
    arry = np.array(image)
    # 阈值判定与转化
    arry = np.where(arry > 55, 255, 0)
    # 重新获取转化后的图像
    image = Image.fromarray(arry.astype('uint8'))
    # 返回转化后的图像
    return image

# 登录操作
# 这里的装饰头指定了尝试次数 错误就继续尝试
@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    # 进入网页
    browser.get('https://captcha7.scrape.center/')
    # 获取对应元素填入值
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    # 获取验证码
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 获取验证码
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    captcha_no_preprocess = tesserocr.image_to_text(image)
    # 验证码处理
    image = preprocess(image)
    # 文本字符转换
    captcha_preprocess = tesserocr.image_to_text(image)
    if not captcha_preprocess:
        captcha = re.sub('[^A-Za-z0-9]', '', captcha_no_preprocess)
    else :
        # 剔除多余内容
        captcha = re.sub('[^A-Za-z0-9]', '', captcha_preprocess)
    print(captcha)
    # 输入验证码
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)
    # 点击登录
    browser.find_element(By.CSS_SELECTOR, '.login').click()
    try:
        # 验证登录成功
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        # 没有就等10分钟
        time.sleep(10)
        # 关闭浏览器
        browser.close()
        return True
    except TimeoutException:
        # 超时返回False
        return False



if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()