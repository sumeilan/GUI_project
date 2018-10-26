# -*- coding:UTF-8 -*-

def login(self, username, password):
    exist = True
    self.driver.find_element_by_id('img_me').click()
    self.driver.find_element_by_id('btn_login').click()
    self.driver.find_element_by_id('et_phone').send_keys(username)
    self.driver.find_element_by_id('et_pwd').send_keys(password)
    self.driver.find_element_by_id('tv_login').click()

    try:
        if self.driver.find_element_by_id('tv_login').is_displayed():
            return exist
    except Exception as e:
        return exist == False
