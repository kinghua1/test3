#! /usr/bin/python
# coding=utf-8
__author__ = 'Administrator'

from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        bsr = self.driver
        bsr.get(self.base_url + "/")
        bsr.find_element_by_id("translateContent").clear()
        bsr.find_element_by_id("translateContent").send_keys("webdriver")

        bsr.find_element_by_link_text("翻译").click()
        time.sleep(2)
        title = bsr.title
        print(title)

        self.assertEqual(title, "webdriver - 有道搜索", msg="网址标题有误！")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()