import pytest
from selenium import webdriver

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        browser_driver = webdriver.Chrome()
    else:
        browser_driver = webdriver.Firefox()
        
    browser_driver.maximize_window()
    browser_driver.get(BASE_URL)

    yield browser_driver

    browser_driver.quit()