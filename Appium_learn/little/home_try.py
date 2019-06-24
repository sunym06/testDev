# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"
caps["deviceName"] = "deviceName"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_xpath('//*[@text="雪球"]')
el1.click()
el2 = driver.find_element_by_xpath('//*[@text="自选"]')
el2.click()
el3 = driver.find_element_by_xpath('//*[@text="动态"]')
el3.click()
el4 = driver.find_element_by_xpath('//*[@text="行情"]')
el4.click()
el5 = driver.find_element_by_xpath('//*[@text="交易"]')
el5.click()
driver.quit()