from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def check_if_basket_empty(self):
        assert self.is_not_element_present(
            By.CSS_SELECTOR, "#basket_formset"), "В корзине есть товар"

    def check_if_text_empty_basket_present(self):
        empty_basket = self.browser.find_element(
            By.CSS_SELECTOR, "#content_inner > p").text
        assert "корзина пуста" in empty_basket, "В корзине есть товар"
