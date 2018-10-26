# -*- coding:utf-8 -*-
import time
from base import scenes, movie_menu,base_methon
from appium import webdriver


def createMovie(self):
    exist = False
    self.driver.find_element_by_id('img_create').click()  # 小铅笔
    try:
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("漫剧")').click()
    except Exception:
        print('已选中，不可点击')

    # 引导
    try:
        self.driver.find_element_by_id('iv_guide_img').click()  # 引导
    except Exception:
        print "go"

    try:
        self.driver.find_element_by_id('sdv_cover').click()  # 点击第一个漫剧连载
        self.driver.find_element_by_id('btn_add_comic').click()  # 新建连载
        self.driver.find_element_by_id('et_title').send_keys(base_methon.generate_random_str(8))  # 输入单篇标题
        self.driver.tap([(700, 60), ])

        scenes.characterScene(self)  # 选择人物对话场景

        # movie_menu.menuDialogue(self)  # 对白—因为坐标定位不准，暂不执行
        time.sleep(1)
        movie_menu.menuCharacter(self)  # 角色
        time.sleep(1)
        movie_menu.menuAction(self)  # 事件
        time.sleep(1)
        movie_menu.menuTableau(self)  # 画面
        time.sleep(1)

        # 增场景
        self.driver.swipe(600, 300, 10, 300, 800)
        time.sleep(2)
        scenes.dialogueScene(self)  # 字幕场景
        movie_menu.menuLabel(self)  # 添加文字

        self.driver.find_element_by_id('iv_finish').click()  # 创作完成
        time.sleep(2)
    except Exception:
        print "go"

    return exist == True
