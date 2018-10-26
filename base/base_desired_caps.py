# -*- coding:utf-8 -*-
from appium import webdriver


# 在appium server 与手机端建立会话关系时，手机端需要告诉服务端设备相关的一些参数，根据这些参数服务端可以做出相应的处理。
def base_desired_caps(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.mallestudio.gugu.app'
    desired_caps['appActivity'] = 'com.mallestudio.gugu.modules.home.activity.HomeActivity'
    # desired_caps['appActivity']='com.mallestudio.gugu.modules.StartActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
