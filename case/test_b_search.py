# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack
from base import base_desired_caps, interrupt
from page import searchPage


# 搜索测试流程
@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    @data(
        (u'王爷的小兔妖', True)
    )
    @unpack
    def test_search(self, input, expectedresult):
        exist = searchPage.searchPage(self, input)
        self.assertEqual(exist, expectedresult)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
