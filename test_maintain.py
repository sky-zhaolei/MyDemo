"""
Author:赵某
Time:2023/3/11 16:58
PROJECT:MyDemo
"""

import unittest
from ddt import ddt, data
from handle_excel import Handle_Excel
import os
from handle_log import logger
from handle_request import send_requests

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data.xlsx")
all_datas = Handle_Excel(file_path, "maintainself").read_all_datas()

@ddt
class TestMaintain(unittest.TestCase):

    @data(*all_datas)
    def test_self_built(self, case):
        logger.info("开始执行用例--------------")
        logger.info("当前步骤：{}".format(case["title"]))
        logger.info("测试数据:{}".format(case["data"]))
        res = send_requests(method=case["method"], url=case["url"], data=eval(case["data"]))
        try:
            self.assertEqual(str(res.json()["code"]), eval(case["assert"])["code"])
        except AssertionError:
            logger.info("断言失败，预计结果为{}".format("code = 200"))
            raise
        else:
            logger.info("断言成功")
        finally:
            logger.info("运行结果为：{}".format(res.json()))
            logger.info("--------------用例执行结束")
