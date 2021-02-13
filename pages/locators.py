from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".alertinner > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main >.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket_summary")


class RegistrationPageLocators():
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[name = "registration-email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[name = "registration-password1"]')
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, 'input[name = "registration-password2"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[name=registration_submit]')
