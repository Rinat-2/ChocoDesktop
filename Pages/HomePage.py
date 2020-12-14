from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    DEPARTURE_CITY = (By.ID, "city_1_user")
    ARRIVAL_CITY = (By.ID, "city_2_user")
    DATE = (By.CLASS_NAME, 'search-form__date_choose__event')
    DATE_PICKER = (By.CLASS_NAME, 'k-active k-in-month')
    FIND_TICKETS = (By.CSS_SELECTOR, "button[type='button']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_search_tickets(self, city_1, city_2):
        self.do_send_keys(self.DEPARTURE_CITY, city_1)
        self.do_send_keys(self.ARRIVAL_CITY, city_2)
        self.do_click(self.DATE)
        self.is_visible(self.DATE_PICKER)
        self.do_click(self.DATE_PICKER)
        self.do_click(self.FIND_TICKETS)
