# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By


class App(object):
    login_icon = (By.ID, 'user_profile_icon')
    click_login_bt = (By.ID, 'tv_login')
    by_phone = (By.ID, 'tv_login_by_phone_or_others')
    phone = (By.ID, 'register_phone_number')
    pwd = (By.ID, 'register_code')
    login_bt = (By.ID, 'button_next')
    sendCode = (By.ID, 'register_code_text')
    driver=WebElement
    def installApp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*').click()
        driver.find_element(self.login_icon)
        return driver
a = App()
time.sleep(8)
d = a.installApp()


