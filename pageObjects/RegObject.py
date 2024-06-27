from selenium.webdriver.common.by import By


class RegisterPage:
    # Locators
    page_title_css = ".page-title h1"
    title_xpath = "//strong[text()='Your Personal Details']"
    gender_css = "#gender-male"
    firstname_css = "#FirstName"
    lastname_css = "#LastName"
    email_id = "Email"
    password_id = "Password"
    conpass_id = "ConfirmPassword"
    register_button_id = "register-button"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def SetPageTitle(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_title_css).text

    def SetTitle(self):
        return self.driver.find_element(By.XPATH, self.title_xpath).text

    def SetGender(self):
        self.driver.find_element(By.CSS_SELECTOR, self.gender_css).click()

    def SetFirstname(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, self.firstname_css).send_keys(firstname)

    def SetLastname(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, self.lastname_css).send_keys(lastname)

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def SetConPassword(self, con_password):
        self.driver.find_element(By.ID, self.conpass_id).send_keys(con_password)

    def SetSubmit(self):
        self.driver.find_element(By.ID, self.register_button_id).click()

