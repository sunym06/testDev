import time
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
# caps["appPackage"] = "com.xueqiu.android"
# caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["appPackage"] = "com.greatmall.u41"
caps["appActivity"] = "io.dcloud.PandoraEntry"
caps["autoGrantPermissions"] = "true"
# caps["noReset"] = "true"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
print('finsh init')
print(driver.contexts)
# driver.switch_to.context('WEBVIEW_com.greatmall.u41')
# driver.find_element_by_xpath("//*[@text='立即领取']").click()
for i in range(8):
    time.sleep(3)
    print('ready')
    print(driver.contexts)

print(driver.contexts)