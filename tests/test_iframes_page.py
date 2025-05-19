from playwright.sync_api import Page
from pages.iframes_page import IframesPage


def test_iframes_page(page: Page) -> None:
    iframe_page = IframesPage(page)
    iframe_page.open_main_page()
    iframe_page.open_single_ui_element()
    iframe_page.open_iframes_page()
    iframe_page.open_menu_in_frame()
    iframe_page.nav_bar_menu_is_visible()
