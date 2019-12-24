
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

global link
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

global product_page_link
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def register_user(self, browser, timeout=5):
        link_register = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link_register)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review  # 1
    def test_user_can_add_product_to_basket(self, browser):

        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page_url()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.if_product_added_to_basket()
        page.if_price_of_product_equal_sum_in_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review  # 2
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page_url()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.if_product_added_to_basket()
    page.if_price_of_product_equal_sum_in_basket()


@pytest.mark.need_review  # 3
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = product_page_link
    page = BasketPage(browser, link)
    page.open()  # Гость открывает страницу товара
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке
    page.check_if_basket_empty()  # Ожидаем, что в корзине нет товаров
    page.check_if_text_empty_basket_present()  # Ожидаем текст что корзина пуста


@pytest.mark.need_review  # 4
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.test_message_disappeared_after_adding_product_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",

                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_param(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page_url()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.if_product_added_to_basket()
    page.if_price_of_product_equal_sum_in_basket()
