from .base_page import BasePage
from .locators import BasketPageLocators


# для запуска в английской версии сайта
class BasketPage(BasePage):
    def should_not_be_goods(self):
        empty_basket_message_en = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESS_EN).text
        print('EN---------------->', empty_basket_message_en)
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESS_EN) or \
            "Basket is empty but no message about."
