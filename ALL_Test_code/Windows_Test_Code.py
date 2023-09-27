# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: Windows_Test_Code.py
@time: 2023/9/27 15:04
窗口切换测试
"""
import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from ALL_Test_code.Base import BaseConf


class TestWindows(BaseConf):
    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, "s-top-loginbtn").click()
        # 打印当前窗口
        print(self.driver.current_window_handle)
        # 打印所有窗口
        print(self.driver.window_handles)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 打印当前窗口
        print(self.driver.current_window_handle)
        # 打印所有窗口
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        # 跳转最后一个窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("13800000000")
        sleep(2)
        # 返回第一个窗口
        self.driver.switch_to.window(windows[0])
        # self.driver.find_element(By.ID,"TANGRAM__PSP_10footerULoginBtn").click()
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("login username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换frame
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element(By.ID, "draggable").text)
        # 切换frame为当前的父frame
        self.driver.switch_to.parent_frame()
        # 切换到默认的frame下 就是最开始进入页面获取到的那个frame
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, "submitBTN").text)

    def test_aler(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        # 拖动
        action.drag_and_drop(drag, drop).perform()
        time.sleep(3)
        print("点击 alert 确认")
        # 点击alre中的确认按钮
        self.driver.switch_to.alert.accept()
        # 切换默认frame
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        sleep(3)
