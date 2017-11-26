#conding=utf-8
#/user/bin/python
from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys


liu2 = webdriver.Firefox()
liu2.get('http://www.ez-robot.cn/account/login')

liu2.find_elements_by_id("username").send_keys('')

#利用元素属性定位
liu2.find_elements_by_xpath("//input[@id='kw']").clear()
liu2.find_elements_by_xpath("//input[@id='kw']").send_keys("python")

#liu2.find_elements_by_xpath("//input[@id='']").clear()
liu2.find_elements_by_xpath("//input[@id='su']").click()

sleep(3)
liu2.quit()