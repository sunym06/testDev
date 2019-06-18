# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.common.MainActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(15)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/iv_action_back")
el4.click()

driver.quit()