from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from locators import MainPageLocators
from constants import CONSTRUCTOR_URL, ORDER_FEED_URL

class MainPage(BasePage):

    def open_constructor(self):
        self.open_url(CONSTRUCTOR_URL)

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    def open_ingredient_details(self):
        self.click_element(MainPageLocators.INGREDIENTS)

    def is_ingredient_modal_displayed(self):
        return self.is_element_displayed(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_ingredient_modal_closed(self):
        return self.is_element_invisible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    def get_ingredient_counter(self):
        counters = self.find_elements(
            MainPageLocators.INGREDIENT_COUNTER
        )

        values = []
        for counter in counters:
            if counter.is_displayed():
                text = counter.text.strip()
                if text.isdigit():
                    values.append(int(text))

        return max(values, default=0)

    def add_first_ingredient_to_constructor(self):
        overlays = [
            element
            for element in self.find_elements(
                MainPageLocators.MODAL_OVERLAY
            )
            if element.is_displayed()
        ]

        if overlays:
            ActionChains(self.driver).send_keys(
                Keys.ESCAPE
            ).perform()

            WebDriverWait(self.driver, 5).until(
                lambda driver: not any(
                    element.is_displayed()
                    for element in driver.find_elements(
                        *MainPageLocators.MODAL_OVERLAY
                    )
                )
            )

        counter_before = self.get_ingredient_counter()

        self.drag_and_drop(
            MainPageLocators.INGREDIENTS,
            MainPageLocators.BURGER_CONSTRUCTOR
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver:
                self.get_ingredient_counter() > counter_before
        )

    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    def is_constructor_open(self):
        return (
            self.get_current_url().rstrip("/")
            == CONSTRUCTOR_URL.rstrip("/")
        )

    def is_order_feed_open(self):
        return (
            self.get_current_url().rstrip("/")
            == ORDER_FEED_URL.rstrip("/")
        )