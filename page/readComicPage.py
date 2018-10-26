# -*- coding:UTF-8 -*-
import time


def readComic(self):
    time.sleep(5)
    els = self.driver.find_elements_by_id('image')
    els[1].click()  # 点击首页-触漫官方的第一篇漫画
    time.sleep(5)
    self.driver.find_element_by_id('btn_read').click()  # 点击开始阅读，阅读第一话
    time.sleep(5)

    # 下滑10次
    for i in range(1, 10):
        self.driver.swipe(710, 1270, 710, 10, 1000)
        time.sleep(3)

    self.driver.swipe(710, 50, 710, 1270, 1000)  # 上滑一下，调出评论、点赞栏
    self.driver.find_element_by_id('tv_like').click()  # 点赞
    # self.driver.find_element_by_id('tv_comment').click()  # 点击评论，进入评论页面

    self.driver.press_keycode(4)  # 点击返回,判断“续看”按钮是否存在
