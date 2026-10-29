import allure
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

    login_page = LoginPage(page)
    login_page.open_url("https://saucedemo.com")
    login_page.login_to_shop("standard_user", "secret_sauce")
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page is not None:
            try:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name="failure screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as error:
                print(f"Could not take screenshot: {error}")
