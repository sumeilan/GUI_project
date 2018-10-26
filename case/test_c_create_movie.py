# -*- coding:utf-8 -*-
# 创作漫剧单篇，人物对话场景+字幕场景
import unittest
from ddt import ddt, data, unpack
from base import base_desired_caps, public_choice, interrupt
from page import createMoviePage


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    @data(
        ('public', True)
    )
    @unpack
    # 画漫剧流程
    def test_creation(self, input, expectedresult):
        exist = createMoviePage.createMovie(self)
        if input == 'draft':
            public_choice.publicAsDraft(self)
        elif input == 'public':
            public_choice.publicAsOffice(self)

        try:
            return exist == True
        except Exception:
            print "ERROR"
        self.assertEqual(exist, expectedresult)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
