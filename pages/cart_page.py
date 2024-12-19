from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
   # SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULTS = (By.XPATH, "//div[@class='h-display-flex h-margin-b-default']//h4")
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1")
    product_in_cart = (By.CSS_SELECTOR, "[id*='addToCartButton']")


    def verify_cart_empty_text(self, product):
        actual_result = self.find_element(*self.CART_EMPTY_MESSAGE).text
        assert product in actual_result.lower(), f'Expected text {product.lower()} not in actual {actual_result}'


    def verify_item_in_cart(self,search_word):
      self.verify_text(search_word,*self.SEARCH_RESULTS)#search_word = 'Your cart is empty'
      """actual_word = self.driver.find_element(*self.CART_EMPTY_MESSAGE).text
      assert search_word in actual_word
      f'{search_word} not in {actual_word}'"""


    def add_item_to_cart(self):
      sleep(4)
    # context.driver.find_element(By.CSS_SELECTOR,"[id*=addToCartButtonOrTextIdFor]").click()
      self.wait_for_element_visible(self.product_in_cart)

    # element =context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
      self.wait_and_click(*self.product_in_cart)
      #self.execute_script(element)
      sleep(4)