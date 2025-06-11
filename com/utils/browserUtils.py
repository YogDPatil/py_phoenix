

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtils:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def enterTetx(self, locator,text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def clickOn(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def currentPageUrl(self,endpoint):
        self.wait.until(expected_conditions.url_contains(endpoint))
        return self.driver.current_url