from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER_LOCATOR = (By.ID, 'inventory_container')
    # ITEMS_LINKS = (By.XPATH, "//div[@class='inventory_item_name']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def inventory_container(self):
        return self.element(InventoryPage.INVENTORY_CONTAINER_LOCATOR)

    def is_page_displayed(self):
        return self.inventory_container.is_displayed()
