from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on the benefits cell')
def click_on_benefits(context):
    context.driver.find_element(By.CSS_SELECTOR, ".cell-item-content").click()
    sleep(1)


@then('verify {cell_count} cells are present')
def verify_found_results_text(context, cell_count):
    actual_count = len(context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content"))
    print(actual_count, cell_count)
    assert int(cell_count) == int(actual_count)
    f'{cell_count} not equal to {actual_count}'
