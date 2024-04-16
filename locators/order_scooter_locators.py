from selenium.webdriver.common.by import By

site = 'https://qa-scooter.praktikum-services.ru/'
date = "15.05.2024" #дата аренды
comment_for_courier = "Позвоните за час до приезда" #комментарий

button_big_order = [By.XPATH, "//div[5]/button[text()='Заказать']"] #кнопка заказать большая
button_middle_order = [By.XPATH, "//div[3]/button[2][text()='Заказать']"] #кнопка заказать средняя
button_little_order = [By.XPATH, "//div[2]/button[1][text()='Заказать']"] #кнопка заказать маленькая

string_name = [By.XPATH, "//input[@placeholder='* Имя']"] #строка Имя
string_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"] #строка Фамилия
string_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] #строка адрес
string_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"] #строка станция метро
string_phone_number = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] #строка телефон
button_next = [By.XPATH, "//button[text()='Далее']"] #кнопка далее

chapter_about_rent = [By.XPATH, "//div[text()='Про аренду']"] #заголовок про аренду
string_when_bring_scooter = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"] #строка когда привезти самокат
rental_period = [By.XPATH, "//div[text()='* Срок аренды']"] #календарь срок аренды
period_one_day = [By.XPATH, "//div[text()='сутки']"] #период аренды
color_scooter_black = [By.XPATH, "//input[@id='black']"] #цвет скутера
string_comment_for_courier = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]#строка для коментарий
button_yes = [By.XPATH, "//button[text()='Да']"] #кнопка Да
windows_success_order = [By.XPATH, "//div[text()='Заказ оформлен']"] #оповещение заказ оформлен

logo_scooter = [By.XPATH, "//img[@alt='Scooter']"] #логотип самоката
logo_yandex = [By.XPATH, "//img[@alt='Yandex']"] #логотип яндекса
scooter_title = [By.XPATH, "//div[text()='Самокат ']"] #заголовок главной страницы самоката
dzen_button = [By.XPATH, "//button[text()='Найти']"] #кнопка найти на дзене
button_see_status = [By.XPATH, "//button[text()='Посмотреть статус']"] #кнопка посмотреть статус
