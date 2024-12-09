from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('add item to cart')
def add_item_to_cart(context):
    #context.driver.find_element(By.CSS_SELECTOR,"[id*=addToCartButtonOrTextIdFor]").click()
    element =context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
    context.driver.execute_script("arguments[0].click();", element)
    sleep(4)


@then('verify item in cart')
def verify_found_results_text(context):
    selected_item= context.driver.find_element(By.XPATH, "//a[@data-test='product-title']")
    item_in_cart = context.driver.find_element(By.XPATH, "//div[@class='h-display-flex h-margin-b-default']//h4")
    assert selected_item.text in item_in_cart.text
    f'{selected_item.text} not in {item_in_cart.text}'