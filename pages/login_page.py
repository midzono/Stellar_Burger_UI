from pages.base_page import BasePage
from locators import LoginPageLocators
from constants import LOGIN_URL

class LoginPage(BasePage):

    def open_login_page(self):
        self.open_url(LOGIN_URL)

    def enter_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()