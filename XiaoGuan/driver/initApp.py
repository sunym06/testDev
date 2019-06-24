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

        self.driver = self.initApp() #之前方法内函数都报没有self,因为没有定义driver？
        self.driver.find_element_by_xpath('//*').click()
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        print(width)
        time.sleep(3)
        self.driver.swipe(0.8*width, 0.5*height, 0.2*width, 0.5*height)
        time.sleep(2)
        self.driver.swipe(0.8*width, 0.5*height, 0.2*width, 0.5*height)
        self.driver.find_element_by_xpath('//*').click()
        self.driver.find_element_by_id('goto').click()
        self.driver.back()


a = initApp()
a.openApp()
a.login()
