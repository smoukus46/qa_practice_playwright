from pages.base_page import BasePage


class SelectPageLocator:
    LANGUAGE_SELECTOR_ID = "#id_choose_language"
    PLACE_SELECTOR_ID = "#id_choose_the_place_you_want_to_go"
    HOW_WANT_SELECTOR_ID = "#id_choose_how_you_want_to_get_there"
    WHEN_SELECTOR_ID = "#id_choose_when_you_want_to_go"
    SUBMIT_BTN = "#submit-id-submit"
    RESULT_TEXT = "#result-text"


class SelectPage(BasePage):
    def open_select_page(self) -> None:
        self.click_on_link('Select')

    def open_multiple_select_tab(self) -> None:
        self.click_on_link('Multiple selects')

    def select_python_language(self) -> None:
        self.select_value(SelectPageLocator.LANGUAGE_SELECTOR_ID, 'Python')

    def select_place(self) -> None:
        self.select_value(SelectPageLocator.PLACE_SELECTOR_ID, 'Ocean')

    def select_how_want(self) -> None:
        self.select_value(SelectPageLocator.HOW_WANT_SELECTOR_ID, 'Air')

    def select_when_you_want_to_go(self) -> None:
        self.select_value(SelectPageLocator.WHEN_SELECTOR_ID, 'Tomorrow')

    def click_submit_btn(self) -> None:
        self.page.locator(SelectPageLocator.SUBMIT_BTN).click()

    def check_result_is_python(self) -> None:
        self.element_have_text(SelectPageLocator.RESULT_TEXT, 'Python')

    def check_result_text_is_ocean(self) -> None:
        self.element_have_text(SelectPageLocator.RESULT_TEXT, 'to go by air to the ocean tomorrow')
