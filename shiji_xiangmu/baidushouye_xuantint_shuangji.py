#coding=utf-8
#!/user/bin/python

#百度首页悬停设置，点击高级搜索

from selenium import webdriver
#引进Actonchaoms类

from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#定位到元素‘设置’
above = driver.find_element_by_link_text("设置")
#对定位的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

#停留5秒
sleep(5)

#定位到子目录
zi_click = driver.find_element_by_link_text('高级搜索')
#执行双击操作
ActionChains(driver).double_click(zi_click).perform()

#停留20秒
sleep(20)

#关闭页面
driver.quit()

