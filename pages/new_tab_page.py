from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class NewTabPageLocator:
    RESULT_TEXT_ID = "#result-text"
    LINK_ID = "#new-page-link"
    NEW_PAGE_BUTTON_ID = "#new-page-button"


class NewTabPage(BasePage):
    def open_new_tab_page(self) -> None:
        self.click_on_link('New tab')

    def open_new_tab_button(self) -> None:
        self.click_on_link('New tab button')

    def switch_to_new_page(self, locator: str) -> Page:
        with self.page.expect_popup() as new_page_info:
            self.page.locator(locator).click()
        new_page = new_page_info.value
        return new_page

    def check_new_page_text(self, new_page: Page) -> bool:
        return expect(new_page.locator(NewTabPageLocator.RESULT_TEXT_ID)).to_have_text('I am a new page in a new tab')
