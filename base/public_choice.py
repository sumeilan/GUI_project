# -*- coding:UTF-8 -*-
import time


def addComicSerials(self):
    self.driver.find_element_by_id('tv_serials').click()  # 加入连载
    self.driver.find_element_by_id('sdv_cover').click()  # 选择第一个连载
    publicAsOffice(self)


def publicAsDraft(self):
    self.driver.find_element_by_id('tv_publish_as_draft').click()  # 转为草稿
    self.driver.find_element_by_id('tv_quit').click()  # 点击退出创作，回到小铅笔页面


def publicAsOffice(self):
    self.driver.find_element_by_id('tv_publish_official').click()  # 发布
    time.sleep(3)
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()  # 点击完成，回到小铅笔页面
