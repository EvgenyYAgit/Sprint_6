from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # переход на страницу
    def get_site(self, site):
        self.driver.get(site)

    # отправка сообщения в строку
    def filling_string(self, string, message):
        self.driver.find_element(*string).send_keys(message)

    # прокрутка до элемента на странице

    def scroll_element(self, scroll_element):
        element = self.driver.find_element(*scroll_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # нажатие на элемент
    def click_on_section(self, section):
        self.driver.find_element(*section).click()

    # ожидание до видимого элемента
    def wait_element_located(self, element_located):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(element_located))

    # ожидание до кликабельного элемента
    def wait_element_clickable(self, element_clickable):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(element_clickable))

    # текст элемента
    def get_text_of_element(self, text_of_element):
        text = self.driver.find_element(*text_of_element).text
        return text


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
