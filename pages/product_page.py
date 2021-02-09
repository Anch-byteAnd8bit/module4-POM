from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_and_solve_the_task(self):
        self.should_be_basket()
        self.add_product_to_basket()
        self.get_code()

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button for adding a product to the basket " \
                                                                            "isn't presented"

    def get_code(self):
        self.solve_quiz_and_get_code()
