#！/user/bin/python
#coding=utf-8

#！/user/bin/python
#coding=utf-8

from selenium import webdriver
import os,time
from time import sleep

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('check5.html')
driver.get(file_path)

#页面选择所有的tag name为input元素
input2 = driver.find_element_by_tag_name('input')

#然后在从中能过滤苏type为checkbox的元素，单击勾选
for i in input2:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        time.sleep(2)

driver.quit()






