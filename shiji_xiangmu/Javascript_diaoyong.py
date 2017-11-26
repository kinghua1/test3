#coding=utf-8
#!/user/bin/python

#调用JavaScript控制页面
from selenium import webdriver
from time import sleep

#访问百度
driver =webdriver.Firefox()
driver.get('https://www.baidu.com')

#设置浏览器大小
#driver.set_window_size(600,600)
driver.maximize_window()
sleep(2)

#截取当前的窗口，并制定截图图片的保存位置
driver.get_screenshot_as_file("H:\\python3.5\\baidu_tu2.jpg")



#搜索

#driver.find_elements_by_id("kw")  #.send_keys("selenium")
#driver.find_elements_by_id("su") #.click()

#通过滚动条JavaScript设置浏览器的窗口的滚动条的位置
#js="window.scrollto(100,450);"
#driver.execute_script(js)
#sleep(4)

driver.quit()