import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Переход на вкладку «Лента заказов»")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.is_order_feed_open()

    @allure.title("Отображение счётчика заказов за всё время")
    def test_total_orders_counter_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        total_count = feed_page.get_total_orders_count()
        assert total_count.isdigit()

    @allure.title("Отображение счётчика заказов за сегодня")
    def test_today_orders_counter_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        today_count = feed_page.get_today_orders_count()
        assert today_count.isdigit()

    @allure.title("Отображение раздела заказов в работе")
    def test_orders_in_progress_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        assert feed_page.is_orders_in_progress_displayed()