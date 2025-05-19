from pages.base_page import BasePage
from playwright.sync_api import Page


class PopUpPageLocator:
    LAUNCH_POP_UP_XPATH = "//button[contains(text(), 'Launch Pop-Up')]"
    CHECKBOX_IN_POP_UP_ID = "#id_checkbox_0"
    SEND_BTN_XPATH = "//button[text()='Send']"
    CHECK_BTN_XPATH = "//button[text()='Check']"
    SUBMIT_BTN_ID = "#submit-id-submit"
    TEXT_FROM_FRAME_INPUT_XPATH = "//input[@id='id_text_from_iframe']"
    RESULT_TEXT_ID = "#result-text"
    CHECK_RESULT_DIV_ID = "#check-result"
    FRAME_LOCATOR = "div iframe"
    TEXT_TO_COPY_ID = "#text-to-copy"


class PopUpPage(BasePage):
    def open_pop_up_page(self) -> None:
        self.click_on_link('Pop-Up')

    def open_iframe_pop_up_tab(self) -> None:
        self.click_on_link('Iframe Pop-Up')

    def click_launch_btn(self) -> None:
        self.page.locator(PopUpPageLocator.LAUNCH_POP_UP_XPATH).click()

    def switch_to_pop_up(self) -> Page:
        self.page.locator(PopUpPageLocator.LAUNCH_POP_UP_XPATH).click()
        pop_up = self.page.context.pages[-1]
        return pop_up

    def click_on_checkbox_in_pop_up(self, pop_up: Page) -> None:
        pop_up.check(PopUpPageLocator.CHECKBOX_IN_POP_UP_ID)

    def click_send_btn_in_pop_up(self, pop_up: Page) -> None:
        pop_up.locator(PopUpPageLocator.SEND_BTN_XPATH).click()

    def click_check_btn_in_pop_up(self, pop_up: Page) -> None:
        pop_up.locator(PopUpPageLocator.CHECK_BTN_XPATH).click()

    def click_submit_btn(self) -> None:
        self.page.locator(PopUpPageLocator.SUBMIT_BTN_ID).click()

    def fill_text_from_iframe_input(self, text: str) -> None:
        self.fill_input(PopUpPageLocator.TEXT_FROM_FRAME_INPUT_XPATH, text)

    def check_result_text_in_main_page(self, locator: str, text: str) -> bool:
        return self.element_contains_text(locator, text)

    def copy_text_in_pop_up_frame(self, pop_up: Page) -> str:
        frame = pop_up.frame_locator(PopUpPageLocator.FRAME_LOCATOR)
        return frame.locator(PopUpPageLocator.TEXT_TO_COPY_ID).text_content()
