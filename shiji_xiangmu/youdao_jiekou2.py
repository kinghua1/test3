#coding=utf-8
#!/user/bin/python

from selenium import webdriver
#"在有道词典上输入框输入词语翻译"
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

#隐形等待时间10秒
sleep(6)
#在输入框输入内容‘hello’
driver.find_element_by_id('translateContent').send_keys('hello')

#提交输入框的内容
driver.find_element_by_id('translateContent').submit()

#隐形等待18秒
sleep(15)

driver.quit()

