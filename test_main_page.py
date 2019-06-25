# import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_ho_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу

    # первый подход: возвращаем экз. LoginPage из метода экз. MainPage
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()

    # вторй подход:
    page.go_to_login_page()         # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# def test_can_login_or_registration(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     login_page = LoginPage(browser, link)
#     login_page.open()
#     login_page.should_be_login_page()


