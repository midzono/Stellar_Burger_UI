from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):

    def open_login_form(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        email_input = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        self.click_element(LoginPageLocators.SUBMIT_LOGIN_BUTTON)