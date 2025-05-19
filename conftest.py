from playwright.sync_api import sync_playwright, Browser, Page, BrowserContext
import pytest


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()