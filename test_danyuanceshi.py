import unittest
from login import login_check
from ddt import ddt, data
from handle_excel import Handle_Excel
import os
from handle_log import logger

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data.xlsx")
all_datas = Handle_Excel(file_path, "Sheet1").read_all_datas()


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        print("前置的内容")

    def tearDown(self):
        print("====后置的内容====")

    @classmethod
    def setUpClass(cls):
        print("类的前置内容++++")

    @classmethod
    def tearDownClass(cls):
        print("类的后置内容------")

    @data(*all_datas)
    def test_login(self, case):
        logger.info("开始执行用例--------------")
        logger.info("测试数据为：{}".format(case))
        res = login_check(case["user"], case["password"])
        try:
            self.assertEqual(res, eval(case["check"]))
        except  AssertionError:
            logger.info("断言失败，预计结果为{}".format(eval(case["check"])))
        else:
            logger.info("断言成功")
        logger.info("运行结果为：{}".format(res))
        logger.info("--------------用例执行结束")





