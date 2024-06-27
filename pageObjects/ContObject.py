from selenium.webdriver.common.by import By


class ContinuePage:
    # Locators
    success_text_css = ".result"
    continue_button_xpath = "//a[@class ='button-1 register-continue-button']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods

    def SetSuccessMsg(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.success_text_css).text
        except:
            None

    def SetContinueButton(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
