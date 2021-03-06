from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_USERNAME_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)
        re_password_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_REPEAT_FIELD)
        re_password_field.send_keys(password)
        submit_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.click()
    
    def login_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.LOGIN_USERNAME_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(
            *LoginPageLocators.LOGIN_PASSWORD_FIELD)
        password_field.send_keys(password)
        submit_button = self.browser.find_element(
            *LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        submit_button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not login URL!"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented!"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_USERNAME_FIELD), "Username field is not presented!"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD_FIELD), "Password field is not presented!"
        assert self.is_element_clicable(
            *LoginPageLocators.LOGIN_SUBMIT_BUTTON), "Submit button is not clicable!"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented!"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_USERNAME_FIELD), "Username field is not presented!"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_FIELD), "Password field is not presented!"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_REPEAT_FIELD), "Password repeat field is not presented!"
        assert self.is_element_clicable(
            *LoginPageLocators.REGISTER_SUBMIT_BUTTON), "Submit button is not clicable!"
