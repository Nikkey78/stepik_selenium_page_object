from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    FIELD_LOGIN_MAIL = (By.ID, "id_login-username")
    FIELD_LOGIN_PASSWORD = (By.ID, "id_login-password")
    FIELD_REGISTRATION_MAIL = (By.ID, "id_registration-email")
    FIELD_REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    FIELD_REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators(object):
    BUTTON_ADD = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_BOOK = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators(object):
    EMPTY_BASKET_MESS_EN = (By.XPATH, "//*[contains(text(), 'Your basket is empty')]")
