from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class ProductPage(BasePage):
    def should_be_product_page_url(self):
        global cur_url
        cur_url = self.browser.current_url
        assert '?promo=' in cur_url, "подстрока ?promo= отсутствует в текущем url"

    def add_product_to_basket(self):
        global product_name
        global product_price

        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text

        print('Наименование товара :', product_name, '\nЦена товара :',
              product_price)

        self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def if_product_added_to_basket(self):
        name_of_product_in_basket = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text
        time.sleep(10)
        print(
            f"Сообщение об успешном добавлении товара в корзину: {name_of_product_in_basket}")
        assert f"{product_name} был добавлен в вашу корзину" in name_of_product_in_basket, f"Товар не был добавлен в корзину {cur_url}"

    def if_price_of_product_equal_sum_in_basket(self):
        sum_in_basket = self.browser.find_element(
            *ProductPageLocators.SUM_IN_BASKET).text
        print('Общая стоимость товара в корзине:', sum_in_basket)
        assert product_price == sum_in_basket, "Сумма в корзине неправильная"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still presented, but should disappear"
