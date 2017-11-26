#coding=utf-8
#!/user/bin/python

#隐形等待函数--NoSuchElementException

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep

dr4 = webdriver.Firefox()

#设置隐形等待
dr4.implicitly_wait(6)
dr4.get('http://www.baidu.com/')

print(ctime())
dr4.find_element_by_id('kw').send_keys('selenium')
sleep(4)

#except NoSuchElementException as e:
#    print(e)
#finally:

print(ctime())

dr4.quit()

