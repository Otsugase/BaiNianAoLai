import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    #   昵称
    nick_name_test_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    #   设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    #   加入超级VIP
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    @allure.step(title='我 获取 昵称')
    def get_nick_name_view(self):
        return self.find_element(self.nick_name_test_view).text

    @allure.step(title='我 点击 设置')
    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()

    @allure.step(title='我 点击 加入vip')
    def click_be_vip(self):
        self.find_element_with_scroll(self.be_vip_button).click()
        #   在网页环境停留足够的时间供打印出环境的名字
        time.sleep(2)