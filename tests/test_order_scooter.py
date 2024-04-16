from selenium import webdriver
from pages.order_scooter import HomePage, OrderPage
import pytest
import allure
from locators.order_scooter_locators import site, button_little_order, button_middle_order, button_big_order, \
    string_name, string_surname, string_address, \
    string_metro, string_phone_number, button_next, chapter_about_rent, string_when_bring_scooter, rental_period, \
    period_one_day, color_scooter_black, string_comment_for_courier, button_yes, windows_success_order, logo_scooter, \
    logo_yandex, scooter_title, dzen_button, date, comment_for_courier, \
    button_see_status


class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" внизу.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Евгений', 'Бородинов', 'Цветной бульвар', '89209234455', 'Ул.Академика Анохина, д.9'],
                              ['Владлена', 'Космодемьянская', 'Полянка', '99307749024', 'Ул.Шоколадная, д.55']])
    def test_positive_case_order_button_below(self, name, surname, metro, phone_number, address):
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        home_page.get_site(site)
        home_page.scroll_element(button_big_order)
        home_page.wait_element_clickable(button_big_order)
        home_page.click_on_section(button_big_order)
        order_page.filling_string(string_name, name)
        order_page.filling_string(string_surname, surname)
        order_page.filling_string(string_address, address)
        order_page.selection_metro(string_metro, metro)
        order_page.filling_string(string_phone_number, phone_number)
        order_page.click_on_section(button_next)
        order_page.wait_element_located(chapter_about_rent)
        order_page.selection_date(string_when_bring_scooter, date)
        order_page.click_on_section(rental_period)
        order_page.click_on_section(period_one_day)
        order_page.click_on_section(color_scooter_black)
        order_page.filling_string(string_comment_for_courier, comment_for_courier)
        order_page.click_on_section(button_middle_order)
        order_page.click_on_section(button_yes)

        assert "Заказ оформлен" in order_page.get_text_of_element(windows_success_order)

        order_page.click_on_section(button_see_status)
        order_page.click_on_section(logo_scooter)
        order_page.wait_element_located(scooter_title)

        assert 'на пару дней' and 'Самокат' in order_page.get_text_of_element(scooter_title)

        order_page.click_on_section(logo_yandex)
        order_page.close_tab()
        order_page.switch_new_tab()
        order_page.wait_element_clickable(dzen_button)

        assert 'Найти' == order_page.get_text_of_element(dzen_button)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Александр', 'Мохов', 'Цветной бульвар', '89409232455', 'Ул.Московская, д.15'],
                              ['Анастасия', 'Крепильникова', 'Полянка', '99307700024', 'Ул.Большая, д.56']])
    def test_positive_case_order_button_top(self, name, surname, metro, phone_number, address):
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        home_page.get_site(site)
        home_page.wait_element_clickable(button_little_order)
        home_page.click_on_section(button_little_order)
        order_page.filling_string(string_name, name)
        order_page.filling_string(string_surname, surname)
        order_page.filling_string(string_address, address)
        order_page.selection_metro(string_metro, metro)
        order_page.filling_string(string_phone_number, phone_number)
        order_page.click_on_section(button_next)
        order_page.wait_element_located(chapter_about_rent)
        order_page.selection_date(string_when_bring_scooter, date)
        order_page.click_on_section(rental_period)
        order_page.click_on_section(period_one_day)
        order_page.click_on_section(color_scooter_black)
        order_page.filling_string(string_comment_for_courier, comment_for_courier)
        order_page.click_on_section(button_middle_order)
        order_page.click_on_section(button_yes)

        assert "Заказ оформлен" in order_page.get_text_of_element(windows_success_order)

        order_page.click_on_section(button_see_status)
        order_page.click_on_section(logo_scooter)
        order_page.wait_element_located(scooter_title)

        assert 'на пару дней' and 'Самокат' in order_page.get_text_of_element(scooter_title)

        order_page.click_on_section(logo_yandex)
        order_page.close_tab()
        order_page.switch_new_tab()
        order_page.wait_element_clickable(dzen_button)

        assert 'Найти' == order_page.get_text_of_element(dzen_button)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
