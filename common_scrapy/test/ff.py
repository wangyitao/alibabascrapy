# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/4/21 22:56

# 创建chrome参数对象
from selenium import webdriver

opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.set_headless()
# 创建chrome无界面对象
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# browser = webdriver.PhantomJS()
browser.set_window_size(1366, 768)



browser.get('http://www.taobao.com')

try:
    browser.implicitly_wait(30)  # 隐性等待，最长等30秒
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # time.sleep(3)
    locator = (By.CSS_SELECTOR, '#dg-item-tl-0')
    WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(locator))

except:
    print('timeout')

with open('taobao33.html', 'w', encoding='utf8') as f:
    f.write(browser.page_source)
