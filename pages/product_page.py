from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_btn_add(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    # в методе задано строгое соответсвие строки названия книги
    def should_be_same_title_book(self):
        title_book = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text
        print('--------------------->', title_book)
        assert "Coders at Work" == title_book, "Title book is not the same."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared."
