import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720}
    }


@pytest.fixture
def logged_in_page(page):
    """Open SauceDemo and log in as standard_user. Returns the same page."""
    login_page = LoginPage(page)
    login_page.open_url("https://saucedemo.com")
    login_page.login_to_shop("standard_user", "secret_sauce")
    return page
