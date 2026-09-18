from pathlib import Path

from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DriverActions:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator: tuple[str, str], timeout: int | None = None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_invisible(self, locator: tuple[str, str]) -> bool | WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_all(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator: tuple[str, str], text: str) -> None:
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find_visible(locator).text.strip()

    def should_have_text(self, locator: tuple[str, str], text: str) -> bool:
        return self.get_text(locator) == text

    def is_displayed(self, locator: tuple[str, str], timeout: int = 0) -> bool:
        try:
            return self.find(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    def count_elements(self, locator: tuple[str, str]) -> int:
        elements = self.find_all(locator)
        return len(elements)

    def scroll_into_view(self, locator: tuple[str, str]) -> WebElement:
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def upload_file(self, locator, relative_path: str) -> None:
        absolute_path = str(Path(relative_path).resolve())
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(absolute_path)
