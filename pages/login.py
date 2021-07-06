from selenium.webdriver.common.by import By

class Login:
    email_field    = (By.ID, "email"       )
    password_field = (By.ID, "passwd"      )
    login_button   = (By.ID, "SubmitLogin" )

    def __init__(self, driver):
        self.driver = driver

    def _enter_email(self, email):
        """
        Helper function for the main login workflow
        """
        self.driver.find_element(*self.email_field).send_keys(email)

    def _enter_password(self, password):
        """
        Helper function for the main login workflow
        """
        self.driver.find_element(*self.password_field).send_keys(password)

    def _click_login(self):
        """
        Helper function for the main login workflow
        """
        self.driver.find_element(*self.login_button).click()

    def login(self, email, password):
        """
        Login using the given email and password. 

        :Args:
            - email - str 
            - password - str
        :return: 
            - None. 
        """
        self._enter_email(email)
        self._enter_password(password)
        self._click_login()