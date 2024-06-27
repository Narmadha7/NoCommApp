import os

from selenium import webdriver
from pageObjects.HomeObject import HomePage
from pageObjects.AccObject import AccountPage
from pageObjects.ContObject import ContinuePage
from pageObjects.LoginObject import LoginPage
from pageObjects.RegObject import RegisterPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestNoCommerceApp:
    baseURL = "https://demo.nopcommerce.com/"
    # baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_noCommerce(self, fixture_1):
        self.logger.info("********001_No Commerce Application starts**********")
        self.driver = fixture_1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        # Home Page
        self.comhome = HomePage(self.driver)
        self.comhome.SetRegister()

        # Register Page
        self.comreg = RegisterPage(self.driver)
        self.page_title = self.comreg.SetPageTitle()
        assert self.page_title == "Register"
        self.title = self.comreg.SetTitle()
        assert self.title == "Your Personal Details"
        self.comreg.SetGender()
        self.comreg.SetFirstname("Ram")
        self.comreg.SetLastname("Ki")
        self.email = randomString.random_string_generator() + '@test.com'
        self.comreg.SetEmail(self.email)
        self.comreg.SetPassword("Ram1234")
        self.comreg.SetConPassword("Ram1234")
        self.comreg.SetSubmit()

        # Continue Page
        self.comcon = ContinuePage(self.driver)
        self.success_text = self.comcon.SetSuccessMsg()
        if self.success_text == "Your registration completed":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_noCommerce.png")
            assert False
        self.comcon.SetContinueButton()

        # Account from home screen
        self.comhome.SetAccount()

        # Account Page
        self.comacc = AccountPage(self.driver)
        self.title_msg = self.comacc.SetTitle()
        print(self.title_msg)

        # Logout and login from Home Page
        self.comhome.SetLogout()
        self.comhome.SetLogin()

        # Login Page
        self.comlog = LoginPage(self.driver)
        self.login_page_title = self.comlog.SetPageTitle()
        print(self.login_page_title)
        # assert self.login_page_title == "Welcome, Please Sign In!"
        self.login_title = self.comlog.SetTitle()
        print(self.login_title)
        # assert self.login_title == "Returning Customer"
        self.comlog.SetEmail("Ramkii6543723@test.com")
        self.comlog.SetPassword("Ram1234")
        self.comlog.SetRemember()
        self.comlog.SetLogin()

        self.driver.close()
