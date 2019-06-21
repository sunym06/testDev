class TestSohu(object):

    @classmethod
    def setup_class(cls):
        """ 这是一个class级别的setup函数，它会在这个测试类TestSohu里
        所有test执行之前，被调用一次.
        注意它是一个@classmethod
        """
        print("------ setup before class TestSohu ------")

    @classmethod
    def teardown_class(cls):
         """ 这是一个class级别的teardown函数，它会在这个测试
         类TestSohu里所有test执行完之后，被调用一次.
        注意它是一个@classmethod
        """
         print("------ teardown after class TestSohu ------")

    def setup_method(self, method):
        """ 这是一个method级别的setup函数，它会在这个测试
         类TestSohu里，每一个test执行之前，被调用一次.
        """
        print("--- setup before each method ---")

    def teardown_method(self, method):
        """ 这是一个method级别的teardown函数，它会在这个测试
         类TestSohu里，每一个test执行之后，被调用一次.
        """
        print("--- teardown after each method ---")

    def test_login(self):
        print("sohu login")
        assert True == True

