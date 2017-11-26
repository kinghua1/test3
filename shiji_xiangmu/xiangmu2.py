#coding=utf-8
#!/user/bin/python
#登录易造机器人


from selenium import webdriver

webdriver =webdriver.Firefox()
webdriver.get("http://www.ez-robot.cn/account/login")

webdriver.find_element_by_id("username").clear()
webdriver.find_element_by_id("username").send_keys("iking12@126.com")
webdriver.find_element_by_id("password").clear()
webdriver.find_element_by_id("password").send_keys("abcd150")

#webdriver.find_element_by_id("loginBth").click()

webdriver.find_element_by_name("form-item form-item-submit")




webdriver.quit()