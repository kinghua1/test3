#!/usr/bin/python
# coding=utf-8
__author__ = 'Administrator'

import unittest

# 定义测试用例的目录
test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)