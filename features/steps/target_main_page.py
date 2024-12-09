from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')





