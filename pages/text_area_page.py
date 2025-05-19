from pages.base_page import BasePage
from playwright.sync_api import expect


class TextAreaPageLocator:
    TEXT_AREA_ID = "#id_text_area"
    FIRST_CHAPTER_ID = "#id_first_chapter"
    SECOND_CHAPTER_ID = "#id_second_chapter"
    THIRD_CHAPTER_ID = "#id_third_chapter"
    SUBMIT_BUTTON_ID = "#submit-id-submit"
    RESULT_TEXT_ID = "#result-text"


class TextAreaPage(BasePage):
    def open_textarea_page(self) -> None:
        self.click_on_link('Text area')

    def open_multiple_textareas_page(self) -> None:
        self.click_on_link('Multiple textareas')

    def send_value_to_textarea(self, locator: str, value: str) -> None:
        self.fill_input(locator, value)

    def click_submit(self) -> None:
        self.page.locator(TextAreaPageLocator.SUBMIT_BUTTON_ID).click()

    def change_textarea_size(self, locator: str, height: str) -> None:
        self.page.locator(locator).evaluate(f"el => el.style.height = '{height}px'")

    def check_result_text(self, value: str) -> None:
        expect(self.page.locator(TextAreaPageLocator.RESULT_TEXT_ID)).to_have_text(value)
