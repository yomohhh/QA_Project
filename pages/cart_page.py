from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("[data-test='checkout']")
        self.remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")

    def checkout_page(self):
        self.checkout_button.click()

    def remove_backpack(self):
        self.remove_button.click()