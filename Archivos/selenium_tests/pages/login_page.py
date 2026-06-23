from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.title = (By.CLASS_NAME, "title")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def set_username(self, username):
            self.driver.find_element(*self.username_field).send_keys(username)
        
    def set_password(self, password):
            self.driver.find_element(*self.password_field).send_keys(password)
        
    def click_login(self):
            self.driver.find_element(*self.login_button).click()
        
    def get_title(self):
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.title)).text
        
    def get_error_message(self):
            return self.driver.find_element(*self.error_message).text