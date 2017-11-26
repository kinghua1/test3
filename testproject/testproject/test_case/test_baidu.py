#! /usr/bin/python
# coding=utf-8
__author__ = 'Administrator'

from selenium import webdriver
import time
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.baidu.com"

    def test_baidu(self):
        bsr = self.driver
        bsr.get(self.base_url + "/")
        bsr.find_element_by_id("kw").clear()
        bsr.find_element_by_id("kw").send_keys("unittest")
        bsr.find_element_by_id("su").click()

        time.sleep(2)
        title = bsr.title
        print(title)
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()