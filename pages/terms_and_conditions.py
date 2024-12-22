from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class TermsAndConditions(BasePage):
    TERMS_CONDITIONS =(By.CSS_SELECTOR, "h1[data-test='page-title']")
    TERMS_CONDITIONS_TEXT = 'Terms & Conditions'

    def verify_terms_and_conditions_page(self):
       self.verify_text('Terms & Conditions', *self.TERMS_CONDITIONS)



    def user_close_window(self):
       self.close()

    """def user_close_new_window_and_switch_to_sigin(self):
        self.close()
        sleep(5)
    """

