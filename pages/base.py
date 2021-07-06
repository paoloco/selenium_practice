from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ShoppingBasePage:
    """
    This class is responsible for common operations while shopping
        -searching for products
        -viewing the products
    """

    #Search
    SEARCH_QUERY = (By.ID, "search_query_top")
    
    #Views
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list .icon-th-list")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid .icon-th-large")

    #Products
    PRODUCTS_LIST = (By.CSS_SELECTOR, "ul.product_list"  )
    PRODUCTS_IMG  = (By.CSS_SELECTOR, ".product_img_link")

    def __init__(self, driver):
        self.driver = driver

    #Search
    def search_for_product(self, text):
        """
        This is a workflow for common test case operations such as looking up an item.
        We want this method at class level to clean so scripts are cleaner

        :Args:
            - text - the item's name eg. 'Summer Chiffon Dress'
        :return: 
            - None.
        """
        web_element = self.driver.find_element(*self.SEARCH_QUERY)
        web_element.clear()
        web_element.send_keys(text)
        web_element.send_keys(Keys.RETURN)

    #Switch views
    def _wait_for_products_to_load(self):
        """
        Helper function when switching views

        :Args:
            - None.
        :return: 
            - None.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.PRODUCTS_IMG))
    
    def switch_to_list_view(self):
        """
        Toggle list view

        :Args:
            - None.
        :return: 
            - None.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LIST_VIEW_BUTTON)).click()
        self._wait_for_products_to_load()

    def switch_to_grid_view(self):
        """
        Toggle list view

        :Args:
            - None.
        :return: 
            - None.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GRID_VIEW_BUTTON)).click()
        self._wait_for_products_to_load()

    #Products
    def get_products_list(self):
        """
        Returns the product list web element. This is a common ancestor when individually deriving products listed.

        :Args:
            - None. 
        :return: 
            - Ancestor web element to be used for deriving child elements
        """
        products_list = self.driver.find_element(*self.PRODUCTS_LIST)
        return products_list

    def get_products(self):
        """
        Returns the individual products derived from the ancestor

        :Args:
            - None. 
        :return: 
            - A list of web elements - a list of products
        """
        products_list = self.get_products_list()
        products = products_list.find_elements(*self.PRODUCTS_IMG)
        return products






