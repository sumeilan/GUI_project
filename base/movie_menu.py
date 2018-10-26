# -*- coding:UTF-8 -*-
import time
from base import base_methon


# 对白
def menuDialogue(self):
    self.driver.find_element_by_id('tv_menu_dialogue').click()  # 对白tab
    base_methon.isTipsExist(self)

    self.driver.find_element_by_android_uiautomator('new UiSelector().text("旁白")').click()  # 添加旁白
    time.sleep(2)

    try:
        if base_methon.isElementExist(self, 'et_input'):
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入内容")').click()
        else:
            self.driver.tap([(300, 350), ])
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入内容")').click()

        time.sleep(2)
        self.driver.find_element_by_id('et_input').send_keys(base_methon.generate_random_str(8))
        self.driver.find_element_by_id('iv_done').click()  # 输入完成
        self.driver.tap([(620, 80), ])  # 点击完成，坐标可能需要调整
    except Exception:
        print('error')


# 角色
def menuCharacter(self):
    self.driver.find_element_by_id('tv_menu_character').click()  # 角色tab
    base_methon.isTipsExist(self)

    self.driver.find_element_by_android_uiautomator('new UiSelector().text("额")').click()
    self.driver.find_element_by_id('iv_close').click()  # 角色tab



# 事件
def menuAction(self):
    self.driver.find_element_by_id('tv_menu_action').click()  # 事件tab
    base_methon.isTipsExist(self)

    if base_methon.isElementExist(self, 'iv_tips'):
        self.driver.find_element_by_id('iv_tips').click()

    self.driver.find_element_by_id('sdv_cover').click()  # 点击第一个事件
    self.driver.find_element_by_id('tv_choose').click()  # 使用
    try:
        self.driver.tap([(615, 120), ])
        self.driver.find_element_by_id('iv_close').click()  # 关闭面板
    except Exception:
        print('go')


# 声音
def menuMusic(self):
    self.driver.find_element_by_id('tv_menu_music').click()  # 音乐tab
    base_methon.isTipsExist(self)

    self.driver.find_element_by_android_uiautomator('new UiSelector().text("使用")').click()  # 使用第一个音乐
    self.driver.find_element_by_id('iv_close').click()  # 关闭面板
    time.sleep(2)


# 画面
def menuTableau(self):
    self.driver.find_element_by_id('tv_menu_tableau').click()  # 画面tab
    base_methon.isTipsExist(self)

    self.driver.find_element_by_android_uiautomator('new UiSelector().text("效果")').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("玻璃")').click()
    time.sleep(2)
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("使用")').click()  # 使用
    self.driver.find_element_by_id('iv_close').click()  # 关闭面板


# 字幕场景的文字
def menuLabel(self):
    for i in range(2):
        f = base_methon.generate_random_str(24)  # 生成随机字符串
        self.driver.find_element_by_id('tv_menu_label').click()  # 文字tab
        self.driver.find_element_by_id('et_text').send_keys(f)
        self.driver.find_element_by_id('iv_done').click()
