from pages.base import ShoppingBasePage

class HomePage(ShoppingBasePage):
    BASE_URL = 'http://automationpractice.com'
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.BASE_URL)
