# -*- coding: utf-8 -*-

"""
@author: lenovo
@software: PyCharm
@file: log_utils.py
@time: 2023/10/7 17:38

"""
# 日志配置
import logging

# 创建Logger实例
logger = logging.getLogger('simple_example')
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 流处理器
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 日志打印格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 添加格式配置
ch.setFormatter(formatter)
# 添加日志配置
logger.addHandler(ch)
