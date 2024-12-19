from behave import given, when, then
from time import sleep

@when ('Click Sign In')
def click_sign_in(context):
    #context.driver.find_element(By.ID,"account-sign-in").click()
    context.app.header.click_on_sign_in()
    sleep(4)