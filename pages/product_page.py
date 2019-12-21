from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page_url(self):
        cur_url = self.browser.current_url
        assert '?promo=newYear' in cur_url, "подстрока ?promo=newYear отсутствует в текущем url"

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
            *ProductPageLocators.TEXT_IN_BASKET).text
        print(
            f"Сообщение об успешном добавлении товара в корзину: {name_of_product_in_basket}")
        assert f"{product_name} был добавлен в вашу корзину" in name_of_product_in_basket, "Товар не был добавлен в корзину"

    def if_price_of_product_equal_sum_in_basket(self):
        sum_in_basket = self.browser.find_element(
            *ProductPageLocators.SUM_IN_BASKET).text
        print('Общая стоимость товара в корзине:', sum_in_basket)
        assert product_price == sum_in_basket, "Сумма в корзине неправильная"
