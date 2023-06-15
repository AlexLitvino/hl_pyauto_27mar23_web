import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from web_tests.helpers.project_helpers import get_browser_name
from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    browser_name = get_browser_name()
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unknown browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    yield login_page


@pytest.fixture(scope='session')
def valid_user():
    return User('standard_user', 'secret_sauce')


@pytest.fixture(scope='session')
def locked_out_user():
    return User('locked_out_user', 'secret_sauce')
