from selenium.webdriver.common.keys import Keys
import time


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    # выбор станции метро
    def selection_metro(self, string_metro, metro):
        time.sleep(2)
        self.driver.find_element(*string_metro).send_keys(metro)
        self.driver.find_element(*string_metro).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*string_metro).send_keys(Keys.ENTER)

    # выбор цвета скутера
    def checkbox_color_scooter(self, color_scooter):
        self.driver.find_element(*color_scooter).click()

    # выбор даты
    def selection_date(self, string_when_bring_scooter, date):
        self.driver.find_element(*string_when_bring_scooter).send_keys(date)
        self.driver.find_element(*string_when_bring_scooter).send_keys(Keys.ENTER)

    # переключение на новую вкладку
    def switch_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    # закрыть вкладку браузера
    def close_tab(self):
        self.driver.close()
