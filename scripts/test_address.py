import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_add_address"))
    def test_add_address(self, args):

        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]

        #   首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        #   我 点击 设置
        self.page.me.click_setting()
        #   设置 点击 地址管理
        self.page.setting.click_address_list()
        #   地址管理 点击 新增地址
        self.page.address_list.click_add_address()
        #   地址管理 输入 收件人
        self.page.edit_address.input_name(name)
        #   地址管理 输入 电话
        self.page.edit_address.input_phone(phone)
        #   地址管理 输入 详细地址
        self.page.edit_address.input_info(info)
        #   地址管理 输入 邮编
        self.page.edit_address.input_post_code(post_code)
        #   新增地址 勾选 设为默认地址
        self.page.edit_address.click_default_address()
        #   新增地址 选择一个随机的区域
        self.page.edit_address.choose_region()
        #   新增地址 点击 保存
        self.page.edit_address.click_save()

        if toast is None:
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name, phone), "保存成功，默认的姓名和电话输入不否"
        else:
            assert self.page.edit_address.is_toast_exist(toast), "保存不成功，toast内容和预期不符"

    def test_edit_address(self):
        #   首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        #   我 点击 设置
        self.page.me.click_setting()
        #   设置 点击 地址管理
        self.page.setting.click_address_list()

        if not self.page.address_list.is_default_feature_exist():

            #   地址管理 点击 新增地址
            self.page.address_list.click_add_address()
            #   地址管理 输入 收件人
            self.page.edit_address.input_name("zhangsan")
            #   地址管理 输入 电话
            self.page.edit_address.input_phone("18888888888")
            #   地址管理 输入 详细地址
            self.page.edit_address.input_info("三单元 504")
            #   地址管理 输入 邮编
            self.page.edit_address.input_post_code("100000")
            #   新增地址 勾选 设为默认地址
            self.page.edit_address.click_default_address()
            #   新增地址 选择一个随机的区域
            self.page.edit_address.choose_region()
            #   新增地址 点击 保存
            self.page.edit_address.click_save()

        #   进入 默认地址 进入了edit_address界面
        self.page.address_list.click_default_address()
        #   重新输入 收件人
        self.page.edit_address.input_name("李四")
        #   重新输入 手机号
        self.page.edit_address.input_phone("16666666666")
        #   重新输入 详细地址
        self.page.edit_address.input_info("302 二单元")
        #   重新输入 邮编
        self.page.edit_address.input_post_code("222222")
        #   重新输入 所在地区
        self.page.edit_address.choose_region()
        #   保存
        self.page.edit_address.click_save()

        #   断言，是否出现 保存成功 的toast信息
        assert self.page.address_list.is_toast_exist("保存成功")

    def test_delete_address(self):
        #   首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        #   我 点击 设置
        self.page.me.click_setting()
        #   设置 点击 地址管理
        self.page.setting.click_address_list()

        #   断言 是否有地址可删除
        assert self.page.address_list.is_default_feature_exist(), "默认标记不存在，没有地址可以删除"

        for i in range(10):
            self.page.address_list.click_edit()
            #   判断 删除是否存在
            if not self.page.address_list.is_delete_exist():
                break
            #   存在 则点击
            #   不存在 break
            self.page.address_list.click_delete()
            self.page.address_list.click_commit()

        #   点击编辑
        self.page.address_list.click_edit()
        #   断言 删除按钮 是否存在 如果不存在则通过 如果存在则有问题
        assert not self.page.address_list.is_delete_exist(), "收货地址没有删除完毕"


