from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        try:
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()
        except ElementClickInterceptedException:
            element = self.find_element(locator)
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def is_element_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            source
        )

        ActionChains(self.driver).move_to_element(source).pause(
            0.3
        ).click_and_hold().pause(
            0.5
        ).move_to_element(target).pause(
            0.5
        ).release().perform()