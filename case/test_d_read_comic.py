# -*- coding:utf-8 -*-

# 已登录-阅读首页触漫官方的第一篇漫画，滑动10次，点赞
import unittest
from base import base_desired_caps, interrupt
from page import readComicPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    def test_read_comic(self):
        readComicPage.readComic(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
