from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

search_textbox =(By.CSS_SELECTOR,'.search-input')
search_button = (By.CSS_SELECTOR,'.search-btn')
six_grids = (By.CSS_SELECTOR,'.boxSmall')
three_grids = (By.CSS_SELECTOR,'.grid_4>h3')
browse_pages = (By.XPATH, "//div[@class='grid_18']//h2")
footer_grids = ['contact us','holiday help','product recalls']

@given('Open Target help page')
def open_target(context):
    context.driver.get('https://help.target.com/help/')

@then('verify {expected_text} is present')
def open_target(context,expected_text):
    actual_text = (context.driver.find_element(By.CSS_SELECTOR,'.custom-h2')).text
    verify = expected_text.lower() in actual_text.lower()
    f'{expected_text} not in {actual_text}'


@then('verify Search Help textbox')
def verify_search_help_textbox(context):
    context.driver.find_element(*search_textbox)

@then('verify Search Help button')
def verify_search_button(context):
    context.driver.find_element(*search_button)

@then('verify {count} grids under What would you like to do')
def verify_grid_count(context, count):
    elements = context.driver.find_elements(*six_grids)
    verify = int(count) == len(elements)

@then('verify grids in What would you like to do footer')
def verify_grid_count(context):
    elements = context.driver.find_elements(*three_grids)
    c= 0
    for e in elements:
        verify = e.text == footer_grids[c]
        c +=1


"""@then('verify {expected_text}')
def verify_text_expected(context, expected_text):
    actual_text = context.driver.find_element(*browse_pages).text
    assert expected_text in actual_text"""

