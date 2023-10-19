# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: base.py
@time: 2023/10/9 17:17

"""
import time

import allure
import yaml
from faker import Faker
from selenium import webdriver


class BaseConfig:
    def setup_class(self):
        # 准备资源文件,做初始化
        # 创建一个driver实例变量
        # 前置
        self.fake = Faker("zh-CN")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 植入cookies
        # 1、访问企业微信主页
        self.driver.get(r"https://work.weixin.qq.com/wework_admin/frame")
        # 2、获取本地的cookies
        with open(r"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\cookies.yaml", "r") as f:
            # 将python转为yaml格式
            cookies = yaml.safe_load(f)
        # 3、植入cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 4、再次访问企业微信主页/ 刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown_class(self):
        # 后置
        # 清除所有cookie
        # self.driver.delete_all_cookies()
        self.driver.quit()

    # 截图操作
    def get_acreen(self):
        timestamp = int(time.time())
        # 注意:!!一定要提前创建好images 路径
        image_path = f"./imags/imags_{timestamp}.PNG"
        # 截图
        self.driver.save_screenshot(image_path)
        # 讲截图放到报告的数据中
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
