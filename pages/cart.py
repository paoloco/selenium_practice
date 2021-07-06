from pages.base import ShoppingBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart(ShoppingBasePage):
    
    CART               = (By.CSS_SELECTOR , ".shopping_cart a"                                             )
    LAYER_CART         = (By.ID           , 'layer_cart'                                                   )
    LAYER_CART_PRODUCT = (By.ID           , 'layer_cart_product_title'                                     )
    CART_SUMMARY       = (By.ID           , 'cart_summary'                                                 )
    ADD_TO_CART_BUTTON = (By.XPATH        , "//*[contains(@class, 'product_list')]//*[span='Add to cart']" )
    CLOSE_WINDOW       = (By.XPATH        , '//*[@title="Close window"]'                                   )

    def __init__ (self, driver):
        self.driver = driver
        self.cart_module_wait_time = 10
    
    def goto_cart(self):
        """
        Clicks the cart icon

        :Args:
            - None.
        :return: 
            - None.
        """
        self.driver.find_element(*self.CART).click()
    
    def add_item_to_cart_by_text(self, item):
        """
        This is a workflow for common test case operations such as adding an item.

        :Args:
            - item - the item's name eg. 'Summer Chiffon Dress'
        :return: 
            - None.
        """
        self.switch_to_list_view()

        products = self.get_products()
        for product in products:
            if product.get_attribute("title") == item:

                #Hover above the element 
                WebDriverWait(self.driver, self.cart_module_wait_time).until(EC.visibility_of(product))
                action = ActionChains(self.driver)
                action.move_to_element(product).perform()

                #Click add to cart button after hovering
                ADD_TO_CART_BUTTON = WebDriverWait(self.driver, self.cart_module_wait_time).until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON))
                ADD_TO_CART_BUTTON.click()

    def delete_item_from_cart_by_text(self, item):
        """
        This is a workflow for common test case operations such as removing an item.

        :Args:
            - item - the item's name eg. 'Summer Chiffon Dress'
        :return: 
            - None.
        """
        #go to cart
        self.driver.find_element(*self.CART).click()

        #Common ancestor for product name and trash icon
        cart_summary = self.driver.find_element(*self.CART_SUMMARY)

        product_names = cart_summary.find_elements_by_css_selector(".product-name")
        trash_icons = cart_summary.find_elements_by_css_selector(".icon-trash")

        #find the corresponding icon based off index
        for i in range(len(product_names)):
            if item == product_names[i].text:
                trash_icons[i].click()
                break 

    def get_confirmation_popup(self):
        """
        After adding/removing an item from the cart, a pop up shows up.
        This is to get the popup as a weblement to derive other web elements eg. item added, price added

        :Args:
            - None.
        :return: 
            - Popup web element
        """
        popup = WebDriverWait(self.driver, self.cart_module_wait_time).until(EC.visibility_of_element_located(self.LAYER_CART))
        return popup
    
    def close_confirmation_popup(self):
        """
        Close the popup

        :Args:
            - None.
        :return: 
            - None.
        """
        self.driver.find_element(*self.CLOSE_WINDOW).click()