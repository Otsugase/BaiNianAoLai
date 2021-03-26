import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        #   根据特征，找元素
        #   feature,特征
        #   timeout,超时时间
        #   poll,频率
        #   return,元素
        feature_by, feature_value = feature
        # element = self.driver.find_element(feature_by, feature_value)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1.0):
        #   根据特征，找多个符合条件的元素
        #   feature,特征
        #   timeout,超时时间
        #   poll,频率
        #   return,元素
        feature_by, feature_value = feature
        # element = self.driver.find_element(feature_by, feature_value)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, context):
        self.find_element(feature).send_keys(context)

    def clear(self, feature):
        self.find_element(feature).clear()

    def get_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self, message):
        """
        根据部分内容判断toast是否存在
        :param message:部分内容
        :return:是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text, '%s')]" % message
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据部分内容 获取toast上所有内容
        :param message:部分内容
        :return:所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text, '%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现")

    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param direction: 方向
            up从下往上
            down从上往下
            right从左往右
            left从右往左
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = width / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = width / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确, up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找 某个元素的特征，并且点击
        :param feature: 元素的特征
        :param direction:方向
            up从下往上
            down从上往下
            right从左往右
            left从右往左
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    def is_keyword_in_page_source(self, keyword, timeout=10, poll=0.1):
        """
        如果keyword不在page_source中，那么返回True
        如果keyword不在page_source中，那么返回Flase
        :param keyword:关键的字符串
        :param timeout: 超时时间，默认为10秒
        :param poll: 频率，默认为0.1秒
        :return:
        """
        end_time = time.time() + timeout
        while True:
            #   如果结束时间大于当前时间，那么就认为超时了
            if end_time < time.time():
                return False
            if keyword in self.driver.page_source:
                return True

            time.sleep(poll)

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)