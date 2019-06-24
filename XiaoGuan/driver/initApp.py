import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class initApp():

    driver = WebDriver
    @classmethod
    def initApp(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.great_mall.u4"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        caps["autoGrantPermissions"] = "true"
        # caps["noReset"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    def openApp(self):
        time.sleep(3)
        self.driver = self.initApp() #之前方法内函数都报没有self,因为没有定义driver？
        self.driver.find_element_by_xpath('//*').click()
        self.driver.swipe(1000,800,200,800)
        time.sleep(1)
        self.driver.swipe(1000,800,200,800)
        self.driver.find_element_by_xpath('//*').click()
        self.driver.find_element_by_id('goto').click()
        self.driver.back()




# a = initApp()
# a.openApp()
# a.login()