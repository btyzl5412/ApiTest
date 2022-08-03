"""
Time:2022/8/2 000220:12
Author:bty
"""
import pytest
import os
import requests
import json
from common.handle_replace import replace_data,BaseCase
from common.handle_log import mylog
from common.handle_path import DATAS_PATH
from common.handle_excel import HandleExcel
from common.handle_config import conf
from common.handle_com import random_phone, res_assert_expected


class TestRegister(BaseCase):
    # 获取测试数据
    excel = HandleExcel(file_name=os.path.join(DATAS_PATH, 'newApiCase.xlsx'), sheet_name='register')
    cases = excel.read_excel()
    # 基础url
    base_url = conf.get('uat', 'base_url')
    # 基础请求头,获取的字符串转换为字典
    base_headers = eval(conf.get('uat', 'base_headers'))

    @pytest.mark.parametrize('items', cases)
    def test_register(self, items):
        url = self.base_url + items['url']
        method = items['method'].lower()
        expected = eval(items['expected'])
        row = items['case_id'] + 1
        BaseCase.phone = random_phone()
        data = eval(replace_data(items['data']))
        # if "#phone#" in items['data']:
        #     phone = random_phone()
        #     items['data'] = items['data'].replace('#phone#', phone)
        # data = eval(items['data'])
        # 发起请求
        response = requests.request(url=url, method=method, json=data, headers=self.base_headers)
        res = response.json()
        # 进行断言
        try:
            res_assert_expected(res, expected)
        except AssertionError as e:
            mylog.error("用例--【编号为:{}，标题为:{}】---执行失败".format(items['case_id'], items['title']))
            mylog.exception(e)
            self.excel.write_excel(row=row, column=9, value='F', colour=False)
            self.excel.write_excel(row=row, column=8, value=json.dumps(res, ensure_ascii=False), colour=False)
            raise e
        else:
            mylog.info("用例--【编号为:{}，标题为:{}】---执行成功".format(items['case_id'], items['title']))
            self.excel.write_excel(row=row, column=9, value='T')
            self.excel.write_excel(row=row, column=8, value="")


if __name__ == '__main__':
    pytest.main()
