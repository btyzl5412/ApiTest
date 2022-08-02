"""
Time:2022/8/2 000211:11
Author:bty
日志输出公共方法
"""
import logging
import os
from common.handle_path import LOGS_PATH


def create_log():
    # 设置日志收集器
    log = logging.getLogger(name="bty")

    # 设置日志收集等级
    log.setLevel(level="DEBUG")

    # 设置日志输出渠道
    # 输出至文件
    sh = logging.FileHandler(os.path.join(LOGS_PATH, 'logs.log'), encoding='utf-8')
    sh.setLevel(level="DEBUG")
    log.addHandler(sh)

    # 输出控制台
    fh = logging.StreamHandler()
    fh.setLevel(level="DEBUG")
    log.addHandler(fh)

    # 4.设置输出格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    # 创建日志格式对象
    log_format = logging.Formatter(formats)

    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 5.返回日志收集器
    return log


mylog = create_log()
