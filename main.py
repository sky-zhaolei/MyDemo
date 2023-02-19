import unittest
from test_danyuanceshi import TestLogin
from unittestreport import TestRunner
from BeautifulReport import BeautifulReport
import ddt
import os

# 获取当前路径下的测试数据文件的绝对路径
case_dir = os.path.dirname(os.path.abspath(__file__))
# 收集测试用用例
s = unittest.TestLoader().discover(case_dir)
# 使用beautiful进行报告收集
runner = BeautifulReport(s)
# 输出测试报告
runner.report("第一份测试报告", "diyi.html")