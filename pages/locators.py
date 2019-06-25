from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    FIELD_LOGIN_MAIL = (By.ID, "id_login-username")
    FIELD_LOGIN_PASSWORD = (By.ID, "id_login-password")
    FIELD_REGISTRATION_MAIL = (By.ID, "id_registration-email")
    FIELD_REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    FIELD_REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")

