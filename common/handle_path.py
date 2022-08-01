"""
Time:2022/8/1 000118:06
Author:bty
"""
import os

# 项目的根目录
DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 项目的公共模块路径
COM_PATH = os.path.join(DIR_PATH, 'common')

# 配置文件目录
CONF_PATH = os.path.join(DIR_PATH, 'config')

# 测试数据
DATAS_PATH = os.path.join(DIR_PATH, 'datas')

# 日志文件路径
LOGS_PATH = os.path.join(DIR_PATH, 'logs')

# 测试报告存放路径
REPORTS_PATH = os.path.join(DIR_PATH, 'reports')

# 测试用例代码存放路径
TEST_PATH = os.path.join(DIR_PATH, 'testcases')


