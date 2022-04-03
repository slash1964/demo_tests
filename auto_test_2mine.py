import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def setUp (self):
        pass

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://www.printfriendly.com/users/sign_in')
        title = driver.title
        print(title)
        assert 'PrintFriendly & PDF' == title

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://www.printfriendly.com/api/instructions')
        title = driver.title
        print(title)
        assert 'PrintFriendly & PDF API - Instructions' == title

    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('https://chrome.google.com/webstore/detail/print-friendly-pdf/ohlencieiipommannpdfcmfdpjjmeolj')
        title = driver.title
        print(title)
        assert 'Zanim przejdziesz dalej' == title

    def test_demo_transfer(self):
        driver = self.driver
        driver.get('http://blog.printfriendly.com/2012/06/print-friendly-speaks-your-language.html')
        title = driver.title
        print(title)
        assert 'Print Friendly: Print Friendly Speaks Your Language' == title

    def tearDown(self):
        pass
    @classmethod
    def tearDownClass (self):
        self.driver.quit()



