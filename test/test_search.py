import pytest
import time
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("item, item_count", [("pink", 1), ("dog food", 0), ("dress", 7)])
def test_count(driver, item, item_count):
    """
        Description:   
            Verify search functionality returns the correct count

        Prerequisites:
            Searching returns the following results 1 pink item, 0 dog food items, 7 dresses
    """

    home = HomePage(driver)
    home.search_for_product(item)

    results_page = SearchResultsPage(driver)
    assert results_page.count_search_results() == item_count

def test_empty_results(driver):
    """
        Description:   
            Verify no products are displayed on an empty search

        Prerequisites:
            The DB must have: 0 dog food items
    """

    #Search for non-existent item
    home = HomePage(driver)
    home.search_for_product("dog food")

    #Verify product list does not exists. This means no results shown for dog food
    results_page = SearchResultsPage(driver)
    with pytest.raises(Exception): 
        results_page.get_product_list()

def test_relevant_results(driver):
    """
        Description:   
            Verify results are relevant to the search

        Prerequisites:
            The DB must have 5 dress items
    """

    #Search dress
    home = HomePage(driver)
    home.search_for_product("dress")

    #search for results in product list
    results_page = SearchResultsPage(driver)
    results_page.switch_to_list_view()
    product_list = results_page.get_product_list_row()

    dresses = product_list.find_elements(By.XPATH, "//*[@class='product_list row list']//*[@class='product-name' and contains(text(),'Dress')]")
    assert len(dresses) == 5
    