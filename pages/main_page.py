from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    # Навигация
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    # Работа с ингредиентами
    def open_ingredient_details(self):
        ingredients = self.wait.until(
            EC.visibility_of_all_elements_located(
                MainPageLocators.INGREDIENTS
            )
        )
        ingredients[0].click()

    def is_ingredient_modal_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL_TITLE
            )
        ).is_displayed()

    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_ingredient_modal_closed(self):
        return self.wait.until(EC.invisibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL_TITLE
            )
        )

    def get_ingredient_counter(self):
        counters = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    def add_ingredient(self, ingredient_locator, target_locator):
        self.drag_and_drop(ingredient_locator, target_locator)

    # Оформление заказа
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)