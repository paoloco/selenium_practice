from pages.base import ShoppingBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class SearchResultsPage(ShoppingBasePage):

    HEADING_COUNTER   = (By.CLASS_NAME   , "heading-counter"         )
    PRODUCT_LIST_ROW  = (By.CSS_SELECTOR , ".product_list.row.list"  )
    PRODUCT_LIST_GRID = (By.CSS_SELECTOR , ".product_list.grid.list" )
    PRODUCTS_IMG      = (By.CSS_SELECTOR , ".product_img_link"       )
    EMPTY_ALERT       = (By.CSS_SELECTOR , ".alert.alert-warning"    )

    def __init__(self, driver):
        self.driver = driver
        self.search_module_wait_time = 10
        self._wait_for_search_results()

    def count_search_results(self):
        """
        Returns the number of items found

        :Args:
            - None. 
        :return: 
            - Integer
        """
        raw_text =  self.driver.find_element(*self.HEADING_COUNTER).text
        num = re.findall(r'\d+', raw_text) 
        return int(num[0])

    def get_product_list_row(self):
        """
        Returns the product list web element. This is a common ancestor when individually deriving products listed.

        :Args:
            - None.
        :return: 
            - Ancestor web element to be used for deriving child elements
        """
        product_list = WebDriverWait(self.driver, self.search_module_wait_time).until(EC.visibility_of_element_located(self.PRODUCT_LIST_ROW))
        return product_list

    def get_product_list_grid(self):
        """
        Returns the product list web element. This is a common ancestor when individually deriving products listed.

        :Args:
            - None.
        :return: 
            - Ancestor web element to be used for deriving child elements
        """
        product_list = WebDriverWait(self.driver, self.search_module_wait_time).until(EC.visibility_of_element_located(self.PRODUCT_LIST_GRID))
        return product_list

    def _wait_for_search_results(self):
        """
        Helper function to avoid race conditions.
        Wait for all products to load

        :Args:
            - None. 
        :return: 
            - None.
        """
        try:
            #Search results are positive
            WebDriverWait(self.driver, self.search_module_wait_time).until(EC.visibility_of_all_elements_located(self.PRODUCTS_IMG))
        except:
            #Search results are negative
            WebDriverWait(self.driver, self.search_module_wait_time).until(EC.visibility_of_element_located(self.EMPTY_ALERT))