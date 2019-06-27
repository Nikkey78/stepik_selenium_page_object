from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import BasketPage
import pytest


# запускать английскую версию сайта
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.view_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()


@pytest.mark.login_guest
class TestLoginFormMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем PageObject, передаем в конструктор экз. драйвера и url
        page.open()
        page.go_to_login_page()  # переходим на страницу логина

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_can_login_or_registration(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_login_page()





