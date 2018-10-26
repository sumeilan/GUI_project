# -*- coding:utf-8 -*-
import random


# 判断元素是否存在
def isElementExist(self, element):
    flag = True
    try:
        self.driver.find_element_by_id(element)
        return flag
    except:
        flag = False
        return flag


# 生成随机字符串
def generate_random_str(randomlength=8):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


# 判断是否有新手引导，有新手引导则点击新手引导
def isTipsExist(self):
    flag = True
    try:
        self.driver.find_element_by_id('iv_tips').click()
        return flag
    except:
        flag = False
        return flag
