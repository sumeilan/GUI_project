# -*- coding:UTF-8 -*-
import time
from base import base_methon


# 场景
def menuScene(self):
    quit()


# 角色
def menuCharacter(self):
    self.driver.find_element_by_id('tv_menu_character').click()  # 点击角色tab
    try:
        self.driver.find_element_by_id('btn_skip').click()  # 跳过
        self.driver.find_element_by_id('btn_next').click()
    except Exception:
        print ("go")

        time.sleep(3)
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("额")').click()
        self.driver.tap([(300, 500), ])  # 选中角色
        self.driver.find_element_by_id('iv_right_background').click()  # 选中角色，换方向
        self.driver.find_element_by_id('tv_menu_ok').click()  # 完成
        time.sleep(2)
        self.driver.find_element_by_id('btn_skip').click()  # 跳过
        self.driver.find_element_by_id('btn_next').click()
    except Exception:
        print "go"


# 文字
def menuDialogue(self):
    self.driver.find_element_by_id('tv_menu_dialogue').click()  # 点击文字tab
    self.driver.find_element_by_id('sdv_cover').click()  # 点击第一个文字气泡
    self.driver.tap([(300, 500), ])  # 选中文字气泡
    try:
        self.driver.find_element_by_id('iv_tips').click()  # 提示
    except Exception:
        print "go"
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击输入文字")').click()
    self.driver.find_element_by_id('et_input').send_keys(base_methon.generate_random_str(10))
    time.sleep(2)
    self.driver.find_element_by_id('iv_done').click()
    self.driver.find_element_by_id('tabDone').click()

# 素材
def menuMaterial(self):
    self.driver.find_element_by_id('tv_menu_material').click()  # 点击素材tab
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("自然")').click()  # 选择“自然”分类
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("植物")').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("木头")').click()


# 格子
def menuBlock(self):
    self.driver.find_element_by_id('tv_menu_block').click()  # 点击格子tab
    self.driver.find_element_by_id('sdv_cover').click()  # 点击第一个格子
    time.sleep(2)
    self.driver.tap([(340, 500), ])  # 点击格子
    # menuTableau(self)
    # self.driver.find_element_by_id('iv_ok').click()  # 点击右上角保存格子


# 画面
def menuTableau(self):
    self.driver.find_element_by_id('tv_menu_tableau').click()  # 点击画面tab
    self.driver.find_element_by_id('tv_name').click()  # 点击第一个画面
    self.driver.find_element_by_id('tv_name').click()  # 点击画面的第一个
