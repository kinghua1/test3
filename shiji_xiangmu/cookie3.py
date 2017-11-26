#-*- coding: UTF-8 -*-


#通过get_cookies获取cookie信息
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.foxsaas.com')

#cookis= driver.get_cookies()

driver.add_cookie({'name': 'key-aaaaaaa', 'value':'value-bbbbb'})
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']) )

driver.quit()