import allure
from selenium.webdriver.remote.webdriver import WebDriver

from core.driver_actions import DriverActions


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.url = url
        self.driver = driver
        self.actions = DriverActions(driver)

    @allure.step("Open the page.")
    def open(self) -> None:
        if not self.url:
            raise ValueError(f"{self.__class__.__name__} has no URL defined.")

        self.driver.get(self.url)

    @allure.step("Reload the page.")
    def reload(self) -> None:
        self.driver.refresh()
