import pytest
from selenium import webdriver

from constants import BASE_URL

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    browser.quit()