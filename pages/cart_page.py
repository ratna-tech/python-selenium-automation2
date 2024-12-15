from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
   # SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
   # SEARCH_RESULTS = (By.XPATH, "//div[@class='h-display-flex h-margin-b-default']//h4")
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1")
    def verify_cart_empty_text(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result.lower(), f'Expected text {product.lower()} not in actual {actual_result}'


    def verify_cart_empty(self,search_word):
      #search_word = 'Your cart is empty'
      actual_word = self.driver.find_element(*self.CART_EMPTY_MESSAGE).text
      assert search_word in actual_word
      f'{search_word} not in {actual_word}'