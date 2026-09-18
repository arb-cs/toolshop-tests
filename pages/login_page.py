import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit']")
    EMAIL_ERROR = (By.CSS_SELECTOR, "[data-test='email-error']")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "[data-test='password-error']")
    LOGIN_ERROR = (By.CLASS_NAME, "help-block")

    @allure.step("Enter your email address.")
    def enter_email(self, email: str):
        self.actions.fill(self.EMAIL_INPUT, email)

    @allure.step("Enter your password.")
    def enter_password(self, password: str):
        self.actions.fill(self.PASSWORD_INPUT, password)

    @allure.step("Click on the login button.")
    def click_login_button(self):
        self.actions.click(self.LOGIN_BUTTON)

    @allure.step(
        "Check the error message that appears if an error occurs when filling in the ‘Email address’ field."
    )
    def check_email_error_text(self, text: str) -> bool:
        return self.actions.should_have_text(self.EMAIL_ERROR, text)

    @allure.step(
        "Check the error message that appears if an error occurs when filling in the ‘Password’ field."
    )
    def check_password_error_text(self, text: str) -> bool:
        return self.actions.should_have_text(self.PASSWORD_ERROR, text)

    @allure.step(
        "Check the error message that appears if a user clicks login button with invalid data."
    )
    def check_login_error_text(self, text: str) -> bool:
        return self.actions.should_have_text(self.LOGIN_ERROR, text)
