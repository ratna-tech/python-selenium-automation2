from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

"""@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH,"//div[@data-test='@web/CartIcon']").click()
     #context.app.header.click_on_cart_icon()
    sleep(1)"""


""""@then('Verify {search_word} message is shown')
def verify_found_results_text(context, search_word):
    actual_word= context.driver.find_element(By.XPATH,"//h1").text
    assert search_word in actual_word
    f'{search_word} not in {actual_word}'"""









"""@then('Verify {search_word1} is shown')
def verify_found_results_text(context, search_word1):
    actual_word= context.driver.find_element(By.XPATH,"//h1").text
    assert search_word1 in actual_word
    f'{search_word1} not in {actual_word}'"""
