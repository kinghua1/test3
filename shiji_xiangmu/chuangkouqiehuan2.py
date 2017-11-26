#/user/bin/python
#coding=utf-8

# 多窗口切换
from selenium import  webdriver
import time

#启动浏览器
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#获得百度搜索窗口
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.windows(handle)
        print('now register windows!')
        driver.find_element_by_name("account").send_keys('小李子子子')
        driver.find_element_by_name("password").send_keys('bcde550')
        time.sleep(4)

#回到搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.windows(handle)
        print('now sreach windows!')
        driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time(3)

driver.quit()
