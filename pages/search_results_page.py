from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
   # SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    SEARCH_RESULTS = (By.XPATH, "//div[@class='h-display-flex h-margin-b-default']//h4")

    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result.lower(), f'Expected text {product.lower()} not in actual {actual_result}'

