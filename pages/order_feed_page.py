from pages.base_page import BasePage
from locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    def get_total_orders_count(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_count(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    def is_orders_in_progress_displayed(self):
        return self.is_element_displayed(OrderFeedLocators.ORDERS_IN_PROGRESS)

    def get_orders_in_progress(self):
        return self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS_NUMBERS)