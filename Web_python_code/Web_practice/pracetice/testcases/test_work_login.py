# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: test_work_login.py
@time: 2023/10/9 10:59
登录  获取cookies
"""
import time

import yaml
from selenium import webdriver

from Web_python_code.Web_practice.pracetice.utils.base import BaseConfig


class TestCookiesLogin(BaseConfig):
    def test_get_cookies(self):
        # 1,访问企业微信登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 2,扫码 手动登录
        time.sleep(20)

        # 3, 登陆后获取cookie
        cookies = self.driver.get_cookies()
        print(cookies)
        # 4, 保存cookie
        with open(r"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\cookies.yaml","w") as f:
            # 将python转为yaml格式
            yaml.safe_dump(data=cookies, stream=f)

    def test_add_cookies(self):
        # 植入cookies
        # 1、访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2、获取本地的cookies
        with open(r"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\cookies.yaml", "r") as f:
            # 将python转为yaml格式
            cookies=yaml.safe_load(f)
        # 3、植入cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 4、再次访问企业微信主页/ 刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)






