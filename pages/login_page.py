from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import RegistrationLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.browser.find_element(
            *RegistrationLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(
            *RegistrationLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(
            *RegistrationLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(
            *RegistrationLocators.REGISTRATION_BUTTON).click()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert 'login' in cur_url, "подстрока login отсутствует в текущем url"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(  # is_element_present > class BasePage
            *LoginPageLocators.LOGIN_FORM), " Форма логина отсутствует "

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "форма регистрации отсутствует"
