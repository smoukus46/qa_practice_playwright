from playwright.sync_api import expect
from pages.base_page import BasePage


class InputPageLocators:
    TEXT_INPUT = '#id_text_string'
    RESULT_FIELD = '#result-text'
    EMAIL_INPUT = '#id_email'
    PASSWORD_INPUT = '#id_password'


class InputPage(BasePage):
    def open_input_page(self) -> None:
        self.click_on_link('Text input')

    def open_email_tab(self) -> None:
        self.click_on_link('Email field')

    def open_password_tab(self) -> None:
        self.click_on_link('Password field')

    def fill_text_input(self) -> None:
        self.fill_input(InputPageLocators.TEXT_INPUT, 'HelloWorld')

    def fill_email_input(self) -> None:
        self.fill_input(InputPageLocators.EMAIL_INPUT, 'BalerinaCapuchina@yandex.ru')

    def fill_password_input(self) -> None:
        self.fill_input(InputPageLocators.PASSWORD_INPUT, '96357415Nn!')

    def result_field_have_text(self, text: str) -> bool:
        return self.element_have_text(InputPageLocators.RESULT_FIELD, text)
