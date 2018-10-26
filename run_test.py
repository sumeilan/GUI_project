# -*- coding:utf-8 -*-
import unittest
import os, sys


# sys.path.append('D:\\GUI_project_test2\\case')

# 多个集合case
def discover_case(case_dir):
    # 待执行用例的目录
    testcase = unittest.TestSuite()
    # discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中

    for test_suite in discover:
        for test_case in test_suite:
            print(test_case)
            testcase.addTests(test_case)

    return (testcase)


test_dir = 'D:\\GUI_project_test2\\case'
case = discover_case(case_dir=test_dir)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(case)
