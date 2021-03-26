import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    #   我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    #   分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    #   购物车
    shop_chat_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

    #   首页
    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    #   放大镜 按钮
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    #   我
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    #   点击 分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.click(self.category_button)

    #   点击 购物车
    @allure.step(title='主页 点击 购物车')
    def click_shop_cart(self):
        self.click(self.shop_chat_button)

    #   点击 首页
    @allure.step(title='主页 点击 首页')
    def click_home(self):
        self.click(self.home_button)

    #   点击 放大镜
    @allure.step(title='主页 点击 放大镜')
    def click_search(self):
        self.click(self.search_button)

    @allure.step(title='主页 登录')
    def login_if_not(self, page):
        #   判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        #   没登录，就去登录
        #   点击 已有账号
        page.register.click_login()
        #   输入 用户名
        page.login.input_username("itheima_test")
        #   输入 密码
        page.login.input_password("itheima")
        #   点击 登录
        page.login.click_login()