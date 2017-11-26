#conding=utf-8

#-*- coding: UTF-8 -*-


#通过get_cookies获取cookie信息
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.ez-robot.cn/account/login')

#获取cookie信息
cookie = driver.get_cookies()
print(cookie)

sleep(7)
driver.quit()