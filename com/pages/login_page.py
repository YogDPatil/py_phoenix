from selenium.webdriver.common.by import By

from com.pages.dashboardPage import DashboardPage
from com.utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    username_field_locator = (By.ID,"username")
    password_field_locator = (By.ID, "password")
    sign_in_button_locator = (By.XPATH, "//span[contains(text(),'Sign in')]/ancestor::button")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def doLogin(self):
        self.enterTetx(self.username_field_locator,"iamfd")
        self.enterTetx(self.password_field_locator, "password")
        self.clickOn(self.sign_in_button_locator)
        return DashboardPage(self.driver)


