from playwright.sync_api import Page
from pages.buttons_page import ButtonsPage


def test_simple_button_tab(page: Page) -> None:
    button_page = ButtonsPage(page)
    button_page.open_main_page()
    button_page.open_buttons_page()
    button_page.click_submit_button()
    button_page.check_result_message_is_visible()


def test_looks_like_a_button(page: Page) -> None:
    button_page = ButtonsPage(page)
    button_page.open_main_page()
    button_page.open_buttons_page()
    button_page.open_fake_button_tab()
    button_page.click_fake_button()
    button_page.check_result_message_is_visible()


def test_click_disabled_button(page: Page) -> None:
    button_page = ButtonsPage(page)
    button_page.open_main_page()
    button_page.open_buttons_page()
    button_page.open_disable_button_tab()
    button_page.make_button_enabled()
    button_page.click_submit_button()
    button_page.check_result_message_is_visible()

