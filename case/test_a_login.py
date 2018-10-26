# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack
from base import base_desired_caps, interrupt
from page import loginPage


# 登录测试流程
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    @data(
        ('18825076907', '123456', False))
    @unpack
    def test_login(self, username, password, expectedresult):
        exist = loginPage.login(self, username, password)
        self.assertEqual(exist, expectedresult)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
