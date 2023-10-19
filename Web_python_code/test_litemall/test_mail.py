# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: test_mail.py
@time: 2023/10/7 10:27

"""
import allure

from ALL_Test_code.log_utils import logger

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# ====问题1: 用例产生了脏数据，
# 解决方案: 清理对应的脏数据。清理的方式可以通过接口也可以通过u的方式，数据的清理一定到放在断言操作之后完成，要不然可能会影响断言结果
# ====问题2: 代码存在大量的强制等待
class TestMall:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 打开页面
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        # 问题，输入框内有默认值，此时send-keys不回清空只会追加
        # 解决方案: 在输入信息之前，先对输入框完成清空
        # 输入用户名密码
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        # 点击商场管理/商品类目，进入商品类目页面
        self.driver.implicitly_wait(3)

    def teardown_class(sef):
        sef.driver.quit()



    # 新增功能
    def test_add_type(self):
        # 点击商场管理/商品类目，进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='品牌制造商']").click()
        # 添加商品类目操作
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__body .el-input__inner").send_keys("新增品牌测试")
        self.driver.find_element(By.XPATH, "//*[@class='el-form el-form--label-left']/div[2]/div/div/input").send_keys(
            "ceshi")
        self.driver.find_element(By.XPATH, "//*[@class='el-form el-form--label-left']/div[4]/div/div/input").send_keys(
            "2")

        # ===========使用显示等待
        # ele = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary")))
        # ele.click()
        # 显示等待二号方案=============== 自定义显示等待
        def click_exception(by, element, max_attempts=5):
            def _inner(driver):

                # 多次点击按钮
                actul_attempts = 0  # 实际点击次数
                while actul_attempts < max_attempts:
                    # 进行点击操作
                    actul_attempts += 1  # 每次循环，实际点击次数加1
                    try:
                        # 如果点击过程报错，则直接执行 except 逻辑，并切继续循环
                        # #没有报错，则直接return 循环结束
                        driver.find_element(by, element).click()
                        return True
                    except Exception:
                        print("在点击动作时报错")
                # 当实际点击次数大于最大点击次数时，结束循环并抛出异常
                raise Exception("超出了最大点击次数")

            # return _inner0 错误写法
            return _inner

        WebDriverWait(self.driver, 10).until(click_exception(By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary"))

        # self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary").click()
        # find 如果没找到则会直接报错 ,finds 如果没找到会返回空列表，
        # 如果没找到，程序也不应该报错
        res = self.driver.find_elements(By.XPATH, "//*[text()='新增品牌测试']")
        logger.info(f"断言的实际结果为{res}")
        # 断言产品新增后是否成功找到，如果找到，证明新增成功，如果没找到则新增失败
        # 判断查找的结果是否为空列表，如果为空列表证明没找到，反之代表元素找到，用例执行成功
        assert res != []
        # 删除商品  数据的清理要放在断言之后操作,以免出现断言失败的情况
        self.driver.find_element(By.XPATH, "//*[text()='新增品牌测试']/../..//*[text()='删除']").click()

    # 删除功能
    def test_delete_type(self):
        # 点击商场管理/商品类目，进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='品牌制造商']").click()
        # 添加商品类目操作
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__body .el-input__inner").send_keys("删除品牌测试")
        self.driver.find_element(By.XPATH, "//*[@class='el-form el-form--label-left']/div[2]/div/div/input").send_keys(
            "ceshi")
        self.driver.find_element(By.XPATH,
                                 "//form[@class='el-form el-form--label-left']/div[4]//input[@class='el-input__inner']").send_keys(
            "2")
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary")))
        ele.click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary").click()
        # 删除商品
        self.driver.find_element(By.XPATH, "//*[text()='删除品牌测试']/../..//*[text()='删除']").click()
        # 断言:
        # 删除之后获取这个,删除商品测试的,这个商品类目是否还能获取到，如果获取到，证明没有删除成功，反之删除成功
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.visibility_of_any_elements_located(
                (By.XPATH, "//*[text()='删除商品测试']")))
        # 问题:因为代码执行速度过快，元素还未消失就捕获了
        # 解决:确认该元素不存在后，再捕获
        res = self.driver.find_elements(By.XPATH, "//*[text()='删除商品测试']")
        assert res == []
