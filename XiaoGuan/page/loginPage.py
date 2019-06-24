import time

from XiaoGuan.driver import initApp


class loginPage(object):

    def __init__(self):
        self.driver = initApp
        print('a')

    @classmethod
    def getDrive(cls):
        cls.driver = initApp3
    def login(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@text="我的"]').click()
        # self.driver.find_element_by_xpath('//*[@text="登录/注册"]').click()
        driver.find_element_by_xpath('//*[contains(@text,"登录")]').click()
        driver.find_element_by_id('phone').send_keys('15801287634')
        driver.find_element_by_id('password').send_keys('aaa12345')
        driver.find_element_by_id('login').click()

a = loginPage.login()