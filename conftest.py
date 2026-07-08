import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=True
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()