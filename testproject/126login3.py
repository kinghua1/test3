#coding=utf-8
#!/user/bin/python
#易造机器人网登录模块，登录。(126邮箱登录)

from selenium import webdriver
from time import sleep

webdriver =webdriver.Firefox()
webdriver.get("http://www.ez-robot.cn/account/login")

webdriver.find_element_by_id("username").clear()
webdriver.find_element_by_id("username").send_keys("898792093@qq.com")
webdriver.find_element_by_id("password").clear()
webdriver.find_element_by_id("password").send_keys("b23456")
webdriver.find_element_by_id("loginBtn").click()

sleep(10)
webdriver.quit()

import sys
r
sys.
