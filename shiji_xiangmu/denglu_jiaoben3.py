#!/user/bin/python
#coding=utf-8

##! /usr/bin/python
# coding=utf-8

from selenium import webdriver
import time
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
ele = browser.find_element_by_link_text('登录')
ele.click()

ele1 = browser.find_element_by_xpath('.//*[@id="TANGRAM__PSP_8__userName"]')
ele1.clear()

ele1.send_keys('xiaojinjin金华')

ele2 = browser.find_element_by_xpath('.//*[@id="TANGRAM__PSP_8__password"]')
ele2.clear()
ele2.send_keys('xiaojinjin')

time.sleep(2)
ele3 =browser.find_element_by_class_name('buttons')
ele3.click()

browser.close()