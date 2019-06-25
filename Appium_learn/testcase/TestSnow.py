import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class TestSnow(object):

    driver = WebDriver

    @classmethod
    def install_app(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)
        return driver

    @classmethod
    def setup_class(cls):
        print('setup class')
        cls.driver = TestSnow.install_app()
        cls.driver.find_element_by_id('user_profile_icon').click()

    def setup_method(self):
        print('setup method')
        driver = TestSnow.driver
        # driver.find_element_by_id('user_profile_icon').click()
        driver.find_element_by_id('tv_login').click()

    def test_login_Phone(self):
        # driver = TestSnow.driver
        self.driver.find_element_by_id('tv_login_by_phone_or_others').click()
        self.driver.find_element_by_id('register_phone_number').send_keys('1580111111')
        self.driver.find_element_by_xpath('//*[contains(@text,"四位")]').send_keys('1234')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="登录"]').click() #密码
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()


    def test_login_wechat(self):
        # TestSnow.driver = TestSnow.install_app()
        self.driver.find_element_by_xpath('//*[contains(@text,"微信")]').click()

    def test_login_mail(self):
        # driver = TestSnow.install_app()
        self.driver.find_element_by_id('tv_login_by_phone_or_others').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"邮箱")]').click()

    def test_swipe(self):
        rect = self.driver.get_window_size()
        width = rect["width"]
        height = rect["height"]
        self.driver.swipe(width * 0.4, height * 0.8, width*0.5, height * 0.6)
        self.driver.swipe(width * 0.5, height * 0.6, width*0.4, height * 0.8)
        self.driver.swipe(width * 0.4, height * 0.8, width*0.5, height * 0.6)



    def teardown_method(self):
        # driver = TestSnow.install_app()
        self.driver.back()