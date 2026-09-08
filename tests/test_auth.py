import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# 1. Задаем параметры: имя пользователя, пароль, и что мы ищем в результате (URL или текст ошибки)
@pytest.mark.parametrize("username, password, expected_result, is_positive", [
    # Позитивный кейс (is_positive = True)
    ("standard_user", "secret_sauce", "inventory.html", True),

    # Негативные кейсы (is_positive = False)
    ("standard_user", "wrong_password", "do not match", False),
    ("", "secret_sauce", "Username is required", False),
    ("standard_user", "", "Password is required", False)
])
def test_login_flow(page, username, password, expected_result, is_positive):
    login_page = LoginPage(page)


    login_page.open_url("https://saucedemo.com")

    login_page.login_to_shop(username, password)

    if is_positive:

        assert expected_result in page.url
    else:

        assert login_page.error_message.is_visible()
        assert expected_result in login_page.error_message.text_content()


def test_cart_workflow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_url("https://saucedemo.com")
    login_page.login_to_shop("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.checkout_button.is_visible()


def test_remove_item_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_url("https://saucedemo.com")
    login_page.login_to_shop("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page.remove_button.click()

    assert inventory_page.cart_badge.is_hidden()