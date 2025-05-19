from playwright.sync_api import Page
from pages.new_tab_page import NewTabPage, NewTabPageLocator


def test_new_tab_page(page: Page) -> None:
    new_tab_page = NewTabPage(page)
    new_tab_page.open_main_page()
    new_tab_page.open_single_ui_element()
    new_tab_page.open_new_tab_page()
    new_page = new_tab_page.switch_to_new_page(NewTabPageLocator.LINK_ID)
    new_tab_page.check_new_page_text(new_page)


def test_new_page_button(page: Page) -> None:
    new_tab_page = NewTabPage(page)
    new_tab_page.open_main_page()
    new_tab_page.open_single_ui_element()
    new_tab_page.open_new_tab_page()
    new_tab_page.open_new_tab_button()
    new_page = new_tab_page.switch_to_new_page(NewTabPageLocator.NEW_PAGE_BUTTON_ID)
    new_tab_page.check_new_page_text(new_page)
