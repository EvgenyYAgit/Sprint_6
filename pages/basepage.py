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
