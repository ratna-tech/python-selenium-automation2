from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()

@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@when('Click on Cart icon')
def click_cart(context):
    #context.driver.find_element(By.XPATH,"//div[@data-test='@web/CartIcon']").click()
     context.app.header.click_on_cart_icon()
     sleep(1)




