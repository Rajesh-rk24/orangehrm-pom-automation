import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage

@pytest.mark.parametrize("employees", [[("John", "Doe"), ("Jane", "Smith"), ("Mike", "Brown")]])
def test_orangehrm_flow(driver, employees):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    add_employee_page = AddEmployeePage(driver)
    employee_list_page = EmployeeListPage(driver)

    # Step 1: Login
    login_page.login("Admin", "admin123")

    # Step 2: Navigate to PIM
    dashboard_page.navigate_to_pim()

    # Step 3: Add Employees
    for first, last in employees:
        add_employee_page.add_employee(first, last)
        dashboard_page.navigate_to_pim()

    # Step 4: Verify Employees
    for first, last in employees:
        full_name = f"{first} {last}"
        employee_list_page.verify_employee(full_name)

    # Step 5: Logout
    dashboard_page.logout()
