from pages.pop_up_page import PopUpPage, PopUpPageLocator
from playwright.sync_api import Page


def test_modal_pop_up(page: Page) -> None:
    modal_pop_up_page = PopUpPage(page)
    modal_pop_up_page.open_main_page()
    modal_pop_up_page.open_single_ui_element()
    modal_pop_up_page.open_pop_up_page()
    pop_up = modal_pop_up_page.switch_to_pop_up()
    modal_pop_up_page.click_on_checkbox_in_pop_up(pop_up)
    modal_pop_up_page.click_send_btn_in_pop_up(pop_up)
    modal_pop_up_page.check_result_text_in_main_page(PopUpPageLocator.RESULT_TEXT_ID, 'select me or not')


def test_iframe_pop_up(page: Page) -> None:
    iframe_pop_up_page = PopUpPage(page)
    iframe_pop_up_page.open_main_page()
    iframe_pop_up_page.open_single_ui_element()
    iframe_pop_up_page.open_pop_up_page()
    iframe_pop_up_page.open_iframe_pop_up_tab()
    pop_up = iframe_pop_up_page.switch_to_pop_up()
    frame_text = iframe_pop_up_page.copy_text_in_pop_up_frame(pop_up)
    iframe_pop_up_page.click_check_btn_in_pop_up(pop_up)
    iframe_pop_up_page.fill_text_from_iframe_input(frame_text)
    iframe_pop_up_page.click_submit_btn()
    iframe_pop_up_page.check_result_text_in_main_page(PopUpPageLocator.CHECK_RESULT_DIV_ID, 'Correct!')
