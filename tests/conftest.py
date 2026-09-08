import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        # channel="chrome" перенаправляет Playwright на твой установленный в Windows Chrome
        browser = p.chromium.launch(
            headless=False,  # Видим браузер глазами

        )
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
