import time
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
# caps["appPackage"] = "com.greatmall.u41"
# caps["appActivity"] = "io.dcloud.PandoraEntry"
caps["autoGrantPermissions"] = "true"
caps['chromedriverExecutableDir']=r'C:\Users\ufc_t\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe'
# caps["noReset"] = "true"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
print('finsh init')
print(driver.contexts)
time.sleep(6)
# driver.switch_to.context('WEBVIEW_com.greatmall.u41')
# driver.find_element_by_xpath("//*[@text='立即领取']").click()
driver.find_element_by_xpath("//*[@text='交易']").click()
for i in range(3):
    time.sleep(2)
    driver.find_element_by_xpath("//*[@text='模拟']").click()
    time.sleep(1)
    driver.switch_to.context('WEBVIEW_com.xueqiu.android')
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(@text,创建)]").click()
    print(driver.contexts)
