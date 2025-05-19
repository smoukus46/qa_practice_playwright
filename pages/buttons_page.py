from pages.base_page import BasePage


class ButtonsPageLocator:
    SIMPLE_BUTTON = '#submit-id-submit'
    RESULT_DIV = '#result'
    SELECT_INPUT = '#id_select_state'


class ButtonsPage(BasePage):
    def open_buttons_page(self) -> None:
        self.click_on_link('Simple button')

    def open_fake_button_tab(self) -> None:
        self.click_on_link('Looks like a button')

    def open_disable_button_tab(self) -> None:
        self.click_on_link('Disabled')

    def click_submit_button(self) -> None:
        self.page.locator(ButtonsPageLocator.SIMPLE_BUTTON).click()

    def check_result_message_is_visible(self) -> None:
        self.element_have_text(ButtonsPageLocator.RESULT_DIV, 'Submitted')

    def click_fake_button(self) -> None:
        self.click_on_link('Click')

    def make_button_enabled(self) -> None:
        self.page.locator(ButtonsPageLocator.SELECT_INPUT).select_option('Enabled')
