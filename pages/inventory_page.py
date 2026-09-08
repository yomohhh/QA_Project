from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Ищем кнопку добавления первого товара (рюкзака) по ее ID на сайте
        self.add_backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        # Ищем иконку корзины в шапке (красный кружок с цифрой количества товаров)
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def go_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()
