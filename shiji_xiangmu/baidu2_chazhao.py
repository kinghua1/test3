#coding=utf-8
#!/user/bin/python

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

#返回百度页面底部的备案信息
text = driver.find_element_by_id('cp').text
print(text)

#返回元素的属性值，可以是ID，name，type或者其他属性的信息
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#返回结果是否可见，返回结果是TRUE或false
result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()