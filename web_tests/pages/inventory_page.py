from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
#from web_tests.pages.item_page import ItemPage
#import web_tests.pages.item_page
import web_tests.pages.item_page as item_page

class InventoryPage(BasePage):

    INVENTORY_CONTAINER_LOCATOR = (By.ID, 'inventory_container')
    # ITEMS_LINKS = (By.XPATH, "//div[@class='inventory_item_name']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def inventory_container(self):
        return self.element(InventoryPage.INVENTORY_CONTAINER_LOCATOR)

    @property
    def item_link(self):
        def get_link(number):
            return self.driver.find_element(By.XPATH, f"//div[@class='inventory_item'][{number}]/descendant::a")
        return get_link

    def navigate_to_item(self, number):
        self.item_link(number).click()
        #return ItemPage(self.driver)
        #return web_tests.pages.item_page.ItemPage(self.driver)
        return item_page.ItemPage(self.driver)

    def is_page_displayed(self):
        return self.inventory_container.is_displayed()
