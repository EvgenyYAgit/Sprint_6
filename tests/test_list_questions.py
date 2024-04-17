from selenium import webdriver
from pages.basepage import BasePage
import allure
from locators.list_questions_locators import question_how_much_it_cost, answer_how_much_it_cost, \
    question_want_several_scooters, answer_want_several_scooters, question_how_rental_time, answer_how_rental_time, \
    question_order_today, answer_order_today, question_renew_or_return_scooter, answer_renew_or_return_scooter, \
    question_charging_together_scooter, answer_charging_together_scooter, question_cancel_order, answer_cancel_order, \
    question_about_moscow_ring_road, answer_about_moscow_ring_road
from locators.url_base import site


class TestListQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка ответа на вопрос: Сколько это стоит? И как оплатить?')
    def test_question_how_much_it_cost(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_how_much_it_cost)
        home_page.wait_element_clickable(question_how_much_it_cost)
        home_page.click_on_section(question_how_much_it_cost)
        home_page.wait_element_located(answer_how_much_it_cost)
        answer = home_page.get_text_of_element(answer_how_much_it_cost)
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка ответа на вопрос: Хочу сразу несколько самокатов! Так можно?')
    def test_question_want_several_scooters(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_want_several_scooters)
        home_page.wait_element_clickable(question_want_several_scooters)
        home_page.click_on_section(question_want_several_scooters)
        home_page.wait_element_located(answer_want_several_scooters)
        answer = home_page.get_text_of_element(answer_want_several_scooters)
        assert answer == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')

    @allure.title('Проверка ответа на вопрос: Как рассчитывается время аренды?')
    def test_question_how_rental_time(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_how_rental_time)
        home_page.wait_element_clickable(question_how_rental_time)
        home_page.click_on_section(question_how_rental_time)
        home_page.wait_element_located(answer_how_rental_time)
        answer = home_page.get_text_of_element(answer_how_rental_time)
        assert answer == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка ответа на вопрос: Можно ли заказать самокат прямо на сегодня?')
    def test_question_order_today(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_order_today)
        home_page.wait_element_clickable(question_order_today)
        home_page.click_on_section(question_order_today)
        home_page.wait_element_located(answer_order_today)
        answer = home_page.get_text_of_element(answer_order_today)
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка ответа на вопрос: Можно ли продлить заказ или вернуть самокат раньше?')
    def test_question_renew_or_return_scooter(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_renew_or_return_scooter)
        home_page.wait_element_clickable(question_renew_or_return_scooter)
        home_page.click_on_section(question_renew_or_return_scooter)
        home_page.wait_element_located(answer_renew_or_return_scooter)
        answer = home_page.get_text_of_element(answer_renew_or_return_scooter)
        assert answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')

    @allure.title('Проверка ответа на вопрос: Вы привозите зарядку вместе с самокатом?')
    def test_question_charging_with_scooter(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_charging_together_scooter)
        home_page.wait_element_clickable(question_charging_together_scooter)
        home_page.click_on_section(question_charging_together_scooter)
        home_page.wait_element_located(answer_charging_together_scooter)
        answer = home_page.get_text_of_element(answer_charging_together_scooter)
        assert answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                          'кататься без передышек и во сне. Зарядка не понадобится.')

    @allure.title('Проверка ответа на вопрос: Можно ли отменить заказ?')
    def test_question_cancel_order(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_cancel_order)
        home_page.wait_element_clickable(question_cancel_order)
        home_page.click_on_section(question_cancel_order)
        home_page.wait_element_located(answer_cancel_order)
        answer = home_page.get_text_of_element(answer_cancel_order)
        assert answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все '
                          'же свои.')

    @allure.title('Проверка ответа на вопрос: Я жизу за МКАДом, привезёте?')
    def test_question_about_moscow_ring_road(self):
        home_page = BasePage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(question_about_moscow_ring_road)
        home_page.wait_element_clickable(question_about_moscow_ring_road)
        home_page.click_on_section(question_about_moscow_ring_road)
        home_page.wait_element_located(answer_about_moscow_ring_road)
        answer = home_page.get_text_of_element(answer_about_moscow_ring_road)
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
