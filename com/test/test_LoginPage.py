import pytest

from com.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_validateLogin(self):
        loginPage = LoginPage(self.driver)
        assert "dashboard" in loginPage.doLogin().dashboardPageUrl()
        print("TEST CASE DONE")
