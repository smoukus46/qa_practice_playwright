from playwright.sync_api import Page
from pages.alerts_page import AlertsPage


def test_alert_box(page: Page) -> None:
    alert_page = AlertsPage(page)
    alert_page.open_main_page()
    alert_page.open_single_ui_element()
    alert_page.open_alerts_page()
    alert_page.click_alert_button(alert_page.alert_handler)


def test_confirmation_box(page: Page) -> None:
    confirmation_page = AlertsPage(page)
    confirmation_page.open_main_page()
    confirmation_page.open_single_ui_element()
    confirmation_page.open_alerts_page()
    confirmation_page.open_confirmation_tab()
    confirmation_page.click_alert_button(confirmation_page.confirmation_handler)
    confirmation_page.check_result_text('Ok')


def test_prompt_box(page: Page) -> None:
    prompt_page = AlertsPage(page)
    prompt_page.open_main_page()
    prompt_page.open_single_ui_element()
    prompt_page.open_alerts_page()
    prompt_page.open_prompt_tab()
    prompt_page.click_alert_button(prompt_page.prompt_handler)
    prompt_page.check_result_text('Hello World!')
