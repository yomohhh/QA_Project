import re
import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect


@allure.feature("Authentication")
@allure.title("Login with different credentials")
@pytest.mark.parametrize("username, password, expected_result, is_positive", [
    ("standard_user", "secret_sauce", "inventory.html", True),
    ("standard_user", "wrong_password", "do not match", False),
    ("", "secret_sauce", "Username is required", False),
    ("standard_user", "", "Password is required", False)
])
def test_login_flow(page, username, password, expected_result, is_positive):
    login_page = LoginPage(page)

    with allure.step("Open the SauceDemo login page"):
        login_page.open_url("https://saucedemo.com")

    with allure.step(f"Log in with username '{username}'"):
        login_page.login_to_shop(username, password)

    if is_positive:
        with allure.step("Check that the inventory page is opened"):
            expect(page).to_have_url(re.compile(expected_result))
    else:
        with allure.step(f"Check that the error contains '{expected_result}'"):
            expect(login_page.error_message).to_be_visible()
            expect(login_page.error_message).to_contain_text(expected_result)


@allure.feature("Cart")
@allure.title("Add a product to the cart and open the cart")
def test_cart_workflow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    with allure.step("Add the Sauce Labs Backpack to the cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Open the cart"):
        inventory_page.go_to_cart()

    with allure.step("Check that the checkout button is visible"):
        expect(cart_page.checkout_button).to_be_visible()


@allure.feature("Cart")
@allure.title("Remove a product from the cart")
def test_remove_item_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    with allure.step("Add the Sauce Labs Backpack to the cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Open the cart"):
        inventory_page.go_to_cart()

    with allure.step("Click Remove on the item"):
        cart_page.remove_button.click()

    with allure.step("Check that the cart badge is hidden"):
        expect(inventory_page.cart_badge).to_be_hidden()
