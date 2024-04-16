from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ScooterHomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_site(self, site):
        self.driver.get(site)

    def scroll_element(self, scroll_element):
        element = self.driver.find_element(*scroll_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_section(self, section):
        self.driver.find_element(*section).click()

    def wait_element_clickable(self, element_clickable):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(element_clickable))

    def wait_element_located(self, element_located):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(element_located))

    def get_text_of_element(self, text_of_element):
        text = self.driver.find_element(*text_of_element).text
        return text
