"""
Time:2022/8/2 000210:54
Author:bty
"""
import os
from common.handle_path import CONF_PATH
from configparser import ConfigParser


class Conf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf-8')


conf = Conf(filename=os.path.join(CONF_PATH, 'conf.ini'))

