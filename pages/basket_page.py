from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BaskePageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def check_if_basket_empty(self):
        assert self.is_not_element_present(
            *BaskePageLocators.BASKET_ITEMS), "В корзине есть товар"

    def check_if_text_empty_basket_present(self):
        empty_basket = self.browser.find_element(
            *BaskePageLocators.BASKET_EMPTY_TEXT).text

        assert "basket is empty" or "Ваша корзина пуста" in empty_basket, (
            "Текст должен содержать 'basket is empty' ", empty_basket)
