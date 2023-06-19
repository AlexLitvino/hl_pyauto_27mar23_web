"""First iteration of tests"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pytest

# TODO: specify path to chromedriver here
path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'


# def test_navigation_back():
#     """
#     1. Navigate to base url
#     2. Enter 'standard_user' as username
#     3. Enter 'secret_sauce' as password
#     4. Click Login button.
#     Verify that Inventory page is displayed
#     5. Select first item on Inventory page.
#     Verify that page for the first item is displayed.
#     6. Click Back button.
#     Verify that Inventory page is displayed
#     """
#     driver = Chrome(service=Service(path))
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     driver.get('https://www.saucedemo.com/')
#
#     valid_user = 'standard_user'
#     valid_password = 'secret_sauce'
#
#     username_input_field = driver.find_element(By.ID, 'user-name')
#     password_input_field = driver.find_element(By.ID, 'password')
#     login_button = driver.find_element(By.ID, 'login-button')
#
#     username_input_field.send_keys(valid_user)
#     password_input_field.send_keys(valid_password)
#     login_button.click()
#
#     inventory_container = driver.find_element(By.ID, 'inventory_container')
#     assert inventory_container.is_displayed()
#
#     item_1 = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")[0]
#     item_1.click()
#     time.sleep(1)
#     # on item#1 page
#     back_button = driver.find_element(By.ID, 'back-to-products')
#     assert back_button.is_displayed()
#
#     back_button.click()
#     time.sleep(1)
#     inventory_container = driver.find_element(By.ID, 'inventory_container')
#     assert inventory_container.is_displayed()
#
#     driver.quit()


def test_navigation_back(login_page, valid_user):
    """
    1. Navigate Inventory page
    2. Select first item on Inventory page.
    Verify that page for the first item is displayed.
    3. Click Back button.
    Verify that Inventory page is displayed
    """
    inventory_page = login_page.successful_login(valid_user)
    assert inventory_page.is_page_displayed()

    first_item_page = inventory_page.navigate_to_item(1)

    assert first_item_page.is_displayed()

    first_item_page.navigate_back()

    assert inventory_page.is_page_displayed
