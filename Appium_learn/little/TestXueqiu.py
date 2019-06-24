import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiu(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print('setup class')
        cls.driver = cls.init_appium()

    def setup_method(self):
        print('setup method')
        # self.driver = TestXueqiu.restart_appium()
        TestXueqiu.driver = self.restart_appium()

    def teardown_method(self):
        print('teardown method')
        TestXueqiu.driver.quit()

    # def test_login(self):
    #
    #     TestXueqiu.driver.find_element_by_id("user_profile_icon").click()
    #     TestXueqiu.driver.find_element_by_id("tv_login").click()
    #     TestXueqiu.driver.find_element_by_id("tv_login_by_phone_or_others").click()
    #     # driver.find_element_by_id("register_phone_number").send_keys("15801287634")
    #     # driver.find_element_by_id("register_code").send_keys("1234")
    #     # driver.find_element_by_id("button_next").click()
    #     # driver.find_element_by_id("md_content").click()
    #     # driver.find_element_by_id("md_buttonDefaultPositive").click()
    #     # driver.find_element_by_id("iv_action_back").click()
    #
    #     # time.sleep(3)

    # def test_tech(self):
    #     # TestXueqiu.driver.find_element_by_id("user_profile_icon").click()
    #
    #     TestXueqiu.driver.find_element_by_xpath('//*[@text="科创板"]').click()
    #     TestXueqiu.driver.find_element_by_xpath('//*[@text="房产"]').click()

    def getSize(self):
        rect = TestXueqiu.driver.get_window_size()
        return rect

    def test_swipe(self):
        TestXueqiu.driver.find_element_by_xpath('//*[@text="推荐"]')
        width = self.getSize()["width"]
        height = self.getSize()["height"]
        time.sleep(5)
        for i in range(5):
            # TestXueqiu.driver.swipe(width * 0.8, height * 0.8, width * 0.2, height * 0.2)
            action = TouchAction(TestXueqiu.driver)
            action.press(x=width * 0.8, y=height * 0.8).move_to(x=width * 0.2, y=height * 0.2).release().perform()
            time.sleep(2)

    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["deviceName"] = "127.0.0.1:7555"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = 'true'
        caps["deviceName"] = "127.0.0.1:7555"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
