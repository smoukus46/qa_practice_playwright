from pages.base_page import BasePage


class CheckboxesPageLocator:
    CHECKBOX_ID = "#id_checkbox_0"
    SUBMIT_BTN = "#submit-id-submit"
    RESULT_TEXT = "#result-text"
    LABEL_ONE_ID = "xpath=//label[contains(text(), 'One')]"
    LABEL_THREE_ID = "xpath=//label[contains(text(), 'Three')]"


class CheckboxesPage(BasePage):
    def open_checkboxes_page(self) -> None:
        self.click_on_link('Checkbox')

    def open_checkboxes_tab(self) -> None:
        self.click_on_link('Checkboxes')

    def click_on_checkbox(self) -> None:
        self.checkbox_clicker(CheckboxesPageLocator.CHECKBOX_ID)

    def click_on_checkbox_one(self) -> None:
        self.page.locator(CheckboxesPageLocator.LABEL_ONE_ID).click()

    def click_on_checkbox_three(self) -> None:
        self.page.locator(CheckboxesPageLocator.LABEL_THREE_ID).click()

    def click_on_submit_btn(self) -> None:
        self.page.locator(CheckboxesPageLocator.SUBMIT_BTN).click()

    def check_result_on_single_checkbox_tab(self) -> bool:
        return self.element_have_text(CheckboxesPageLocator.RESULT_TEXT, 'select me or not')

    def check_result_on_checkboxes_tab(self) -> bool:
        return self.element_have_text(CheckboxesPageLocator.RESULT_TEXT, 'one, three')
