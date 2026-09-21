import time

import allure

from pages.login_page import LoginPage


@allure.feature("Authorization")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(
    "Checking that authentication is not carried out using incorrect data."
)
def test_invalid_login_password(login_page: LoginPage):
    login_page.open()
    login_page.enter_email("customer@practicesoftwaretesting.com")
    time.sleep(1)
    login_page.enter_password("Test")
    time.sleep(1)
    login_page.click_login_button()
    time.sleep(1)

    assert login_page.check_login_error_text("Invalid email or password")


@allure.feature("Authorization")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Checking that short passwords are not allowed.")
def test_invalid_password_length(login_page: LoginPage):
    login_page.open()
    login_page.enter_email("customer@practicesoftwaretesting.com")
    login_page.enter_password("T")
    login_page.click_login_button()

    assert login_page.check_password_error_text("Password length is invalid")


@allure.feature("Authorization")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("An error occurs when a user does not fill in the password field.")
def test_empty_password_field(login_page: LoginPage):
    login_page.open()
    login_page.enter_email("customer@practicesoftwaretesting.com")
    login_page.click_login_button()

    assert login_page.check_password_error_text("Password is required")


@allure.feature("Authorization")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "An error is displayed when a user enters an email address in an incorrect format."
)
def test_invalid_email(login_page: LoginPage):
    login_page.open()
    login_page.enter_email("customer")
    login_page.click_login_button()

    assert login_page.check_email_error_text("Email format is invalid")


@allure.feature("Authorization")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Errors are displayed when a user does not enter their email and password."
)
def test_empty_fields(login_page: LoginPage):
    login_page.open()
    login_page.click_login_button()

    assert login_page.check_email_error_text("Email is required")
    assert login_page.check_password_error_text("Password is required")
