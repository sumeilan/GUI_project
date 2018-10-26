# -*- coding:utf-8 -*-
#创作漫画单篇--》小铅笔--》漫画--》画漫画--》新增单篇--》添加角色--》改变角色方向--》添加素材--》保存
import unittest
from ddt import ddt, data, unpack
from base import base_desired_caps,public_choice,interrupt
from page import createComicPage

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    # @data(
    #     ('public', True),
    #     ('draft', True),
    #     ('draft', True),
    #     ('serials',True)
    # )
    @data(
        ('draft', True)
    )
    @unpack
    # 画漫画流程
    def test_creation(self, input,expectedresult):
        exist=createComicPage.createComic(self)
        if input=='draft':
            public_choice.publicAsDraft(self)
        elif input=='public':
            public_choice.publicAsOffice(self)
        elif input == 'serials':
            public_choice.addComicSerials(self)

        try:
            return exist == True
        except Exception:
            print "ERROR"
        self.assertEqual(exist, expectedresult)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
