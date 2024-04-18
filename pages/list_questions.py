from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ListQuestions:

    def __init__(self, driver):
        self.driver = driver

    # прокрутка до элемента на странице с нажатием
    def search_question_click(self, element):
        element_scroll = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_scroll)
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

