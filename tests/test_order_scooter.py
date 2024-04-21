from pages.order_scooter import OrderPage
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
        order_page = OrderPage(start_and_stop_browser)
        order_page.get_site(site)

        order_page.search_element_and_click(locators.order_scooter_locators.button_big_order)

        order_page.filling_who_is_scooter_for(locators.order_scooter_locators.string_name, name,
                                              locators.order_scooter_locators.string_surname, surname,
                                              locators.order_scooter_locators.string_address, address,
                                              locators.order_scooter_locators.string_phone_number, phone_number,
                                              locators.order_scooter_locators.string_metro, metro)

        order_page.click_and_wait_element(locators.order_scooter_locators.button_next,
                                          locators.order_scooter_locators.chapter_about_rent)

        order_page.filling_about_rent(locators.order_scooter_locators.rental_period,
                                      locators.order_scooter_locators.period_one_day,
                                      locators.order_scooter_locators.color_scooter_black,
                                      locators.order_scooter_locators.string_when_bring_scooter, date,
                                      locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)

        order_page.click_on_section(locators.order_scooter_locators.button_middle_order)
        order_page.click_on_section(locators.order_scooter_locators.button_yes)

        assert "Заказ оформлен" in order_page.get_text_of_element(locators.order_scooter_locators.windows_success_order)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Александр', 'Мохов', 'Цветной бульвар', '89409232455', 'Ул.Московская, д.15'],
                              ['Анастасия', 'Крепильникова', 'Полянка', '99307700024', 'Ул.Большая, д.56']])
    def test_order_button_top_yandex_page(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.get_site(site)

        order_page.wait_element_and_click(locators.order_scooter_locators.button_little_order)

        order_page.filling_who_is_scooter_for(locators.order_scooter_locators.string_name, name,
                                              locators.order_scooter_locators.string_surname, surname,
                                              locators.order_scooter_locators.string_address, address,
                                              locators.order_scooter_locators.string_phone_number, phone_number,
                                              locators.order_scooter_locators.string_metro, metro)

        order_page.click_and_wait_element(locators.order_scooter_locators.button_next,
                                          locators.order_scooter_locators.chapter_about_rent)

        order_page.filling_about_rent(locators.order_scooter_locators.rental_period,
                                      locators.order_scooter_locators.period_one_day,
                                      locators.order_scooter_locators.color_scooter_black,
                                      locators.order_scooter_locators.string_when_bring_scooter, date,
                                      locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)

        order_page.valid_purchase(locators.order_scooter_locators.button_middle_order,
                                  locators.order_scooter_locators.button_yes,
                                  locators.order_scooter_locators.button_see_status)

        order_page.click_on_section(locators.order_scooter_locators.logo_scooter)
        order_page.wait_element_located(locators.order_scooter_locators.scooter_title)

        assert 'на пару дней' and 'Самокат' in order_page.get_text_of_element(
            locators.order_scooter_locators.scooter_title)

    @allure.title('Проверка позитивного сценария с двумя наборами данных. Точка входа кнопка "Заказать" сверху.')
    @pytest.mark.parametrize('name, surname, metro, phone_number, address',
                             [['Виталий', 'Громов', 'Цветной бульвар', '89509232455', 'Ул.Ленина, д.45'],
                              ['Роза', 'Курилова', 'Полянка', '99307710024', 'Ул.Маленькая, д.156']])
    def test_order_button_top_dzen_page(self, name, surname, metro, phone_number, address, start_and_stop_browser):
        order_page = OrderPage(start_and_stop_browser)
        order_page.get_site(site)

        order_page.wait_element_and_click(locators.order_scooter_locators.button_little_order)

        order_page.filling_who_is_scooter_for(locators.order_scooter_locators.string_name, name,
                                              locators.order_scooter_locators.string_surname, surname,
                                              locators.order_scooter_locators.string_address, address,
                                              locators.order_scooter_locators.string_phone_number, phone_number,
                                              locators.order_scooter_locators.string_metro, metro)

        order_page.click_and_wait_element(locators.order_scooter_locators.button_next,
                                          locators.order_scooter_locators.chapter_about_rent)

        order_page.filling_about_rent(locators.order_scooter_locators.rental_period,
                                      locators.order_scooter_locators.period_one_day,
                                      locators.order_scooter_locators.color_scooter_black,
                                      locators.order_scooter_locators.string_when_bring_scooter, date,
                                      locators.order_scooter_locators.string_comment_for_courier, comment_for_courier)

        order_page.valid_purchase(locators.order_scooter_locators.button_middle_order,
                                  locators.order_scooter_locators.button_yes,
                                  locators.order_scooter_locators.button_see_status)
        order_page.dzen(locators.order_scooter_locators.logo_yandex, locators.order_scooter_locators.dzen_button)

        assert 'Найти' == order_page.get_text_of_element(locators.order_scooter_locators.dzen_button)
