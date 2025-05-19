from playwright.sync_api import Page
from pages.checkboxes_page import CheckboxesPage


def test_checkboxes_page(page: Page) -> None:
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.open_main_page()
    checkboxes_page.open_checkboxes_page()
    checkboxes_page.click_on_checkbox()
    checkboxes_page.click_on_submit_btn()
    checkboxes_page.check_result_on_single_checkbox_tab()


def test_checkboxes_tab(page: Page) -> None:
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.open_main_page()
    checkboxes_page.open_checkboxes_page()
    checkboxes_page.open_checkboxes_tab()
    checkboxes_page.click_on_checkbox_one()
    checkboxes_page.click_on_checkbox_three()
    checkboxes_page.click_on_submit_btn()
    checkboxes_page.check_result_on_checkboxes_tab()
