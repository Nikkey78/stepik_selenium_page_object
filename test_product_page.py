from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import BasketPage
import pytest


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    page.press_btn_add()
    page.solve_quiz_and_get_code()

    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_be_same_title_book()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.view_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()


@pytest.mark.login_guest
class TestUserAddToCartFromProductPage(object):
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com/"
    #     page = MainPage(browser, link)
    #     page.open()
    #
    #     page.go_to_login_page()
    #     login_page = LoginPage(browser, browser.current_url)
    #
    #     email = str(time.time()) + "@fakemail.org"
    #     password = 'qwerty123456789X'
    #
    #     login_page.register_new_user(email, password)
    #     login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.press_btn_add()
        page.solve_quiz_and_get_code()

        basket_page = ProductPage(browser, browser.current_url)
        basket_page.should_be_same_title_book()
