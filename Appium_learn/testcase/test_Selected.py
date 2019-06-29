import pytest

from Appium_learn.driver.AndroidClient import AndroidClient
from Appium_learn.page.mainPage import mainPage


class Test_Selected(object):


    @classmethod
    def setup_class(cls):
        print('setup class')
        cls.main = mainPage()

    def setup_method(self):
        print('setup method')

    def test_price(self):
        assert self.main.gotoSelected().getPrice("拼多多") == 20.63

    def test_price2(self):
        assert self.main.gotoSelected().getPrice("中国平安") == 88.61

    def teardown_method(self):
        print('teardown method')


