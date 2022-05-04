import pytest
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from config.config import TestData


class Test_Login(BaseTest):

    def test_valid_login(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        personaldiv = homePage.is_personal_div_exist()
        assert personaldiv
