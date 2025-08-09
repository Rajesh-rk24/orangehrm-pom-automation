import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_list_button = (By.XPATH, "//a[text()='Employee List']")
        self.search_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.result_firstname_cell = (By.XPATH, "(//div[@role='row'])[2]//div[3]")
        self.result_lastname_cell = (By.XPATH, "(//div[@role='row'])[2]//div[4]")

    def verify_employee(self, full_name):
        first_name = full_name.split()[0]

        # Go to Employee List page
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_list_button)
        ).click()

        time.sleep(2)  # wait for page load

        # Search by first name
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_name_input)
        ).clear()
        self.driver.find_element(*self.search_name_input).send_keys(first_name)
        self.driver.find_element(*self.search_button).click()

        # Wait for results
        fname = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_firstname_cell)
        ).text.strip()
        lname = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_lastname_cell)
        ).text.strip()

        found_fullname = f"{fname} {lname}"
        assert found_fullname == full_name, f"Expected {full_name}, but got {found_fullname}"
        print(f"✅ Name Verified: {full_name}")
