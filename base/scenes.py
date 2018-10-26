# -*- coding:UTF-8 -*-
# 四种场景
import time
from base import base_methon


# 人物对话场景
def characterScene(self):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("人物对话")').click()
    self.driver.find_element_by_id('fl_add').click()  # 添加背景
    time.sleep(2)
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("公交站")').click()
    time.sleep(2)
    self.driver.find_element_by_id('tv_choose').click()  # 使用背景
    self.driver.tap([(700, 60), ])  # 点击右上角√，完成

    try:
        if base_methon.isElementExist(self, 'iv_tips'):
            self.driver.find_element_by_id('iv_tips').click()

    except Exception:
        print 'go'


# 自由场景
def freeScene(self):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("自制场景")').click()


# 通讯场景
def chatScene(self):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("手机通讯")').click()


# 字幕场景
def dialogueScene(self):
    self.driver.find_element_by_id('sdv_scene_dialogue').click()  # 选择字幕场景
    self.driver.find_element_by_id('fl_add').click()  # 添加背景
    time.sleep(2)
    self.driver.find_element_by_id('tv_name').click()  # 选择第一个背景
    time.sleep(2)
    self.driver.find_element_by_id('tv_choose').click()  # 使用背景
    self.driver.tap([(700, 60), ])  # 点击右上角√，完成
