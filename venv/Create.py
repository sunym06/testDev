import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

url = r'http://124.193.68.233:8888/'

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(6)

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('111111')
driver.find_element_by_xpath('//button').click()
driver.maximize_window()
time.sleep(2)
# driver.find_element_by_xpath('//*[@id="navBtn"]/li[2]/text()').click()
driver.find_element_by_css_selector('.iconfont.icon-yunyingzhongxin').click()
driver.find_element_by_css_selector('.icon-jingpaiguanli.iconfont').click()
driver.find_element_by_xpath('//*[@id="217"]/li[1]/dl/dd[1]/a').click()
iframe_main = driver.find_element(By.CLASS_NAME, "admin-iframe")
time.sleep(1)
driver.switch_to.frame(iframe_main)
time.sleep(1)
driver.find_element_by_id('activityNo').send_keys('123')
driver.find_element_by_id('btnAdd').click()
time.sleep(6)
# print(driver.page_source)
print(len(driver.window_handles))
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     time.sleep(6)
driver.switch_to_frame()
driver.find_element_by_id('activityName').click()

driver.switch_to.window()
# iframe_alert = driver.find_element_by_id('layui-layer-iframe1')
# time.sleep(6)
# driver.switch_to.frame(iframe_alert)
print(driver.window_handles)
# iframe_alert = driver.find_element(By.ID, 'layui-layer-iframe2')
driver.switch_to.frame(iframe_alert)
time.sleep(3)
driver.switch_to.alert()
driver.find_element_by_id('activityName').click()

driver.find_element_by_id('btnAdd').click()

time.sleep(3)

driver.find_element_by_id('activityName').send_keys('ttt')
# driver.find_element_by_id('activityName').send_keys('123')