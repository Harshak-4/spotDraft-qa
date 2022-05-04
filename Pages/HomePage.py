import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Locators for home page"""
    textbox_search_xpath = (By.XPATH, "(//input[@placeholder='Search books'])[1]")
    button_search_xpath = (By.XPATH, "//button[@class='searchBox__icon--magnifyingGlass gr-iconButton searchBox__icon searchBox__icon--navbar']")
    div_personal_header_class = (By.CLASS_NAME, "siteHeader__personal")
    button_want_to_read_xpath = (By.XPATH, "//div[@id='1_book_29581']//div[@class='wtrUp wtrLeft']//form")
    text_book_title_xpath = (By.XPATH, "//span[normalize-space()='Foundation and Empire (Foundation #2)']")
    button_remove_book_xpath = (By.XPATH, "//button[@title='Remove this book from your shelves']")
    button_user_profile_xpath = (By.XPATH, "//a[@class='dropdown__trigger dropdown__trigger--profileMenu dropdown__trigger--personalNav']//img[@alt='Harsha K']")
    button_signout_xpath = (By.XPATH, "//div[@class='siteHeader__subNav siteHeader__subNav--profile gr-box gr-box--withShadowLarge']//a[@class='siteHeader__subNavLink'][normalize-space()='Sign out']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_personal_div_exist(self):
        return self.is_visible(self.div_personal_header_class)

    def search_book(self, title):
        self.do_send_keys(self.textbox_search_xpath, title)
        time.sleep(3)
        self.do_click(self.button_search_xpath)

    def is_book_visible(self):
        return self.is_visible(self.text_book_title_xpath)

    def is_want_to_read_btn_visible(self):
        return self.is_visible(self.button_want_to_read_xpath)

    def add_book(self):
        self.do_click(self.button_want_to_read_xpath)

    def remove_book(self):
        self.do_click(self.button_remove_book_xpath)
        time.sleep(2)
        self.accept_alert()

    def do_logout(self):
        self.do_click(self.button_user_profile_xpath)
        self.do_click(self.button_signout_xpath)