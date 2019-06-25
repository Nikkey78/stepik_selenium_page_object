from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, "string 'login' is not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FIELD_LOGIN_MAIL), \
            "Login mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.FIELD_LOGIN_PASSWORD), \
            "Login password field is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FIELD_REGISTRATION_MAIL), \
            "Registration mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD_1), \
            "Registration password_1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD_2), \
            "Registration password 2 field is not presented"
