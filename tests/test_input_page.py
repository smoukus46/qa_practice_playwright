from playwright.sync_api import Page
from pages.input_page import InputPage


def test_text_input(page: Page) -> None:
    input_page = InputPage(page)
    input_page.open_main_page()
    input_page.open_input_page()
    input_page.fill_text_input()
    input_page.press_enter()
    input_page.result_field_have_text('HelloWorld')


def test_email_field(page: Page) -> None:
    input_page = InputPage(page)
    input_page.open_main_page()
    input_page.open_input_page()
    input_page.open_email_tab()
    input_page.fill_email_input()
    input_page.press_enter()
    input_page.result_field_have_text('BalerinaCapuchina@yandex.ru')


def test_password_field(page: Page) -> None:
    input_page = InputPage(page)
    input_page.open_main_page()
    input_page.open_input_page()
    input_page.open_password_tab()
    input_page.fill_password_input()
    input_page.press_enter()
    input_page.result_field_have_text('96357415Nn!')
