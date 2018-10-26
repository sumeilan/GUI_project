# -*- coding:utf-8 -*-

def interrupt(self):
    try:
        if self.driver.find_element_by_android_uiautomator('new UiSelector().text("作品未保存")').is_displayed():
            self.driver.find_element_by_id('textViewCancel').click()  # 放弃
    except Exception:
        print('')
