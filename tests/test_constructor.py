import allure

from pages.main_page import MainPage

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход на вкладку «Конструктор»")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        main_page.click_constructor()

        assert main_page.is_constructor_open()

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
        counter_before = main_page.get_ingredient_counter()
        main_page.add_first_ingredient_to_constructor()
        counter_after = main_page.get_ingredient_counter()
        assert counter_after > counter_before