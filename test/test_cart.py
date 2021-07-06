import pytest
from pages.home_page import HomePage
from pages.cart import Cart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Test_Cart:

    @staticmethod
    def verify_text_in_confirmation_pop_up(driver, text):
        cart = Cart(driver)
        popup = cart.get_confirmation_popup()
        assert str(text) in popup.text  #TODO tests stop once an assert fails. Better to use 'check' if we want to continue after failure

    @pytest.mark.parametrize("item, price", [
        ("Printed Chiffon Dress", 16.40), 
        ("Blouse", 27), 
        ("Faded Short Sleeve T-shirts", 16.51)
    ])
    def test_add_single_item_to_cart(self, driver, item, price):
        """
            Description:   
                Verify I can add an item to the cart. Verify the item added and price.

            Prerequisites:
                The following items exists and have the correct price:
                    "Printed Chiffon Dress"      , 16.40
                    "Blouse"                     , 27   
                    "Faded Short Sleeve T-shirts", 16.51
        """

        home = HomePage(driver)
        home.search_for_product(item)

        cart = Cart(driver)
        cart.add_item_to_cart_by_text(item)

        #Verify item name added to cart
        self.verify_text_in_confirmation_pop_up(driver, item)

        #Verify item price added to cart
        self.verify_text_in_confirmation_pop_up(driver, price)
    
    def test_price_running_total(self, driver):
        """
            Description:   
                Verify the running price total after adding multiple items

            Prerequisites:
                The following items exists and have the correct price:
                    "Printed Chiffon Dress"      , 16.40
                    "Blouse"                     , 27   
                    "Faded Short Sleeve T-shirts", 16.51
        """

        home = HomePage(driver)
        cart = Cart(driver)
        inventory = [("Printed Chiffon Dress", 16.40), ("Blouse", 27), ("Faded Short Sleeve T-shirts", 16.51)]

        running_total = 0
        for item, price in inventory:
            running_total += price

            home.search_for_product(item)
            cart.add_item_to_cart_by_text(item)

            #Verify item name
            self.verify_text_in_confirmation_pop_up(driver, item)

            #Verify running total
            self.verify_text_in_confirmation_pop_up(driver, running_total)
            cart.close_confirmation_popup()

    def test_remove_item_from_cart(self, driver):
        """
            Description:   
                Verify I can remove an item from the cart.

            Prerequisites:
                The following items exists and have the correct price:
                    "Blouse"   
        """
        item = "Blouse"
        
        home = HomePage(driver)
        home.search_for_product(item)

        #Add blouse
        cart = Cart(driver)
        cart.add_item_to_cart_by_text(item)
        cart.close_confirmation_popup()

        #Remove blouse and assert the total price is 0
        cart.goto_cart()
        cart.delete_item_from_cart_by_text(item)

        #Verify empty shopping cart after removing the item
        expected_text = "Your shopping cart is empty."
        alert = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(),'{expected_text}')]")))
        assert alert