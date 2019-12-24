
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

global link
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке сайта
    page.check_if_basket_empty()  # Ожидаем, что в корзине нет товаров
    page.check_if_text_empty_basket_present()  # Ожидаем текст корзина пуста


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()  # class BasePage()
        page.should_be_login_link()  # class MainPage(BasePage)

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()  # class BasePage()
        page.should_be_login_link()  # class MainPage(BasePage)
        page.go_to_login_page()  # class MainPage(BasePage)
        #
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()  # class LoginPage(BasePage)
        login_page.should_be_login_form()  # class LoginPage(BasePage)
        login_page.should_be_register_form()  # class LoginPage(BasePage)
