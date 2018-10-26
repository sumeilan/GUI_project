# -*- coding:utf-8 -*-
import time
from base import comic_menu


def createComic(self):
    exist = False
    self.driver.find_element_by_id('img_create').click()  # 小铅笔
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("漫画")').click()
    except Exception:
        print('已选中，不可点击')

    # 引导
    try:
        self.driver.find_element_by_id('iv_guide_img').click()  # 引导
        self.driver.find_element_by_id('iv_guide_img').click()  # 引导
    except Exception:
        print "go"

    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("新建单篇")').click()  # 新建单篇
        self.driver.find_element_by_id('btn_next').click()  # 走起
        self.driver.find_element_by_id('btn_skip').click()  # 跳过
    except Exception:
        print "go"

    comic_menu.menuCharacter(self)  # 角色tab的操作

    comic_menu.menuMaterial(self)  # 素材tab的操作

    comic_menu.menuDialogue(self)  # 文字tab的操作

    comic_menu.menuBlock(self)  # 格子tab的操作

    try:
        self.driver.find_element_by_id('iv_close_selected_entity_title_bar').click()  # 完成元素的操作
    except Exception:
        print "go"

    self.driver.find_element_by_id('tv_create_finish').click()  # 创作页面右上角的保存，保存
    time.sleep(5)
    return exist == True
