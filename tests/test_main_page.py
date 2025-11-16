import pytest
import allure
from pages.main_page import MainPage
from data import FAQAnswers

class TestMainPage:
    
    @allure.feature("Раздел 'Вопросы о важном'")
    @allure.story("Проверка корректности ответов на вопросы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_number", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answer_display(self, driver, question_number):
        """
        Проверка отображения правильных ответов на вопросы
        """
        main_page = MainPage(driver)
        expected_answer = FAQAnswers.ANSWERS[question_number]
        
        with allure.step(f"Кликаем на вопрос номер {question_number + 1}"):
            main_page.expand_question(question_number)
        
        with allure.step("Получаем текст ответа"):
            actual_answer = main_page.get_answer_text(question_number)
        
        with allure.step("Сравниваем с ожидаемым ответом"):
            assert actual_answer == expected_answer, \
                f"Ошибка в ответе на вопрос {question_number + 1}\n" \
                f"Ожидалось: {expected_answer}\n" \
                f"Получено: {actual_answer}"
    
    @allure.feature("Кнопки заказа")
    @allure.story("Проверка доступности кнопок заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_buttons_availability(self, driver):
        """
        Проверка что обе кнопки заказа доступны на главной странице
        """
        main_page = MainPage(driver)
        
        with allure.step("Проверяем видимость верхней кнопки заказа"):
            assert main_page.is_order_button_visible(), "Верхняя кнопка заказа не видна"  # ← используем метод Page-класса
        
        with allure.step("Проверяем видимость нижней кнопки заказа"):
            assert main_page.is_order_button_bottom_visible(), "Нижняя кнопка заказа не видна"  # ← нужно добавить этот метод