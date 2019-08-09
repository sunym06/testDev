import time

from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By


class Testxueqiu():

    driver = WebElement

    @classmethod
    def setup_class(cls):
        print('setup class')

        print('setup class')


        # Testxueqiu.install()

    def setup_method(cls):
        print('setup method')
        cls.install()
        # Testxueqiu.driver = self.restart()
        # Testxueqiu.restart()
        # self.driver.quit()

    def teardown_method(cls):
        print('teardown method')
        cls.driver.quit()
        # self.driver.quite()
        # Testxueqiu.driver.quite()
        # self.driver.quite()
        # self.driver = Testxueqiu.restart()

    def test_login(cls):
        driver = cls.driver
        time.sleep(3)
        driver.find_element_by_id('user_profile_icon')
        driver.find_element_by_id('user_profile_icon').click()
        driver.find_element_by_id('tv_login').click()
        # driver.find_element(*by_phone).click()
        driver.find_element_by_id('tv_login_by_phone_or_others').click()
        driver.find_element_by_id('register_phone_number').send_keys('15801287634')
        # time.sleep(2)
        # driver.find_element_by_id("register_code").send_keys("3456")
        # driver.find_element_by_id('button_next').click()
        print('method1')

    def test_fda(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_id('user_profile_icon')

        driver.find_element_by_id('user_profile_icon').click()
        driver.find_element_by_id('tv_login').click()
        driver.find_element_by_id('tv_login_by_phone_or_others').click()
        driver.find_element_by_id('register_phone_number').send_keys('1580111111')
        # time.sleep(2)
        # driver.find_element_by_id("register_code").send_keys("3456")
        # driver.find_element_by_id('button_next').click()
        print('method1')

    @classmethod
    def install(cls) ->WebElement:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def restart(cls) ->WebElement:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(15)
        return cls.driver

