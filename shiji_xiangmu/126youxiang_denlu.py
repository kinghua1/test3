#coding=utf-8
#!/user/bin/python

#登录126邮箱，通过简单的操作

from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("http://mail.126.com/")

driver.find_element_by_id()