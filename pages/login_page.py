from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        # Wait for username field
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
