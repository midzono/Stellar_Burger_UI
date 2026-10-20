from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']")

    INGREDIENTS = (
        By.CSS_SELECTOR,
        "a[class*='BurgerIngredient_ingredient__']"
    )
    INGREDIENT_COUNTER = (
        By.CSS_SELECTOR,
        "[class*='counter_counter__num']"
    )
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//*[normalize-space(text())='Детали ингредиента']"
    )
    MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[class*='Modal_modal__close']"
    )
    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "[class*='Modal_modal_overlay']"
    )

    BURGER_CONSTRUCTOR = (
        By.CSS_SELECTOR,
        "ul[class*='BurgerConstructor_basket__list']"
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Оформить заказ')]"
    )
    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "[class*='Modal_modal__'] h2"
    )

class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Войти')]"
    )

class OrderFeedLocators:
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//*[normalize-space(text())='Выполнено за всё время:' "
        "or normalize-space(text())='Выполнено за все время:' "
        "or normalize-space(text())='Выполнено за всё время' "
        "or normalize-space(text())='Выполнено за все время']"
        "/following-sibling::*[1]"
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//*[normalize-space(text())='Выполнено за сегодня:' "
        "or normalize-space(text())='Выполнено за сегодня']"
        "/following-sibling::*[1]"
    )
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//*[normalize-space(text())='В работе' "
        "or normalize-space(text())='В работе:']"
    )
    ORDERS_IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//*[normalize-space(text())='В работе' "
        "or normalize-space(text())='В работе:']"
        "/following::*[self::li or self::p]"
    )