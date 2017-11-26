#coding=utf-8
#!/user/bin/python
from selenium import webdriver

#引入actionchains类
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com/')

#在搜索栏输入字符
driver.find_element_by_id('kw').send_keys('seleinum')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

sleep(4)

cookie_r = driver.get_cookies()
cookies_list =[]
for i in cookie_r:
    cookie = i['name'] + '=' + i['value']
    cookies_list.append(cookie)
cookies_str = ','.join(cookies_list)

print(cookies_str)

#通过link定位要双击的元素新闻
#right_lick = driver.find_element_by_link_text("新闻")


#对定位到的元素鼠标双击
#ActionChains(driver).context_click(right_lick).perform()
#print('wancheng')

#等待查看是否跳转成功
sleep(4)

driver.quit()