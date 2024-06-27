from selenium.webdriver.common.by import By


class LoginPage:
    page_title_css = ".page-title h1"
    # assert page_title == "Welcome, Please Sign In!"
    title_xpath = "//strong[text()='Returning Customer']"
    # assert title == "Returning Customer"
    email_id = "Email"
    password_id = "Password"
    remember_id = "RememberMe"
    login_button_xpath = "//button[@class ='button-1 login-button']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def SetPageTitle(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_title_css).text

    def SetTitle(self):
        return self.driver.find_element(By.XPATH, self.title_xpath).text

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def SetRemember(self):
        self.driver.find_element(By.ID, self.remember_id).click()

    def SetLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
