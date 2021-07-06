
from pages.user_registration import UserRegistration
from pages.login import Login
from selenium.webdriver.common.by import By

class Test_User:

    def test_create_new_user(self, driver):
        """
            Description:   
                Verify I can create a new user

            Prerequisites: NA, user is dynamically created
        """

        #Create new user
        new_user = UserRegistration(driver)
        email, password = new_user.create_account()

        #Verify landing page after account creation
        assert driver.title == 'My account - My Store'

    def test_signout_user(self, driver):
        """
            Description:   
                Verify I can signout a user

            Prerequisites: NA, user is dynamically created
        """

        #Create new user
        new_user = UserRegistration(driver)
        email, password = new_user.create_account()

        #Click logout button
        driver.find_element(By.CSS_SELECTOR, '.logout').click()
        
        #Verify landing page after successful logout goes back to login page
        assert driver.title == 'Login - My Store'

    def test_signin_user(self, driver):
        """
            Description:   
                Verify I can sign in a user

            Prerequisites: NA, user is dynamically created
        """

        #Create new user
        new_user = UserRegistration(driver)
        email, password = new_user.create_account()

        #Click logout button
        driver.find_element(By.CSS_SELECTOR, '.logout').click()

        #Sign in the user again
        login_page = Login(driver)
        login_page.login(email, password)
        
        #Verify landing page after successful login goes to my account
        assert driver.title == 'My account - My Store'


        


    
    