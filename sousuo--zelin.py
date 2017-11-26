from selenium import webdriver
import time

#百度首页登录
browser = webdriver.Firefox()
baidu_url = "http://www.baidu.com"
browser.get(baidu_url)

time.sleep(3)

ele1 = browser.find_element_by_id("kw")
ele1.clear()
ele1.send_keys("泽林")

ele2 = browser.find_element_by_id("su")
ele2.click()

print(browser.current_url)

browser.close()
