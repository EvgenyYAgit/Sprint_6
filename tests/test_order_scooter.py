from pages.order_scooter import OrderPage
from pages.basepage import BasePage
import pytest
import allure
import locators.order_scooter_locators
from locators.url_base import site
from locators.order_scooter_test_data import date, comment_for_courier


class TestOrderScooter:
    driver = None

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" внизу.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Евгений', 'Бородинов', 'Цветной бульвар', '89209234455', 'Ул.Академика Анохина, д.9'],
                              ['Владлена', 'Космодемьянская', 'Полянка', '99307749024', 'Ул.Шоколадная, д.55']])
    def test_order_button_below_order_access(self, name, surname, metro, phone_number, address,
                                             start_and_stop_browser):
        base_page = BasePage(start_and_stop_browser)
        order_page = OrderPage(start_and_stop_browser)
        base_page.get_site(site)
        base_page.scroll_element(locators.order_scooter_locators.button_big_order)
        base_page.wait_element_clickable(locators.order_scooter_locators.button_big_order)
        base_page.click_on_section(locators.order_scooter_locators.button_big_order)
        base_page.filling_string(locators.order_scooter_locators.string_name, name)
        base_page.filling_string(locators.order_scooter_locators.string_surname, surname)
        base_page.filling_string(locators.order_scooter_locators.string_address, address)
        order_page.selection_metro(locators.order_scooter_locators.string_metro, metro)
        base_page.filling_string(locators.order_scooter_locators.string_phone_number, phone_number)
        base_page.click_on_section(locators.order_scooter_locators.button_next)
        base_page.wait_element_located(locators.order_scooter_locators.chapter_about_rent)
        order_page.selection_date(locators.order_scooter_locators.string_when_bring_scooter, date)
        base_page.click_on_section(locators.order_scooter_locators.rental_period)
        base_page.click_on_section(locators.order_scooter_locators.period_one_day)
        base_page.click_on_section(locators.order_scooter_locators.color_scooter_black)
        base_page.filling_string(locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)
        base_page.click_on_section(locators.order_scooter_locators.button_middle_order)
        base_page.click_on_section(locators.order_scooter_locators.button_yes)

        assert "Заказ оформлен" in base_page.get_text_of_element(locators.order_scooter_locators.windows_success_order)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Александр', 'Мохов', 'Цветной бульвар', '89409232455', 'Ул.Московская, д.15'],
                              ['Анастасия', 'Крепильникова', 'Полянка', '99307700024', 'Ул.Большая, д.56']])
    def test_order_button_top_yandex_page(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        base_page = BasePage(start_and_stop_browser)
        order_page = OrderPage(start_and_stop_browser)
        base_page.get_site(site)
        base_page.wait_element_clickable(locators.order_scooter_locators.button_little_order)
        base_page.click_on_section(locators.order_scooter_locators.button_little_order)
        base_page.filling_string(locators.order_scooter_locators.string_name, name)
        base_page.filling_string(locators.order_scooter_locators.string_surname, surname)
        base_page.filling_string(locators.order_scooter_locators.string_address, address)
        order_page.selection_metro(locators.order_scooter_locators.string_metro, metro)
        base_page.filling_string(locators.order_scooter_locators.string_phone_number, phone_number)
        base_page.click_on_section(locators.order_scooter_locators.button_next)
        base_page.wait_element_located(locators.order_scooter_locators.chapter_about_rent)
        order_page.selection_date(locators.order_scooter_locators.string_when_bring_scooter, date)
        base_page.click_on_section(locators.order_scooter_locators.rental_period)
        base_page.click_on_section(locators.order_scooter_locators.period_one_day)
        base_page.click_on_section(locators.order_scooter_locators.color_scooter_black)
        base_page.filling_string(locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)
        base_page.click_on_section(locators.order_scooter_locators.button_middle_order)
        base_page.click_on_section(locators.order_scooter_locators.button_yes)
        base_page.click_on_section(locators.order_scooter_locators.button_see_status)
        base_page.click_on_section(locators.order_scooter_locators.logo_scooter)
        base_page.wait_element_located(locators.order_scooter_locators.scooter_title)

        assert 'на пару дней' and 'Самокат' in base_page.get_text_of_element(locators.order_scooter_locators.scooter_title)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Виталий', 'Громов', 'Цветной бульвар', '89509232455', 'Ул.Ленина, д.45'],
                              ['Роза', 'Курилова', 'Полянка', '99307710024', 'Ул.Маленькая, д.156']])
    def test_order_button_top_dzen_page(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        base_page = BasePage(start_and_stop_browser)
        order_page = OrderPage(start_and_stop_browser)
        base_page.get_site(site)
        base_page.wait_element_clickable(locators.order_scooter_locators.button_little_order)
        base_page.click_on_section(locators.order_scooter_locators.button_little_order)
        base_page.filling_string(locators.order_scooter_locators.string_name, name)
        base_page.filling_string(locators.order_scooter_locators.string_surname, surname)
        base_page.filling_string(locators.order_scooter_locators.string_address, address)
        order_page.selection_metro(locators.order_scooter_locators.string_metro, metro)
        base_page.filling_string(locators.order_scooter_locators.string_phone_number, phone_number)
        base_page.click_on_section(locators.order_scooter_locators.button_next)
        base_page.wait_element_located(locators.order_scooter_locators.chapter_about_rent)
        order_page.selection_date(locators.order_scooter_locators.string_when_bring_scooter, date)
        base_page.click_on_section(locators.order_scooter_locators.rental_period)
        base_page.click_on_section(locators.order_scooter_locators.period_one_day)
        base_page.click_on_section(locators.order_scooter_locators.color_scooter_black)
        base_page.filling_string(locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)
        base_page.click_on_section(locators.order_scooter_locators.button_middle_order)
        base_page.click_on_section(locators.order_scooter_locators.button_yes)
        base_page.click_on_section(locators.order_scooter_locators.button_see_status)
        base_page.click_on_section(locators.order_scooter_locators.logo_yandex)
        order_page.close_tab()
        order_page.switch_new_tab()
        base_page.wait_element_clickable(locators.order_scooter_locators.dzen_button)

        assert 'Найти' == base_page.get_text_of_element(locators.order_scooter_locators.dzen_button)
