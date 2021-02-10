from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.name_product = None
        self.price_product = None

    def add_to_cart_and_solve_the_task(self, name_product_, price_product_=0):
        self.name_product = name_product_
        self.price_product = price_product_
        self.check_name_product()  # проверка имени товара
        self.should_be_basket()  # есть ли кнопка добавления в корзину
        self.add_product_to_basket()  # добавление в корзину
        self.get_code()  # получение кода
        self.check_succeed()  # проверка сообщения об успехе

    def check_name_product(self):
        assert self.get_name_product() == self.name_product, "Product names do not match!"

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def should_be_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button for adding a product to the " \
                                                                            "basket isn't presented "

    def get_code(self):
        self.solve_quiz_and_get_code()

    def check_succeed(self):
        msg_succeed = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS).text
        assert self.name_product == msg_succeed, "The item has not been added to the basket!"
