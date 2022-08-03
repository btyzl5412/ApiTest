"""
Time:2022/8/2 000216:57
Author:bty
公共方法库
"""
import random
import string
from common.handle_db import HandleDB


def random_phone() -> str:
    """
    随机生成手机号
    :return:
    """
    mysql = HandleDB()
    sql = "SELECT * FROM futureloan.member where mobile_phone = '{}'"
    while True:
        start_ = ['132', '133', '156', '138']
        end = "".join(random.sample(string.digits, 8))
        phone = random.choice(start_) + end
        count = mysql.find_count(sql=sql.format(phone))
        if count > 0:
            continue
        else:
            return phone


def res_assert_expected(res, expected: dict):
    """
    实际结果与预期结果进行比对
    :param res: 实际结果
    :param expected: 预期结果
    :return:
    """
    for k in expected:
        if expected.get(k) == res.get(k):
            pass
        else:
            raise AssertionError("预期结果：{} not in 实际结果：{}".format(expected, res))


if __name__ == '__main__':
    p = random_phone()
    print(p, type(p))
