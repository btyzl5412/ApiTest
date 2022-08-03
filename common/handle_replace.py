"""
Time:2022/8/3 000319:58
Author:bty
"""
import re
from common.handle_config import conf


class BaseCase:
    pass


def replace_data(data) -> str:
    """
    替换字符串
    :param data: 需要替换的字符串
    :return:
    """
    while re.search('#(.+?)#', data):
        res2 = re.search('#(.+?)#', data)
        # 需要替换的内容,例： #phone#
        item = res2.group()
        # 需要进行查找的属性名称 ，例 phone
        attr = res2.group(1)
        try:
            value = getattr(BaseCase, attr)
        except AttributeError:
            value = conf.get('uat', attr)
        # 进行替换
        data = data.replace(item, str(value))

    return data
