import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # #   测试代码：判断登录状态，没有登录就登录，home_page,login_if_not
    # def test_hello(self):
    #     self.page.home.login_if_not(self.page)

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        #   解析yaml的数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        #   脚本流程
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()

        if toast is None:
            assert self.page.me.get_nick_name_view() == username, "登录后的用户名和输入的用户名不一致"
        else:
            #   找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.login.is_toast_exist(toast)