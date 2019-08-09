import time
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.greatmall.u41"
caps["appActivity"] = "io.dcloud.PandoraEntry"
caps["autoGrantPermissions"] = "true"
# caps['chromedriverExecutableDir']=r'C:\Users\ufc_t\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe'
# caps["noReset"] = "true"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
rect = driver.get_window_rect()
x = rect['width']
y = rect['height']
time.sleep(30)
for i in range (5):
    driver.swipe(0.8*x, 0.6*y ,0.2*x, 0.6*y)
    time.sleep(3)

driver.find_element_by_xpath('//*').click()

time.sleep(15)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.greatmall.u41')
driver.find_element_by_xpath('//*[@text="立即领取"]').click()
# # print(driver.window_handles)
# time.sleep(20)
# driver.find_element_by_xpath('//*[@text="立即领取"]').click()
time.sleep(5)