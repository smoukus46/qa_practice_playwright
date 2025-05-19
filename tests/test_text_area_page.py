from playwright.sync_api import Page
from pages.text_area_page import TextAreaPage, TextAreaPageLocator


def test_textarea_page(page: Page) -> None:
    textarea_page = TextAreaPage(page)
    textarea_page.open_main_page()
    textarea_page.open_textarea_page()
    textarea_page.send_value_to_textarea(TextAreaPageLocator.TEXT_AREA_ID, 'Hello World!')
    textarea_page.change_textarea_size(TextAreaPageLocator.TEXT_AREA_ID, '500')
    textarea_page.click_submit()
    textarea_page.check_result_text('Hello World!')


def test_multiple_textareas_page(page: Page) -> None:
    textarea_page = TextAreaPage(page)
    textarea_page.open_main_page()
    textarea_page.open_textarea_page()
    textarea_page.open_multiple_textareas_page()
    textarea_page.change_textarea_size(TextAreaPageLocator.FIRST_CHAPTER_ID, '100')
    textarea_page.send_value_to_textarea(TextAreaPageLocator.FIRST_CHAPTER_ID, 'Hello World from Fisrt Chapter')
    textarea_page.change_textarea_size(TextAreaPageLocator.SECOND_CHAPTER_ID, '100')
    textarea_page.send_value_to_textarea(TextAreaPageLocator.SECOND_CHAPTER_ID, 'Hello World from Second Chapter')
    textarea_page.change_textarea_size(TextAreaPageLocator.THIRD_CHAPTER_ID, '100')
    textarea_page.send_value_to_textarea(TextAreaPageLocator.THIRD_CHAPTER_ID, 'Hello World from Third Chapter')
    textarea_page.click_submit()
    textarea_page.check_result_text('Hello world from fisrt chapterHello world from second chapterHello world from third chapter')
