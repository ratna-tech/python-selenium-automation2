from behave import given, when, then
from time import sleep

"""@given('Open sign in page')
def open_signin(context):
    context.app.main_page.open_main()
    context.app.header.click_on_sign_in()
    context.app.sign_in_page.click_on_sign_in()
    #context.driver.get('https://www.target.com/')
    #context.app.sign_in_page.open_sign_in_page()
"""
"""@when('From right side navigation menu, click Sign')
def right_side_sign_in(context):
    #context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    context.app.sign_in_page.click_on_sign_in()
    sleep(4)"""

@then('Verify Sign into your Target account is shown')
def verify_sign_into_text(context):
    context.app.sign_in_page.verify_sign_into_target_account_text()

@when('Enter email')
def enter_email(context):
    context.app.sign_in_page.enter_email()

@when('Enter password')
def enter_password(context):
    context.app.sign_in_page.enter_password()

@when('Click on Signin button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_on_login()

@when('Click skip button')
def click_skip_button(context):
    context.app.sign_in_page.click_skip_btn()

@when('Click on Maybe later button')
def click_maybe_button(context):
    context.app.sign_in_page.click_on_maybe_later_button()

@then('Verify Sign in')
def verify_sign_in(context):
    sleep(5)
    context.app.sign_in_page.verify_sign_in_user_name()

@when('Store original window')
def store_original_window(context):
    context.app.sign_in_page.store_original_window()

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_on_target_terms_and_conditions_link()
    sleep(10)

@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.sign_in_page.switch_to_newly_opened_window()

@then('switch back to original page')
def switch_back_to_original_page(context):
    context.app.sign_in_page.switch_back_to_original_page()

@when('Enter incorrect email')
def enter_incorrect_email(context):
    context.app.sign_in_page.enter_incorrect_email()

@when('Enter incorrect password')
def enter_incorrect_password(context):
    context.app.sign_in_page.enter_incorrect_password()

@then('Verify Incorrect Sign in')
def verify_incorrect_sign_in(context):
    context.app.sign_in_page.verify_incorrect_sign_in()