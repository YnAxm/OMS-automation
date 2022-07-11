# 开始执行自动化用例
# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
from config import dingding
from config import id_order
id_order.format_time_to_timestamp()
# print(id_order.format_time_to_timestamp())

# 用例存放位置
case_path = "E:\\OMS-automation\\case"
# 测试报告存放位置
log_path = "E:\\OMS-automation\\report\\report"
# 测试报告名称
filename = '测试报告'
# 用例名称
description = '测试'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*1test.py"
pattern = "testzhengxiang.py"
# dingding.msg()

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, report_dir=log_path)
