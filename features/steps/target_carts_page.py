from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

product_in_cart = (By.CSS_SELECTOR, "[id*='addToCartButton']")
product_in_cart_title = (By.XPATH, "//a[@data-test='product-title']")


@when('add item to cart')
def add_item_to_cart(context):
    context.app.cart_page.add_item_to_cart()
    """sleep(4)
    #context.driver.find_element(By.CSS_SELECTOR,"[id*=addToCartButtonOrTextIdFor]").click()
    element = context.driver.wait.until(EC.element_to_be_clickable(product_in_cart))
   # element =context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
    context.driver.execute_script("arguments[0].click();", element)
    sleep(4)"""


@then('verify {item} in cart')
def verify_found_results_text(context,item):
    """sleep(4)
    #selected_item = context.driver.wait.until(EC.visibility_of_element_located(product_in_cart_title))
    selected_item= context.driver.find_element(By.XPATH, "//a[@data-test='product-title']")
    print(selected_item.text)
    sleep(4)
    item_in_cart = context.driver.find_element(By.XPATH, "//div[@class='h-display-flex h-margin-b-default']//h4")
    assert selected_item.text in item_in_cart.text
    f'{selected_item.text} not in {item_in_cart.text}'"""
    context.app.search_results_page.verify_search_results(item)


@then('Verify {search_word} message is shown')
def verify_item_in_cart(context,search_word):
    context.app.cart_page.verify_item_in_cart(search_word)


