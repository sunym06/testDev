from Appium_learn.page.mainPage import mainPage


class TestLogin():

    @classmethod
    def setup_class(cls):
        print('setup class')
        mainPage.goLogin()

    def setup_method(self):
        print('setup method')

    def testLogin(self):
        print('test')
