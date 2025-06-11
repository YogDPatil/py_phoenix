import time

import pytest
from selenium import webdriver

from com.pages.login_page import LoginPage


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://phoenix.techwithjatin.com/sign-in")
    request.cls.driver=driver
    yield
    time.sleep(3)
    # driver.quit()






