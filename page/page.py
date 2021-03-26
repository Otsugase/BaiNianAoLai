from base.base_action import BaseAction
from page.about_page import AboutPage
from page.address_list_page import AddressListPage
from page.category_page import CategoryPage
from page.edit_address_page import EditAddressPage
from page.goods_detail_page import GoodsDetailPage
from page.goods_list_page import GoodsListPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegisterPage
from page.search_page import SearchPage
from page.setting_page import SettingPage
from page.shop_cart_page import ShopCartPage
from page.vip_page import VipPage


class Page(BaseAction):

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)

    @property
    def vip(self):
        return VipPage(self.driver)

    @property
    def address_list(self):
        return AddressListPage(self.driver)

    @property
    def edit_address(self):
        return EditAddressPage(self.driver)

    @property
    def category(self):
        return CategoryPage(self.driver)

    @property
    def goods_detail(self):
        return GoodsDetailPage(self.driver)

    @property
    def goods_list(self):
        return GoodsListPage(self.driver)

    @property
    def shop_cart(self):
        return ShopCartPage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)