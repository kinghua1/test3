#coding=utf-8
#!/user/bin/python

#现行等待，是否确定元素加载完成

from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

element =WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID,'kw'))
)
#element.send_kys('selenium')
driver.find_element_by_id('kw').send_keys('自动化测试')


#driver.find_element_by_id('kw').send_keys(Keys.ENTER)
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(3)

driver.quit()