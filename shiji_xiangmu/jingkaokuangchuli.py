#coding=utf-8
#!/user/bin/python

#警告框处理
from selenium import  webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time

jing = webdriver.Firefox()
jing.implicitly_wait(9)
jing.get('http://www.baidu.com')

#鼠标悬停至‘设置’连接
link = jing.find_element_by_link_text('设置')
ActionChains(jing).move_to_element(link).perform()

#打开搜索设置
jing.find_element_by_link_text('搜索设置').click()

#保存设置
jing.find_elements_by_class_name('prefpanelgo')

rightdian =jing.find_elements_by_name('prefpanelgo')
ActionChains(jing).context_click(rightdian).perform()
time.sleep(3)

#接受警告框
jing.switch_to_alert().accept()

time.sleep(3)

jing.quit()