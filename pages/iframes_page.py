from pages.base_page import BasePage
from playwright.sync_api import FrameLocator, expect


class IframesPageLocator:
    FRAME_LOCATOR = ".embed-responsive-item"
    NAV_BAR_MENU_BTN = ".navbar-toggler"


class IframesPage(BasePage):
    def open_iframes_page(self) -> None:
        self.click_on_link('Iframes')

    def switch_to_frame_page(self) -> FrameLocator:
        return self.page.frame_locator(IframesPageLocator.FRAME_LOCATOR)

    def open_menu_in_frame(self) -> None:
        frame = self.switch_to_frame_page()
        frame.locator(IframesPageLocator.NAV_BAR_MENU_BTN).click()

    def nav_bar_menu_is_visible(self) -> bool:
        frame = self.switch_to_frame_page()
        follow_link = frame.get_by_role('link', name='Follow on Twitter')
        return expect(follow_link).to_be_visible()
