# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: test_contact.py
@time: 2023/10/9 17:18

"""
from selenium.webdriver.common.by import By

from Web_python_code.Web_practice.pracetice.utils.base import BaseConfig


class TestAddMember(BaseConfig):
    def test_addmember(self):
        # Faker随机生成  改为中文:fake = Faker("zh-CN")
        name = self.fake.name()
        accid = self.fake.ssn()
        phonenum = self.fake.phone_number()
        # 功能:添加通讯录成员
        # 1、首页点击添加成员
        # 第一种写法 ------- 可以  多个的时候默认第一个
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        # 第二种写法------ 可以   去列表下标第1个元素
        # self.driver.find_elements(By.CSS_SELECTOR,".index_service_cnt_item_title")[0].click()
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 3、点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()  # 4、验证添加成功
        result = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" == result


# 测试换上传





