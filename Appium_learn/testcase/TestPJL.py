import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class TestPJL(object):
    driver = WebDriver

    @classmethod
    def installPJL(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.great_mall.u4"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        caps["autoGrantPermissions"] = "true"
        # caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def setup_class(cls):
        print('setup class')
        cls.driver = TestPJL.installPJL()
        cls.driver()
        cls.Fri_open()

    def setup_method(self):
        print('setup method')
        self.driver.find_element_by_xpath('//*[@text="我的"]')

    def teardown_method(self):
        print('teardown method')

    def testLogin(self):
        self.driver = TestPJL.installPJL()

    def direct(self):
        rect = self.driver.get_window_size()
        width = rect["width"]
        height = rect["height"]
        self.driver.swipe(width * 0.8, height * 0.5, width*0.3, height * 0.6)
        time.sleep(2)
        self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.6)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*").click()

    def Fri_open(self):
        self.driver.find_element_by_id('goto').click()

