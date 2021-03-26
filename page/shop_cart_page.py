import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ShopCartPage(BaseAction):

    #   点击 全选
    select_all_button = By.ID, "com.yunmall.lc:id/iv_select_all"

    #   点击 全选
    @allure.step(title="购物车 点击 全选")
    def click_select_all(self):
        self.click(self.select_all_button)

    #   编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    #   点击 全选
    @allure.step(title="购物车 点击 编辑")
    def click_edit(self):
        self.click(self.edit_button)

    #   完成 按钮
    commit_button = By.XPATH, "//*[@text='完成']"

    #   点击 全选
    @allure.step(title="购物车 点击 完成")
    def click_commit(self):
        self.click(self.commit_button)

    #   加号 按钮
    add_button = By.ID, "com.yunmall.lc:id/iv_add"

    #   点击 全选
    @allure.step(title="购物车 点击 加号")
    def click_add(self):
        self.click(self.add_button)

    #   单价 特征
    price_feature = By.ID, "com.yunmall.lc:id/tv_price"

    #   总价 特征
    all_price_feature = By.ID, "com.yunmall.lc:id/tv_count_money"

    def get_price(self):
        #   获取单价的文字
        price_text = self.get_text(self.price_feature)
        #   通过 deal_with_price 去掉前面的人名币符号，并且转化成float类
        return self.deal_with_price(price_text)

    def get_all_price(self):
        #   获取单价的文字
        price_text = self.get_text(self.all_price_feature)
        #   通过 deal_with_price 去掉前面的人名币符号，并且转化成float类
        return self.deal_with_price(price_text)

    def deal_with_price(self, price):
        return float(price[2: ])

    #   删除 按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    #   确认 按钮
    yes_button = By.XPATH, "//*[@text='确认']"

    #   点击 删除
    def click_delete(self):
        self.click(self.delete_button)

    #   点击 确认
    def click_yes(self):
        self.click(self.yes_button)

    #   判断购物车是否为空
    def id_shop_cart_empty(self):
        xpath = By.XPATH, "//*[contains(@text, '购物车还是空的')]"
        return self.is_feature_exist(xpath)