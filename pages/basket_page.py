from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        self.should_not_be_products_in_basket()
        self.should_be_text_about_empty_basket()

    def basket_should_not_be_empty(self):
        self.should_be_products_in_basket()
        self.should_not_be_text_about_empty_basket()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "There are products in the basket, although they should not be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "There is a message about an empty " \
                                                                               "cart, although it shouldn't be "

    def should_be_products_in_basket(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Products is not presented in the basket, although they should be"

    def should_not_be_text_about_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.TEXT_EMPTY_BASKET), "Text about empty basket is not presented " \
                                                                           "in the basket, although it should be "
