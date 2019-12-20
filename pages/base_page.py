
# Для начала сделаем базовую страницу, от которой будут унаследованы все
# остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
# создайте класс с названием BasePage.
from selenium.common.exceptions import NoSuchElementException
import time


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        #  Теперь добавим еще один метод open. Он должен открывать нужную страницу
        # в браузере, используя метод get().
        self.browser.get(self.url)
