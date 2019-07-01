from Appium_learn.driver.AndroidClient import AndroidClient


class SelectedPage(object):

    def getPrice(self, name) -> float:
        price = AndroidClient.driver.find_element_by_xpath\
            ('//*[@text="{}" and contains(@resource-id,"stockName")]/../../..'
                                         '//*[contains(@resource-id,"currentPrice")]'.format(name)).text
        return float(price)


