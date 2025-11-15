from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """
    Page Object для главной страницы Яндекс.Самокат
    """
    
    def click_order_button_top(self):
        """Клик на верхнюю кнопку 'Заказать'"""
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
        return self
    
    def click_order_button_bottom(self):
        """Клик на нижнюю кнопку 'Заказать'"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        return self
    
    def expand_question(self, question_number):
        """
        Раскрыть вопрос по номеру
        :param question_number: номер вопроса от 0 до 7
        """
        questions = {
            0: MainPageLocators.QUESTION_1,
            1: MainPageLocators.QUESTION_2,
            2: MainPageLocators.QUESTION_3,
            3: MainPageLocators.QUESTION_4,
            4: MainPageLocators.QUESTION_5,
            5: MainPageLocators.QUESTION_6,
            6: MainPageLocators.QUESTION_7,
            7: MainPageLocators.QUESTION_8
        }
        
        question_locator = questions.get(question_number)
        if question_locator:
            self.scroll_to_element(question_locator)
            self.click_element(question_locator)
        else:
            raise ValueError(f"Вопрос с номером {question_number} не найден. Допустимые значения: 0-7")
        
        return self
    
    def get_answer_text(self, question_number):
        """
        Получить текст ответа на вопрос
        :param question_number: номер вопроса от 0 до 7
        """
        answers = {
            0: MainPageLocators.ANSWER_1,
            1: MainPageLocators.ANSWER_2,
            2: MainPageLocators.ANSWER_3,
            3: MainPageLocators.ANSWER_4,
            4: MainPageLocators.ANSWER_5,
            5: MainPageLocators.ANSWER_6,
            6: MainPageLocators.ANSWER_7,
            7: MainPageLocators.ANSWER_8
        }
        
        answer_locator = answers.get(question_number)
        if answer_locator:
            return self.get_text(answer_locator)
        else:
            raise ValueError(f"Ответ для вопроса {question_number} не найден")
    
    def click_scooter_logo(self):
        """Клик на логотип Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)
        return self
    
    def click_yandex_logo(self):
        """Клик на логотип Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)
        return self
    
    def wait_for_page_load(self):
        """Ожидание загрузки главной страницы"""
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON_TOP))
        return self
    
    def is_order_button_visible(self):
        """Проверка видимости кнопки заказа"""
        return self.is_element_visible(MainPageLocators.ORDER_BUTTON_TOP)
    
    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title