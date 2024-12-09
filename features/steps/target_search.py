from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import Keys


@when('search for {item}')
def search_for_candy(context,item):
    context.driver.find_element(By.ID, "search").send_keys(item)
    context.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)
