# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: Base.py
@time: 2023/9/27 15:02

"""
from selenium import webdriver


class BaseConf:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(sef):
        sef.driver.quit()
