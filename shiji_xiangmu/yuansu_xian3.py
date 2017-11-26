#!/user/bin/python
#coding=utf-8

#is_displayed()方法是否显示元素

#from selenium import webdriver
from time import sleep, ctime
from selenium import webdriver

print(ctime())

for i in range(10):
    try:
        el = driver.find_element_by_id('kw22')
        if el.is_displayed():
            break
    except:pass
    sleep(1)
else:
    print('time out')

#driver.close()
#driver.close()
print(ctime())
