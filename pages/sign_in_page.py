#"[data-test='accountNav-signIn']"
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage
class SignIn(BasePage):
    SIGN_IN_BUTTON=(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_INTO_YOUR_TARGET_ACCOUNT_TEXT = (By.XPATH,"//div//h1//span")
    SIGN_INTO_YOUR_TARGET_ACCOUNT_EXPECTED_TEXT = "Sign into your Target account"
    EMAIL_TEXTBOX = (By.ID, "username")
    PSWD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    SIGNED_IN_USER = (By.XPATH,"//a[@id='account-sign-in']")
    #SIGNED_IN_USER = (By.XPATH, "//a[@data-test='@web/AccountLink']//span")
    MAYBE_LATER_BUTTON= (By.XPATH,"//button[text()='Maybe later']")
    SKIP_BTN = (By.CSS_SELECTOR, '[href="/"]')
    def click_on_sign_in(self):
         self.wait_and_click(*self.SIGN_IN_BUTTON)

    def verify_sign_into_target_account_text(self):
         self.verify_text(*self.SIGN_INTO_YOUR_TARGET_ACCOUNT_EXPECTED_TEXT,*self.SIGN_INTO_YOUR_TARGET_ACCOUNT_TEXT)

    def enter_email(self):
        self.input_text('ashvat09@gmail.com',*self.EMAIL_TEXTBOX)

    def enter_password(self):
        self.input_text('Sunny09!',*self.PSWD_TEXTBOX)

    def click_on_login(self):
         #self.wait_and_click(*self.LOGIN_BUTTON)
        self.find_element(*self.LOGIN_BUTTON).click()

    def click_skip_btn(self):
        self.find_element(*self.SKIP_BTN).click()

    def click_on_maybe_later_button(self):
        self.wait_and_click(*self.MAYBE_LATER_BUTTON)

    def verify_sign_in_user_name(self):
        self.verify_partial_text('Ashvat', *self.SIGNED_IN_USER)