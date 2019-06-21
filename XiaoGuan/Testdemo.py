import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class Testdemo():

    driver = WebDriver
    @classmethod
    def installApp(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.great_mall.u4"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver


    @classmethod
    def setup_class(cls):

        print('setup class')
        cls.driver= cls.installApp()
        # time.sleep(5)
        # cls.swip()
        cls.goLog()
        # cls.driver.find_element_by_xpath('//*[@text="我的"]').click()
        # cls.driver.find_element_by_xpath('//*[@text="登录/注册"]').click()

    def setup_method(self):
        print('setup method')



    def teardown_method(self):
        print('teardown method')
        self.quitLog()
    def test_login(self,ph,pwd):
        self.driver.find_element_by_xpath('//*[@text="请输入手机号"]').send_keys('15801287634')
        self.driver.find_element_by_xpath('//*[contains（@text，"请输入密码")]').send_keys('aaa12345')
        self.driver.find_element_by_xpath('//*[@text="立即登录"]').click()

    def swip(self):
        time.sleep(2)
        # self.driver.swipe(1000,20,200,20)
        self.driver.swipe(1000,820,200,820)
        time.sleep(2)
        self.driver.swipe(1000, 820, 200, 820)
        time.sleep(2)
        self.driver.swipe(1000, 820, 200, 820)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*').click()


    def goLog(self):

        self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        self.find_element_by_xpath('//*[@text="登录/注册"]').click()

    def quitLog(self):
        self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        self.driver.find_element_by_id('personal_data').click()
        self.driver.find_element_by_xpath('//*[@text="退出登录"]').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        self.driver.find_element_by_class_name('android.view.View').click()



