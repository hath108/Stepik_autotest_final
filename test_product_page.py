
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page_url()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.if_product_added_to_basket()
    product_page.if_price_of_product_equal_sum_in_basket()
