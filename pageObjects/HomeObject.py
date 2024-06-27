from selenium.webdriver.common.by import By


class HomePage:
    # Locators
    register_link = "Register"
    login_link = "Log in"
    account_link = "My account"
    logout_link = "Log out"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods

    def SetRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.register_link).click()

    def SetLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link).click()

    def SetAccount(self):
        return self.driver.find_element(By.LINK_TEXT, self.account_link).click()

    def SetLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link).click()



