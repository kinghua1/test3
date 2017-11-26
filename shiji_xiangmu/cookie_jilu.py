#/user/bin/python
#coding=utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.ez-robot.cn/account/login')

#将用户名，密码注入cookie中
driver.add_cookie({'name':'Login_UserNumber','value':'iking12@126.com'})
driver.add_cookie({'name','value':'abcd150'})

#再次访问一次网站，查看是否会自动登录
driver.get('http://www.ez-robot.cn/account/login')

sleep(7)
driver.quit()


