from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH,"//div[@data-test='@web/CartIcon']")
    SIGN_IN_BUTTON = (By.ID,"account-sign-in")
    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_and_click(*self.SEARCH_BTN)
        sleep(10)

    def click_on_cart_icon(self):
        self.wait_and_click(*self.CART_ICON)

    def click_on_sign_in(self ):
        self.wait_and_click(*self.SIGN_IN_BUTTON)
