import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

IMPLICIT_WAIT = 5 #Default time to find an element

@pytest.fixture(scope="function")
def init():
    #This is a place holder that we can expand later for different browsers
    return {
        'chrome' : webdriver.Chrome(ChromeDriverManager().install()),
        #'ff'     : webdriver.Firefox(executable_path=GeckoDriverManager().install())
    }
    

@pytest.fixture(scope="function", params=['chrome'])
def driver(init, request):
    driver = init[request.param]
    driver.implicitly_wait(IMPLICIT_WAIT) 
    driver.maximize_window()
    yield driver
    driver.quit()