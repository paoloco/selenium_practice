import pandas
import time
from pathlib import Path
from pages.home_page import HomePage
from pages.base import ShoppingBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistration(ShoppingBasePage):

    CUSTOMER_FIRSTNAME = (By.CSS_SELECTOR, "#customer_firstname")
    CUSTOMER_LASTNAME  = (By.CSS_SELECTOR, "#customer_lastname" )
    EMAIL              = (By.CSS_SELECTOR, "#email"             )
    PASSWD             = (By.CSS_SELECTOR, "#passwd"            )
    FIRSTNAME          = (By.CSS_SELECTOR, "#firstname"         )
    LASTNAME           = (By.CSS_SELECTOR, "#lastname"          )
    ADDRESS1           = (By.CSS_SELECTOR, "#address1"          )
    CITY               = (By.CSS_SELECTOR, "#city"              )
    ID_STATE           = (By.CSS_SELECTOR, "#id_state"          )
    POSTCODE           = (By.CSS_SELECTOR, "#postcode"          )
    ID_COUNTRY         = (By.CSS_SELECTOR, "#id_country"        )
    PHONE_MOBILE       = (By.CSS_SELECTOR, "#phone_mobile"      )
    ALIAS              = (By.CSS_SELECTOR, "#alias"             )
    SIGNIN_BTN         = (By.CSS_SELECTOR, ".login"             )
    EMAIL_CREATE       = (By.CSS_SELECTOR, "#email_create"      )
    SUBMITCREATE       = (By.CSS_SELECTOR, "#SubmitCreate"      )
    SUBMITCACCOUNT     = (By.CSS_SELECTOR, "#submitAccount"     )

    def __init__(self, driver):
        self.driver = driver
        self.default_test_user = 'Homer'

    def _get_element_by_css(self, css):
        """
        Helper function that returns the web element. 
        Solves the problem of creating multiple getters for each webelement in the page

        :Args:
            - css 
        :return: 
            - Web Element
        """
        
        element_locator = getattr(self, css)
        element = self.driver.find_element(*element_locator)
        return element

    def _convert_csv_to_pandas_data_frame(self):
        """
        Helper function to get data from the CSV 

        :Args:
            - None. Ideally a path to csv if we have multiple
        :return: 
            - Pandas Data Frame containing data from users_test_data.csv 
        """

        users_test_data_path = Path(__file__).parent.parent / "data" / "users_test_data.csv" 
        users_test_data_path_str = str(users_test_data_path.resolve())
        df = pandas.read_csv(users_test_data_path_str, sep=',', header=0)
        return df

    def _get_random_email(self):
        """
        Helper funtion. Generates a random email for Data Driven Tests

        :Args:
            - None. 
        :return: 
            - A random email address based of the default test user's email
        """

        df = self._convert_csv_to_pandas_data_frame()
        email = df.loc[df.CUSTOMER_FIRSTNAME == self.default_test_user, 'EMAIL'].values[0]
        email = str(time.time()) + email

        return email

    def create_account(self):
        """
        Main workflow funtion called at script level. Creates an account based off test_data.csv

        :Args:
            - None. 
        :return: 
            - Email and Password used to login
        """

        #Click sign in from the home page
        HomePage(self.driver)
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()

        #Store login
        email = self._get_random_email()

        #Create an account using this login
        input_field = self.driver.find_element(*self.EMAIL_CREATE)
        input_field.send_keys(email)

        self.driver.find_element(*self.SUBMITCREATE).click()

        #Wait for 'Create an account' to show up 
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, " //h1[contains(text(),'Create an account')]" )))
        
        #Enter values in user registration
        df = self._convert_csv_to_pandas_data_frame()
        for col in df.columns:

            if col == 'EMAIL': #Value already present 
                continue

            user_data = str(df.loc[df.CUSTOMER_FIRSTNAME == self.default_test_user, col].values[0])
            site_web_element_input = self._get_element_by_css(col)
            site_web_element_input.send_keys(user_data)

            if col == 'PASSWD':
                passwd = user_data

        #Click submit
        self.driver.find_element(*self.SUBMITCACCOUNT).click()

        return (email, passwd)