from pages.base_page import BasePage


class DragAndDropPageLocator:
    DRAGGABLE_BOX_ID = "#rect-draggable"
    DRAGGABLE_IMAGE_XPATH = "//div[@id='rect-droppable1']/img"
    DROPPABLE_BOX_ID = "#rect-droppable"
    DROPPABLE_IMAGE_ID = "#rect-droppable2"
    DROPPED_BOX_TEXT_ID = "#text-droppable"
    DROPPED_IMAGE_TEXT_XPATH = "//div[@id='rect-droppable2']/p[@class='text-droppable']"


class DragAndDropPage(BasePage):
    def open_drag_and_drop_page(self) -> None:
        self.click_on_link('Drag and Drop')

    def open_images_tab(self) -> None:
        self.click_on_link('Images')

    def drag_and_drop(self, draggable_locator: str, droppable_locator: str) -> None:
        self.page.locator(draggable_locator).drag_to(self.page.locator(droppable_locator))

    def check_elem_is_dropped(self, dropped_text_locator: str) -> bool:
        return self.element_have_text(dropped_text_locator, 'Dropped!')
