# -*- coding:utf-8 -*-
import time


def searchPage(self, input):
    exist = True

    time.sleep(3)
    self.driver.find_element_by_id('imageView_category').click()
    self.driver.find_element_by_id('et_search').send_keys(input)
    self.driver.find_element_by_id('tv_search').click()

    try:
        comic = self.driver.find_elements_by_id('tv_comic_name')
        comic[0].click()  # 点击搜索结果页面的第一部漫画连载作品

        if self.driver.find_element_by_id('btn_read').is_displayed():
            return exist
    except Exception as e:
        return exist == False
