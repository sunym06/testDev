from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):

    driver = WebDriver
    @classmethod
    def install_app(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

