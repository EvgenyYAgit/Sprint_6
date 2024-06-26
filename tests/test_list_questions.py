from pages.homepage import HomePage
import allure
import locators.list_questions_locators
from locators.url_base import site


class TestListQuestions:
    driver = None

    @allure.title('Проверка ответа на вопрос: Сколько это стоит? И как оплатить?')
    def test_question_how_much_it_cost(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(locators.list_questions_locators.question_how_much_it_cost,
                                                           locators.list_questions_locators.answer_how_much_it_cost)
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка ответа на вопрос: Хочу сразу несколько самокатов! Так можно?')
    def test_question_want_several_scooters(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_want_several_scooters,
            locators.list_questions_locators.answer_want_several_scooters)
        assert answer == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')

    @allure.title('Проверка ответа на вопрос: Как рассчитывается время аренды?')
    def test_question_how_rental_time(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_how_rental_time,
            locators.list_questions_locators.answer_how_rental_time)
        assert answer == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка ответа на вопрос: Можно ли заказать самокат прямо на сегодня?')
    def test_question_order_today(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_order_today,
            locators.list_questions_locators.answer_order_today)
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка ответа на вопрос: Можно ли продлить заказ или вернуть самокат раньше?')
    def test_question_renew_or_return_scooter(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_renew_or_return_scooter,
            locators.list_questions_locators.answer_renew_or_return_scooter)
        assert answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')

    @allure.title('Проверка ответа на вопрос: Вы привозите зарядку вместе с самокатом?')
    def test_question_charging_with_scooter(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_charging_together_scooter,
            locators.list_questions_locators.answer_charging_together_scooter)
        assert answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                          'кататься без передышек и во сне. Зарядка не понадобится.')

    @allure.title('Проверка ответа на вопрос: Можно ли отменить заказ?')
    def test_question_cancel_order(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_cancel_order,
            locators.list_questions_locators.answer_cancel_order)
        assert answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все '
                          'же свои.')

    @allure.title('Проверка ответа на вопрос: Я жизу за МКАДом, привезёте?')
    def test_question_about_moscow_ring_road(self, start_and_stop_browser):
        home_page = HomePage(start_and_stop_browser)
        home_page.get_site(site)
        answer = home_page.search_question_and_open_answer(
            locators.list_questions_locators.question_about_moscow_ring_road,
            locators.list_questions_locators.answer_about_moscow_ring_road)
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
