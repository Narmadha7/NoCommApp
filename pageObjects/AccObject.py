from selenium.webdriver.common.by import By


class AccountPage:
    # Locators
    title_page_xpath = "//h1[text()='My account - Customer info']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def SetTitle(self):
        return self.driver.find_element(By.XPATH, self.title_page_xpath).text






