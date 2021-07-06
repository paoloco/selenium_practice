
from pages.user_registration import UserRegistration
from pages.login import Login
from selenium.webdriver.common.by import By

class Test_Cookie:

    def test_cookies_created(self, driver):
        """
            Description:   
                Verify cookies are created for a new user

            Prerequisites: NA, user is dynamically created
        """

        #Initial state no cookies
        cookies = driver.get_cookies()
        assert len(cookies) == 0

        #Create new user
        new_user = UserRegistration(driver)
        email, password = new_user.create_account()

        #Cookie created for new user
        cookies = driver.get_cookies()
        assert len(cookies) == 1