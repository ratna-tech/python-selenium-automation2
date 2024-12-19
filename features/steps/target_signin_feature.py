from behave import given, when, then
from time import sleep


@when('From right side navigation menu, click Sign')
def right_side_sign_in(context):
    #context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    context.app.sign_in_page.click_on_sign_in()
    sleep(4)

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