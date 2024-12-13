from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
color_option = (By.XPATH,"//div[@aria-label='Carousel']//ul//picture")
#selected_color =(By.XPATH,"//span[text()='color']")
selected_color = (By.CSS_SELECTOR,"[data-test='@web/VariationComponent'] div span")

SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
banner_ad = (By.XPATH,"//div[contains(@id,'search_3__container')]")
product_names = (By.CSS_SELECTOR,"[data-test='product-title']")
product_images = (By.XPATH,"//div[@data-test='web/ProductCard/ProductCardVariantDefault']//h3")
product_image = (By.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper'] h3")
total_product = (By.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper'] h3")
total_product1 = (By.XPATH,"//div[@data-test='@web/ProductCard/ProductCardVariantDefault']")

@when('search for {item}')
def search_for_candy(context,item):
    context.driver.find_element(By.ID, "search").send_keys(item)
    context.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click hrough colors')
def click_through_colors(context):
   # expected_colors = ['Blue Tint', 'Denim Blue', 'Raven', 'Marine']
    expected_colors = ['Blue', 'Rose Pink', 'Red']
    actual_colors = []
    context.driver.execute_script("window.scrollBy(0,50)", "")
    #context.driver.execute_script("return arguments[0].scrollIntoView('colors');", actual_colors)
    context.driver.wait.until(EC.invisibility_of_element(banner_ad))
    colors = context.driver.find_elements(*color_option)
   # [webelement1, webelement2, webelement3]
    #context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS))
    for color in colors:
        color.click()
        print('CCC',color.text)
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
       # print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
       # print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('verify product has a name')
def verify_name(context):
    #names=[]
    products = context.driver.find_elements(*total_product)
    print(len(products))
    names = context.driver.find_elements(*product_names)
    total_products= len(products)
    total_names = len(names)
    print(total_names)
    print(total_products)
    print(total_names, total_products)
    assert total_products == total_names


@then('verify product has image')
def verify_image(context):
    total_image = []
    total_products = len(context.driver.find_elements(*total_product1))
    print(total_products)
    images = context.driver.find_elements(*product_image)
    total_images = len(images)

    print(total_images, total_products)
    assert total_products == total_images