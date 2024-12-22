from behave import given, when, then
from time import sleep


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_and_conditions.verify_terms_and_conditions_page()

@then('User can close new window')
def user_close_new_window(context):
    context.app.terms_and_conditions.user_close_window()