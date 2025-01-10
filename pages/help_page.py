from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select



class HelpPage(BasePage):
    HELP_DD= (By.CSS_SELECTOR, "select[id*='viewHelp']")
    OPEN_SUBCATEGORY = (By.XPATH,"//div[text()='view current promotions']")
    RETURN_PAGE= (By.CSS_SELECTOR,".grid_14")


    def open_target_subcategory(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')



    def select_help_topic_dropdown(self):
        select = Select(self.find_element(*self.HELP_DD))
        select.select_by_value('Returns & Exchanges')

    def verify_returns_page(self):
        self.find_element(*self.RETURN_PAGE)
