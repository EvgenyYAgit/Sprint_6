from selenium.webdriver.common.by import By

site = 'https://qa-scooter.praktikum-services.ru/'

section_questions = [By.XPATH, "//div[text()='Вопросы о важном']"] #секция Вопросы о важном

question_how_much_it_cost = [By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"] #первый вопрос
question_want_several_scooters = [By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']"] #второй вопрос
question_how_rental_time = [By.XPATH, "//div[text()='Как рассчитывается время аренды?']"] #третий вопрос
question_order_today = [By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']"] #четвертый вопрос
question_renew_or_return_scooter = [By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"] #пятый вопрос
question_charging_together_scooter = [By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']"] #шестой вопрос
question_cancel_order = [By.XPATH, "//div[text()='Можно ли отменить заказ?']"] #седьмой вопрос
question_about_moscow_ring_road = [By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']"] #восьмой вопрос

answer_how_much_it_cost = [By.XPATH, "//div[@id='accordion__panel-0']"] #первый ответ
answer_want_several_scooters = [By.XPATH, "//div[@id='accordion__panel-1']"] #второй ответ
answer_how_rental_time = [By.XPATH, "//div[@id='accordion__panel-2']"] #третий ответ
answer_order_today = [By.XPATH, "//div[@id='accordion__panel-3']"] #четвертый ответ
answer_renew_or_return_scooter = [By.XPATH, "//div[@id='accordion__panel-4']"] #пятый ответ
answer_charging_together_scooter = [By.XPATH, "//div[@id='accordion__panel-5']"] #шестой ответ
answer_cancel_order = [By.XPATH, "//div[@id='accordion__panel-6']"] #седьмой ответ
answer_about_moscow_ring_road = [By.XPATH, "//div[@id='accordion__panel-7']"] #восьмой ответ
