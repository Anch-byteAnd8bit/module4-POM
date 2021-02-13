import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.name_product = None
        self.price_product = None

    def add_to_cart_only(self, name_product_, price_product_):
        self.name_product = name_product_
        self.price_product = price_product_
        self.check_name_product()  # проверка имени товара
        self.should_be_basket()  # есть ли кнопка добавления в корзину
        self.add_product_to_basket()  # добавление в корзину
        # self.check_succeed_messsage()  # проверка сообщения об успехе

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

    def check_succeed_message(self):
        self.is_element_present_with_waiting(*ProductPageLocators.MESSAGE_SUCCESS), \
           "Success message is not presented, but should be"

        msg_succeed = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS).text
        assert self.name_product == msg_succeed, "There is no suitable product name in the message"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert self.price_product == price, "There is no matching product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
           "Success message is presented, but should not be"

    def there_should_be_a_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
           "Success message is not presented, but should be"
