from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
#from web_tests.pages.inventory_page import InventoryPage
#import web_tests.pages.inventory_page
import web_tests.pages.inventory_page as inventory_page

class ItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    BACK_BUTTON = (By.ID, 'back-to-products')

    @property
    def back_button(self):
        return self.element(ItemPage.BACK_BUTTON)

    def navigate_back(self):
        self.back_button.click()
        #return InventoryPage(self.driver)
        #return web_tests.pages.inventory_page.InventoryPage(self.driver)
        return inventory_page.InventoryPage(self.driver)

    def is_displayed(self):
        return self.back_button.is_displayed()

