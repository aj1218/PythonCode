# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: test_biadu.py
@time: 2023/10/17 10:37

"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '. ')))

import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# from ALL_Test_code.log_utils import logger


# 目标1:实现代码异常的时候，截图/打印page_source
# 实现方法: try catch 配合截图/ page_source
# ===问题1: 异常处理会影响用例本身的结果
# 解决方案: 在exception 之后再把异常抛出
# ===问题2: 异常捕获处理代码和业务代码无关，不能耦合
# 解决方案: 使用装饰器装饰用例或者相关方法，就不会体现在源码中了
# 问题3:被装饰函数还没有执行，所以还没有self.driver
# #解决方案:获取driver 放在函数执行之后

# 先吧装饰器的架子搭好
# 把相关逻辑嵌套进来

# =====问题4:隐藏的小bug，一旦被装饰方法有返回值，会丢失返回值解决方案:
# 当被装饰方法/函数发生异常就捕获并做数据记录
# return func(*args，**kwargs)
def ui_exceptlon_record(func):
    def inner(*args, **kwargs):

        try:
            # 当被装饰方法/函数 发生异常就捕获并做数据记录
            return func(*args, **kwargs)

        except Exception:
            # 出现异常的处理
            # 获取被装饰方法的self,也就是实例对象(self.driver)
            # 通过self 就可以拿到声明的实例变最driver
            # 前提条件: 1，被装饰的方法是一个实例方法， 2.实例需要有实例变量self.driver
            # 问题:被装饰函数还没有执行，所以还没有self.driver
            # 解决方案1:获取driver 放在函数执行之后
            # 解决方案2:保证使用装饰器的时候，driver 已经声明 子啊setup_class中声明:  self.driver = webdriver.Chrome()

            driver = args[0].driver
            print("出现异常啦")
            timestamp = int(time.time())
            # 注意:!!一定要提前创建好images 路径
            image_path = f"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\imags_{timestamp}.PNG"
            page_source_path = f"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            # 讲截图放到报告的数据中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # 记录page_source
            # 解决方案: 在报错的代码行之前打印page_source，确认定位的元素没有问题
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)
            # 获取page_source
            # logger.debug(self.driver.page_source)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise Exception

    return inner


class TestBaidu:
    def test_baidu(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        try:
            # 如果发生异常
            self.driver.find_element(By.ID, "su1")
        except Exception:
            # 出现异常的处理
            print("出现异常啦")
            timestamp = int(time.time())
            # 注意:!!一定要提前创建好images 路径
            image_path = f"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\imags_{timestamp}.PNG"
            page_source_path = f"D:\PythonCode\Web_python_code\Web_practice\pracetice\datas\page_source_{timestamp}.html"
            # 截图
            self.driver.save_screenshot(image_path)
            # 讲截图放到报告的数据中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # 记录page_source
            # 解决方案: 在报错的代码行之前打印page_source，确认定位的元素没有问题
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(self.driver.page_source)
            # 获取page_source
            # logger.debug(self.driver.page_source)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise Exception

        self.driver.quit()

    @ui_exceptlon_record
    def test_baidu1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "su")
        self.driver.quit()
