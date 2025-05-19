from playwright.sync_api import Page
from pages.drag_and_drop_page import DragAndDropPage, DragAndDropPageLocator


def test_boxes_tab(page: Page) -> None:
    boxes_page = DragAndDropPage(page)
    boxes_page.open_main_page()
    boxes_page.open_single_ui_element()
    boxes_page.open_drag_and_drop_page()
    boxes_page.drag_and_drop(DragAndDropPageLocator.DRAGGABLE_BOX_ID, DragAndDropPageLocator.DROPPABLE_BOX_ID)
    boxes_page.check_elem_is_dropped(DragAndDropPageLocator.DROPPED_BOX_TEXT_ID)


def test_images_tab(page: Page) -> None:
    images_page = DragAndDropPage(page)
    images_page.open_main_page()
    images_page.open_single_ui_element()
    images_page.open_drag_and_drop_page()
    images_page.open_images_tab()
    images_page.drag_and_drop(DragAndDropPageLocator.DRAGGABLE_IMAGE_XPATH, DragAndDropPageLocator.DROPPABLE_IMAGE_ID)
    images_page.check_elem_is_dropped(DragAndDropPageLocator.DROPPED_IMAGE_TEXT_XPATH)
