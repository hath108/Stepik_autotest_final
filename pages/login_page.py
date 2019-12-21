from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    '''
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    '''

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


'''
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # class BasePage()
    page.should_be_login_url()  # class LoginPage(BasePage)
    page.should_be_login_form()  # class LoginPage(BasePage)
    page.should_be_register_form()  # class LoginPage(BasePage)
'''
