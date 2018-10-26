# -*- coding:utf-8 -*-
import unittest
from appium import webdriver
import time

class MyTestCase(unittest.TestCase):

    #启动类
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.mallestudio.gugu.app'
        # desired_caps['appActivity'] = 'com.mallestudio.gugu.modules.home.activity.HomeActivity'
        desired_caps['appActivity'] = 'com.mallestudio.gugu.modules.StartActivity' #全新安装，启动类
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #启动页，滑到页面d
    def test_page(self):
        time.sleep(10)
        exist=True
        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').is_displayed()
            print(exist)
        except Exception as e:
            exist = False

        if exist == True:
            print '非第一次启动'
            self.driver.close_app()
        else:
            try:
                for i in range(1, 5):
                    self.driver.swipe(500, 300, 10, 300, 500)
                    time.sleep(2)

                self.driver.find_element_by_id('guide_btn').click()  # 开始体验按钮
                self.driver.find_element_by_id('btn_next').click() #立即走起
                self.driver.find_element_by_id('btn_skip').click() #不登录，稍后
            except Exception:
                print('无新手引导')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
