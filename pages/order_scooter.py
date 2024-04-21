from selenium.webdriver.common.keys import Keys
import time
from pages.basepage import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage(BasePage):

    # выбор цвета скутера
    def checkbox_color_scooter(self, color_scooter):
        self.driver.find_element(*color_scooter).click()

    # заполнение страницы для кого скутер
    def filling_who_is_scooter_for(self, string_name, name, string_surname, surname, string_address, address,
                                   string_phone_number, phone_number, string_metro, metro):
        self.driver.find_element(*string_name).send_keys(name)
        self.driver.find_element(*string_surname).send_keys(surname)
        self.driver.find_element(*string_address).send_keys(address)
        self.driver.find_element(*string_phone_number).send_keys(phone_number)
        time.sleep(2)
        self.driver.find_element(*string_metro).send_keys(metro)
        self.driver.find_element(*string_metro).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*string_metro).send_keys(Keys.ENTER)

    # заполнение страницы о аренде
    def filling_about_rent(self, rental_period, period_one_day, color_scooter_black, string_when_bring_scooter, date, string, message):
        self.driver.find_element(*string_when_bring_scooter).send_keys(date)
        self.driver.find_element(*string_when_bring_scooter).send_keys(Keys.ENTER)
        self.driver.find_element(*rental_period).click()
        self.driver.find_element(*period_one_day).click()
        self.driver.find_element(*color_scooter_black).click()
        self.driver.find_element(*string).send_keys(message)

    # ожидание элемента и нажатие
    def wait_element_and_click(self, element):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    # нажатие на элемент и ожидание
    def click_and_wait_element(self, button_next, chapter_about_rent):
        self.driver.find_element(*button_next).click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(chapter_about_rent))

    # подтвердить заказ
    def valid_purchase(self, button_middle_order, button_yes, button_see_status):
        self.driver.find_element(*button_middle_order).click()
        self.driver.find_element(*button_yes).click()
        self.driver.find_element(*button_see_status).click()

    # переход на дзен
    def dzen(self, logo_yandex, dzen_button):
        self.driver.find_element(*logo_yandex).click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable(dzen_button))
