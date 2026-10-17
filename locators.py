from selenium.webdriver.common.by import By

class MainPageLocators:
    # Навигация по приложению
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[contains(., 'Конструктор')]"
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[contains(., 'Лента заказов')]"
    )

    # Карточки ингредиентов
    INGREDIENTS = (
        By.XPATH,
        "//*[contains(@class, 'BurgerIngredient_ingredient__')]"
    )

    # Счётчик количества добавленного ингредиента
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//*[contains(@class, 'counter_counter__num')]"
    )

    # Модальное окно с деталями ингредиента
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'Детали ингредиента')]"
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[@aria-label='Закрыть']"
    )

    # Область сборки бургера
    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//*[contains(@class, 'BurgerConstructor_basket__')]"
    )

    # Оформление заказа
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Оформить заказ')]"
    )

    # Номер оформленного заказа в модальном окне
    ORDER_NUMBER = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal__')]"
        "//*[self::h2 or self::p][normalize-space()]"
    )

class OrderFeedLocators:
    # Счётчик заказов за всё время
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//*[contains(text(), 'Выполнено за все время')]/following-sibling::*"
    )

    # Счётчик заказов за сегодня
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::*"
    )

    # Заголовок раздела заказов в работе
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//*[contains(text(), 'В работе')]"
    )

    # Номера заказов в разделе «В работе»
    ORDERS_IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//*[contains(text(), 'В работе')]/following::*"
    )

    class LoginPageLocators:
    # Кнопка перехода к авторизации
        LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Войти в аккаунт')]"
        )

    # Поля ввода данных для авторизации
        EMAIL_INPUT = (
        By.XPATH,
        "//input[@type='text' or @type='email']"
        )
        PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
        )

    # Подтверждение входа
        SUBMIT_LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Войти')]"
        )