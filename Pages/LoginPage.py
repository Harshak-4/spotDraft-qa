from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from config.config import TestData
from Pages.HomePage import HomePage

class LoginPage(BasePage):
    """Locators for login page"""
    button_signin_xpath = (By.XPATH, "//button[contains(text(),'Sign in with email')]")
    textbox_usermail_id = (By.ID, "ap_email")
    textbox_password_id = (By.ID, "ap_password")
    button_login_id = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, usermail, password):
        self.do_click(self.button_signin_xpath)
        self.do_send_keys(self.textbox_usermail_id, usermail)
        self.do_send_keys(self.textbox_password_id, password)
        self.do_click(self.button_login_id)
        return HomePage(self.driver)