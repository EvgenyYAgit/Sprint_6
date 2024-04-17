from selenium import webdriver
from pages.order_scooter import OrderPage
from pages.basepage import BasePage
import pytest
import allure
from locators.order_scooter_locators import button_little_order, button_middle_order, button_big_order, \
    string_name, string_surname, string_address, \
    string_metro, string_phone_number, button_next, chapter_about_rent, string_when_bring_scooter, rental_period, \
    period_one_day, color_scooter_black, string_comment_for_courier, button_yes, windows_success_order, logo_scooter, \
    logo_yandex, scooter_title, dzen_button, button_see_status
from locators.url_base import site
from locators.order_scooter_test_data import date, comment_for_courier


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
        base_page = BasePage(self.driver)
        order_page = OrderPage(self.driver)
        base_page.get_site(site)
        base_page.scroll_element(button_big_order)
        base_page.wait_element_clickable(button_big_order)
        base_page.click_on_section(button_big_order)
        base_page.filling_string(string_name, name)
        base_page.filling_string(string_surname, surname)
        base_page.filling_string(string_address, address)
        order_page.selection_metro(string_metro, metro)
        base_page.filling_string(string_phone_number, phone_number)
        base_page.click_on_section(button_next)
        base_page.wait_element_located(chapter_about_rent)
        order_page.selection_date(string_when_bring_scooter, date)
        base_page.click_on_section(rental_period)
        base_page.click_on_section(period_one_day)
        base_page.click_on_section(color_scooter_black)
        base_page.filling_string(string_comment_for_courier, comment_for_courier)
        base_page.click_on_section(button_middle_order)
        base_page.click_on_section(button_yes)

        assert "Заказ оформлен" in base_page.get_text_of_element(windows_success_order)

        base_page.click_on_section(button_see_status)
        base_page.click_on_section(logo_scooter)
        base_page.wait_element_located(scooter_title)

        assert 'на пару дней' and 'Самокат' in base_page.get_text_of_element(scooter_title)

        base_page.click_on_section(logo_yandex)
        order_page.close_tab()
        order_page.switch_new_tab()
        base_page.wait_element_clickable(dzen_button)

        assert 'Найти' == base_page.get_text_of_element(dzen_button)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Александр', 'Мохов', 'Цветной бульвар', '89409232455', 'Ул.Московская, д.15'],
                              ['Анастасия', 'Крепильникова', 'Полянка', '99307700024', 'Ул.Большая, д.56']])
    def test_positive_case_order_button_top(self, name, surname, metro, phone_number, address):
        base_page = BasePage(self.driver)
        order_page = OrderPage(self.driver)
        base_page.get_site(site)
        base_page.wait_element_clickable(button_little_order)
        base_page.click_on_section(button_little_order)
        base_page.filling_string(string_name, name)
        base_page.filling_string(string_surname, surname)
        base_page.filling_string(string_address, address)
        order_page.selection_metro(string_metro, metro)
        base_page.filling_string(string_phone_number, phone_number)
        base_page.click_on_section(button_next)
        base_page.wait_element_located(chapter_about_rent)
        order_page.selection_date(string_when_bring_scooter, date)
        base_page.click_on_section(rental_period)
        base_page.click_on_section(period_one_day)
        base_page.click_on_section(color_scooter_black)
        base_page.filling_string(string_comment_for_courier, comment_for_courier)
        base_page.click_on_section(button_middle_order)
        base_page.click_on_section(button_yes)

        assert "Заказ оформлен" in base_page.get_text_of_element(windows_success_order)

        base_page.click_on_section(button_see_status)
        base_page.click_on_section(logo_scooter)
        base_page.wait_element_located(scooter_title)

        assert 'на пару дней' and 'Самокат' in base_page.get_text_of_element(scooter_title)

        base_page.click_on_section(logo_yandex)
        order_page.close_tab()
        order_page.switch_new_tab()
        base_page.wait_element_clickable(dzen_button)

        assert 'Найти' == base_page.get_text_of_element(dzen_button)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
