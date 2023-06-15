from selenium.webdriver.common.by import By

from web_tests.helpers.project_helpers import get_base_url
from web_tests.pages.base_page import BasePage
from web_tests.pages.inventory_page import InventoryPage


class LoginPage(BasePage):

    USERNAME_INPUT_FIELD_LOCATOR = (By.ID, 'user-name')
    PASSWORD_INPUT_FIELD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')
    ERROR_MESSAGE_LOCATOR = (By.TAG_NAME, 'h3')
    USERNAME_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='user-name']/following-sibling::*[local-name()='svg']")
    PASSWORD_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='password']/following-sibling::*[local-name()='svg']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def username_input_field(self):
        return self.element(LoginPage.USERNAME_INPUT_FIELD_LOCATOR)

    @property
    def password_input_field(self):
        return self.element(LoginPage.PASSWORD_INPUT_FIELD_LOCATOR)

    @property
    def login_button(self):
        return self.element(LoginPage.LOGIN_BUTTON_LOCATOR)

    @property
    def error_message(self):
        return self.element(LoginPage.ERROR_MESSAGE_LOCATOR)

    @property
    def username_error_marker(self):
        return self.element(LoginPage.USERNAME_ERROR_MARKER_LOCATOR)

    @property
    def password_error_marker(self):
        return self.element(LoginPage.PASSWORD_ERROR_MARKER_LOCATOR)

    def navigate(self):
        self.driver.get(get_base_url())

    def enter_username(self, username):
        self.username_input_field.send_keys(username)
        return self

    def enter_password(self, password):
        self.password_input_field.send_keys(password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def fill_login_form(self, user):
        self.enter_username(user.username)
        self.enter_password(user.password)
        self.click_login_button()

    def successful_login(self, user):
        self.fill_login_form(user)
        return InventoryPage(self.driver)

    def unsuccessful_login(self, user):
        self.fill_login_form(user)
        return self
