from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_tab = (By.LINK_TEXT, "Employee List")
        self.table_rows = (By.XPATH, "//div[@role='row']")

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.add_employee_button).click()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

    def go_to_employee_list(self):
        self.driver.find_element(*self.employee_list_tab).click()

    def verify_employee_in_list(self, first_name, last_name):
        rows = self.driver.find_elements(*self.table_rows)
        for row in rows:
            if first_name in row.text and last_name in row.text:
                print(f"{first_name} {last_name} - Name Verified")
                return True
        return False
