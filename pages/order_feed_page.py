from pages.base_page import BasePage
from locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    def get_total_orders_count(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_count(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    def is_orders_in_progress_displayed(self):
        return self.find_element(OrderFeedLocators.ORDERS_IN_PROGRESS).is_displayed()

    def get_orders_in_progress(self):
        return self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS_NUMBERS)