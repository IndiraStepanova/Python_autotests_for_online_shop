from .base_page import BasePage
from .locators import ProductPageLocators

# dict for add to basket button
expected_button_text = {
    "ru": "Добавить в корзину",
    "en-gb": "Add to basket",
    "fr": "Ajouter au panier",
    "es": "Añadir al carrito"
}


class ProductPage(BasePage):
    def compare_selected_and_added_product(self):
        self.compare_selected_product_name_and_added_product_name()
        self.compare_selected_product_price_and_added_product_price()

    def should_be_add_to_basket_button(self, language):
        button_text = self.get_element_text(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        print("\ntext of button: "+button_text)
        assert button_text in expected_button_text[language], "Incorrect text of button!"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def compare_selected_product_name_and_added_product_name(self):
        product_added_allert = self.get_element_text(
            *ProductPageLocators.PRODUCT_ADDED_ALLERT_MESSAGE)
        product_name = self.get_element_text(
            *ProductPageLocators.NAME_OF_PRODUCT)
        assert product_name == product_added_allert, "Selected and added product name does not match!"

    def compare_selected_product_price_and_added_product_price(self):
        product_price_allert = self.get_element_text(
            *ProductPageLocators.PRODUCT_PRICE_ALLERT_MESSAGE)
        product_price = self.get_element_text(
            *ProductPageLocators.PRICE_OF_PRODUCT)
        assert product_price == product_price_allert, "Selected and added product price does not match!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
