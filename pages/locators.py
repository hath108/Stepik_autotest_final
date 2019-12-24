from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")


class RegistrationLocators():
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class BaskePageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    BTN_ADD_TO_BASKET = (
        By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, '#messages > .alert-success > div.alertinner')
    SUM_IN_BASKET = (By.CSS_SELECTOR, '#messages > div.alert> div >p>strong')
