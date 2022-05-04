import time
import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from config.config import TestData


class Test_HomePage(BaseTest):

    def test_book_available(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(3)
        homePage.search_book(TestData.BOOK_TITLE)
        book_available = homePage.is_book_visible()
        assert book_available

    def test_want_to_read_btn_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(3)
        homePage.search_book(TestData.BOOK_TITLE)
        want_to_read_btn = homePage.is_want_to_read_btn_visible()
        assert want_to_read_btn

    def test_remove_book(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(3)
        homePage.search_book(TestData.BOOK_TITLE)
        homePage.add_book()
        time.sleep(2)
        homePage.remove_book()
        want_to_read_btn = homePage.is_want_to_read_btn_visible()
        assert want_to_read_btn

    def test_signout(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(3)
        homePage.do_logout()
