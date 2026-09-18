import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage


def build_url(base, path):
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
@allure.title("Create an instance of LoginPage class.")
def login_page(driver: WebDriver, base_url) -> LoginPage:
    url = build_url(base_url, "auth/login")
    return LoginPage(driver, url)
