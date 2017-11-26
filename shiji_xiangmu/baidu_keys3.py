#conding=utf-8
#!/user/bin/python

#练习键盘事件

from selenium import webdriver
from time import sleep

#引入keys模块
from selenium.webdriver.common.keys import Keys

dr2 = webdriver.Firefox()
dr2.get('http://www.baidu.com')

#设置浏览器大小
dr2.maximize_window()

#输入框输入内容
dr2.find_element_by_id('kw').send_keys('seleniumm')
sleep(6)

#删除输入的m
dr2.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
sleep(6)

#输入空格键+‘教程’
dr2.find_element_by_id('kw').send_keys(Keys.SPACE)
dr2.find_element_by_id('kw').send_keys('教程')
sleep(6)

#ctrl+a 全选输入框的内容
dr2.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(6)

#ctrl+x 剪切输入框的内容
dr2.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(4)

#ctrl +v 复制内容到输入框
dr2.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
dr2.find_element_by_id('kw').send_keys('python')
sleep(5)

#通过回车代替点击操作
dr2.find_element_by_id('kw').send_keys(Keys.CONTROL)
sleep(5)

dr2.quit()

