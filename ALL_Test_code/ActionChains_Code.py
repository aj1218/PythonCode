# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: ActionChains_Code.py
@time: 2023/9/25 17:30

键盘事件

"""
import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from ALL_Test_code.Base import BaseConf


class TestKeyboard(BaseConf):

    def test_shift(self):
        """
        1.访问 https://ceshiren.com/ 官方网站
        2。 点击搜索按钮
        3，输入搜索的内容，输入的同时按着shift 键
        """

        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 目标即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # key_down()代表按下某个键位
        # send_keys("appium")  输入内容`
        # .perform()   确定输入内容,执行以上操作
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys("appium").perform()
        time.sleep(3)

    def test_enter(self):
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
        # 第一种回车方式# self.driver.find_element(By.ID，"query").send_keys(Keys.ENTER)#第二种回车方式
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(3)

    # 复制粘贴逻辑
    def test_copy_and_paste(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 判断操作系统是否为mac如果是mac 则返回 command 键位， 如果是windows 返回 control键位
        command_control = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        # 剪切后复制,几个v就代表负责制几次,,,key_down(command_control)鼠标左移几次就写多少个
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys("selenium!").key_down(Keys.ARROW_LEFT).key_down(
            Keys.ARROW_LEFT).key_down(Keys.ARROW_LEFT).key_down(command_control).send_keys("xvvvvvv").key_up(
            command_control).perform()
        time.sleep(10)

    def test_copy_and_paste1(self):
        # 演练环境2   复制粘贴逻辑
        self.driver.get("https://ceshiren.com/")
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.driver.find_element(By.ID, "search-button").click()
        ele = self.driver.find_element(By.ID, "search-term")
        # 打开搜索，选择搜索框，输入selenium，剪切后复制，几个v就代表复制几次
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys("Selenium!").send_keys(Keys.ARROW_LEFT).key_down(
            cmd_ctrl).send_keys("xvvvvv").key_up(cmd_ctrl).perform()
        time.sleep(5)

    # 双击方法
    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        self.driver.find_element(By.ID, "primary_btn").click()
        ele = self.driver.find_element(By.ID, "primary_btn")
        # 调用 双击方法， 传入被双击的元素
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(3)

    # 拖动元素
    def test_drap_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 获取起始元素的位置
        start_ele = self.driver.find_element(By.ID, "item1")  # 获取目标元素的位置
        target_ele = self.driver.find_element(By.ID, "item3")  # 实现拖拽操作
        ActionChains(self.driver).drag_and_drop(start_ele, target_ele).perform()
        time.sleep(3)

    # 鼠标悬浮事件
    def test_move_element(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.driver.find_element(By.CSS_SELECTOR, ".menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'管理班')]").click()
        time.sleep(3)

    # 滚动操作
    def test_scroll_to_element(self):
        self.driver.get("https://ceshiren.com/")
        ele = self.driver.find_element(By.XPATH, "//*[text() ='20230917-Python基础']")
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(10)

        # 滚动操作

    def test_scroll_to_xy(self):
        self.driver.get("https://ceshiren.com/")
        ActionChains(self.driver).scroll_by_amount(0, 1000).perform()
        time.sleep(10)
