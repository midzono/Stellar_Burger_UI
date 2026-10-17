import allure

from pages.main_page import MainPage
from locators import MainPageLocators

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход в раздел «Конструктор»")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        main_page.click_constructor()
        assert "stellarburgers.education-services.ru" in driver.current_url

    @allure.title("Переход в раздел «Лента заказов»")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert "stellarburgers.education-services.ru" in driver.current_url

    @allure.title("Открытие окна с деталями ингредиента")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_details()
        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие окна с деталями ингредиента")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_details()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()
        
    @allure.title("Увеличение счётчика при добавлении ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_details()
        assert main_page.is_ingredient_modal_displayed()

        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()
        
        ingredient = main_page.find_element(MainPageLocators.INGREDIENTS)
        constructor = main_page.find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        main_page.drag_and_drop(
            MainPageLocators.INGREDIENTS,
            MainPageLocators.BURGER_CONSTRUCTOR
        )
        assert main_page.get_ingredient_counter() > 0