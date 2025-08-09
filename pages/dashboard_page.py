from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-name")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def navigate_to_pim(self):
        pim = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.pim_menu)
        )
        ActionChains(self.driver).move_to_element(pim).click().perform()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.user_dropdown)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
