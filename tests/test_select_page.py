from playwright.sync_api import Page
from pages.select_page import SelectPage


def test_single_select(page: Page) -> None:
    select_page = SelectPage(page)
    select_page.open_main_page()
    select_page.open_select_page()
    select_page.select_python_language()
    select_page.click_submit_btn()
    select_page.check_result_is_python()


def test_multiple_select(page: Page) -> None:
    select_page = SelectPage(page)
    select_page.open_main_page()
    select_page.open_select_page()
    select_page.open_multiple_select_tab()
    select_page.select_place()
    select_page.select_how_want()
    select_page.select_when_you_want_to_go()
    select_page.click_submit_btn()
    select_page.check_result_text_is_ocean()
