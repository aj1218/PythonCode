# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: test_data_record.py
@time: 2023/9/28 10:48

"""
from selenium.webdriver.common.by import By

from ALL_Test_code.Base import BaseConf
from ALL_Test_code.log_utils import logger


class TestDataRecord(BaseConf):
    def test_log_data_record(self):
        # 进入搜狗首页
        search_content = "霍格沃兹测试开发学社"
        self.driver.get("https://www.sogou.com/")
        # 输入霍格沃兹测试开发，进行搜索操作
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, "stb").click()
        # 获取搜索结果(对应测试用例的实际结果)
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"实际结果为:{search_res.text},预期结果为:{search_content}")
        assert search_res.text == search_content

    def test_log_data_screeshot(self):
        # 截图
        # 进入搜狗首页
        search_content = "霍格沃兹测试开发学社"
        self.driver.get("https://www.sogou.com/")
        # 输入霍格沃兹测试开发，进行搜索操作
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, "stb").click()
        # 获取搜索结果(对应测试用例的实际结果)
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"实际结果为:{search_res.text},预期结果为:{search_content}")
        # 截图记录
        self.driver.save_screenshot("res.png")
        assert search_res.text == search_content

    def test_page_source_data(self):
        # ctrl + alt + L  格式化html文件
        # 现象:产生了 no such element 的错误
        # 解决方案: 在报错的代码行之前打印page_source，确认定位的元素没有问题
        search_content = "霍格沃兹测试开发学社"
        self.driver.get("https://www.sogou.com/")
        with open("record3.html","w",encoding="u8") as f:
            f.write(self.driver.page_source)
        # 输入霍格沃兹测试开发，进行搜索操作
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        # 获取page_source
        logger.debug(self.driver.page_source)



