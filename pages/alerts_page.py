from pages.base_page import BasePage
from playwright.sync_api import Dialog


class AlertsPageLocator:
    RESULT_TEXT_ID = '#result-text'


class AlertsPage(BasePage):
    def open_alerts_page(self) -> None:
        self.click_on_link('Alerts')

    def open_confirmation_tab(self) -> None:
        self.click_on_link('Confirmation box')

    def open_prompt_tab(self) -> None:
        self.click_on_link('Prompt box')

    def click_alert_button(self, handler) -> None:
        self.page.on('dialog', handler)
        self.click_on_link('Click')

    def alert_handler(self, dialog: Dialog) -> None:
        assert dialog.message == 'I am an alert!'
        dialog.accept()

    def confirmation_handler(self, dialog: Dialog) -> None:
        dialog.accept()

    def prompt_handler(self, dialog: Dialog) -> None:
        dialog.accept("Hello World!")

    def check_result_text(self, text: str) -> bool:
        return self.element_have_text(AlertsPageLocator.RESULT_TEXT_ID, text)
