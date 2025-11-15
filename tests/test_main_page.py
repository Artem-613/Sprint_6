import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.epic("Главная страница Яндекс.Самокат")
class TestMainPage:
    """
    Тесты для главной страницы Яндекс.Самокат
    """
    
    @allure.feature("Раздел 'Вопросы о важном'")
    @allure.story("Проверка корректности ответов на вопросы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_number,expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_question_answer_display(self, driver, question_number, expected_answer):
        """
        Проверка отображения правильных ответов на вопросы
        """
        main_page = MainPage(driver)
        
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
            assert main_page.is_element_visible(MainPageLocators.ORDER_BUTTON_TOP), "Верхняя кнопка заказа не видна"
        
        with allure.step("Проверяем видимость нижней кнопки заказа"):
            main_page.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
            assert main_page.is_element_visible(MainPageLocators.ORDER_BUTTON_BOTTOM), \
                "Нижняя кнопка заказа не видна"