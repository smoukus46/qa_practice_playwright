from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, locator: str) -> None:
        self.page.goto(locator)

    def open_main_page(self) -> None:
        self.page.goto('https://www.qa-practice.com/')

    def open_single_ui_element(self) -> None:
        self.page.locator('xpath=//span[text()="Single UI Elements"]').click()

    def click_on_link(self, link_text: str) -> None:
        self.page.get_by_role('link', name=link_text).click()

    def fill_input(self, locator: str, value: str) -> None:
        self.page.locator(locator).fill(value)

    def press_enter(self) -> None:
        self.page.keyboard.press('Enter')

    def element_is_visible(self, locator: str) -> bool:
        return expect(self.page.locator(locator)).to_be_visible()

    def element_have_text(self, locator: str, value: str) -> bool:
        return expect(self.page.locator(locator)).to_have_text(value)

    def element_contains_text(self, locator: str, value: str) -> bool:
        return expect(self.page.locator(locator)).to_contain_text(value)

    def checkbox_clicker(self, locator: str) -> None:
        self.page.check(locator)

    def select_value(self, locator: str, value: str) -> None:
        self.page.select_option(locator, value)
