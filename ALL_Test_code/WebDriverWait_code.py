# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: WebDriverWait_code.py
@time: 2023/9/25 14:55

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 输入一:点击的目标按钮 输入二:下一个页面的某个元素
def muliti_click(target_element, next_element):
    def _inner(driver):
        driver.find_element(*target_element).click()
        # 第一个结果就是找到了,return 的内容为webelement对象
        # 第二种结果为 没有找到  driver.find_element(*next_element) 代码报错,
        # 但是被 until中的异常捕获逻辑捕获异常。继续循环
        return driver.find_element(*next_element)

    return _inner


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 问题: 使用官方提供的expected condition 已经无法满足需求
    # 解决方案: 自己封装期望条件
    # 期望条件的设计:需求:一直点击按钮，直到下一个页面出现为止
    WebDriverWait(driver, 1).until(muliti_click(
        (By.ID, "primary_btn"),
        (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")
    ))
    time.sleep(5)


if __name__ == '__main__':
    wait_until()
