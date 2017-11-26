#! /usr/bin/python
# coding=utf-8

__author__ = 'fjxz12321sjff'

from selenium import webdriver
from time import sleep

#反问百度首页
brs = webdriver.Firefox()
brs.get('https://www.baidu.com')

#窗口最大化
brs.maximize_window()
sleep(2)

#搜索selenium
brs.find_element_by_id('kw').send_keys('selenum')
brs.find_element_by_id('su').click()

#设置浏览器的显示窗口
brs.set_window_size(600, 600)
sleep(3)
#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(200,450);"
brs.execute_script(js)
sleep(3)

print(__author__)
brs.quit()