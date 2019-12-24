from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
        self.browser.find_element(
            By.CSS_SELECTOR, "#register_form > button").click()

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
