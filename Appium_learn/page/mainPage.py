import time

from Appium_learn.driver.AndroidClient import AndroidClient
from Appium_learn.page.SelectedPage import SelectedPage
from Appium_learn.page.LoginPage import LoginPage


class mainPage():

    def __init__(self):
        AndroidClient.restart_app()
        # pass
    def gotoSelected(self):
        time.sleep(1)

        AndroidClient.driver.find_element_by_xpath('//*[@text="自选"]')
        time.sleep(1)
        AndroidClient.driver.find_element_by_xpath('//*[@text="自选"]').click()
        return SelectedPage()

    def gotoLogin(self):
        AndroidClient.driver.find_element_by_xpath('//*[@text="自选"]')
        return LoginPage()

