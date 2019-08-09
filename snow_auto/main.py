import time

from selenium import webdriver

url = r'https://wapceshi.paijl.com:10398/'
# 初始化
driver = webdriver.Chrome()
driver.get(url)

# 登录
user = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_css_selector('.layui-btn.layui-btn-fluid')
user.send_keys('admin')
password.send_keys('111111')
login_button.click()

# 商品中心 -商品列表
print('began to wait')
time.sleep(5)
driver.find_element_by_css_selector('.iconfont.icon-shangpinzhongxin').click()
time.sleep(3)
driver.find_element_by_css_selector('.icon-shangpinguanli.iconfont').click()
driver.find_element_by_xpath('//a[text()="商品列表"]').click()

# 创建商品
print('began to wait')
time.sleep(5)
iframes = driver.find_elements_by_tag_name('iframe')
print(len(iframes))
for i in iframes:
    print(i)
# driver.switch_to.frame(1)
driver.find_element_by_id('btnAdd').click()
