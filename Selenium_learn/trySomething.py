from selenium import webdriver

# 验证群里所说minimize_window函数
def miniWin():
    url = r'http://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.minimize_window()