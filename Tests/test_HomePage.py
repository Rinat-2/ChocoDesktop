import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_Home_Page(BaseTest):

    def test_find_tickets(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_search_tickets(TestData.CITY_1, TestData.CITY_2)
