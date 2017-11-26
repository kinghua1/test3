#coding=utf-8
#!/user/bin/python
from selenium import webdriver
from time import sleep

webdriver = webdriver.Firefox()
webdriver.get("http://www.baidu.com")

#参数数字为像素点
print("设置浏览器宽480，高800显示")
webdriver.get_window_size(480,800)
webdriver.refresh()
webdriver.quit()

sleep(4)

webdriver.quit()