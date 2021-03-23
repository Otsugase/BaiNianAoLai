from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        #   根据特征，找元素
        #   feature,特征
        #   timeout,超时时间
        #   poll,频率
        #   return,元素
        feature_by, feature_value = feature
        # element = self.driver.find_element(feature_by, feature_value)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1):
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

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)