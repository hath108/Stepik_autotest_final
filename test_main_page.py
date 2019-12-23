
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

global link
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_if_basket_empty()
    page.check_if_text_empty_basket_present()


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()  # class BasePage()
    page.should_be_login_link()  # class MainPage(BasePage)
    page.go_to_login_page()  # class MainPage(BasePage)
    #
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()  # class LoginPage(BasePage)
    login_page.should_be_login_form()  # class LoginPage(BasePage)
    login_page.should_be_register_form()  # class LoginPage(BasePage)
