from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    """
    Page Object для страницы оформления заказа Яндекс.Самокат
    """
    
    @allure.step("Ожидание загрузки страницы заказа")
    def wait_for_order_page_load(self):
        """Ожидание загрузки страницы заказа"""
        self.find_element(OrderPageLocators.NAME_INPUT)
    
    @allure.step("Заполнить поле 'Имя' значением '{name}'")
    def fill_name(self, name):
        """Заполнить поле 'Имя'"""
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        return self
    
    @allure.step("Заполнить поле 'Фамилия' значением '{surname}'")
    def fill_surname(self, surname):
        """Заполнить поле 'Фамилия'"""
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        return self
    
    @allure.step("Заполнить поле 'Адрес' значением '{address}'")
    def fill_address(self, address):
        """Заполнить поле 'Адрес'"""
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        return self
    
    @allure.step("Выбрать станцию метро '{station_name}'")
    def select_metro_station(self, station_name):
        """
        Выбрать станцию метро
        :param station_name: название станции метро
        """
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        self.input_text(OrderPageLocators.METRO_SEARCH_INPUT, station_name)
        self.click_element(OrderPageLocators.METRO_STATION_OPTION)
        return self
    
    @allure.step("Заполнить поле 'Телефон' значением '{phone}'")
    def fill_phone(self, phone):
        """Заполнить поле 'Телефон'"""
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        return self
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        """Нажать кнопку 'Далее'"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        return self
    
    @allure.step("Заполнить информацию о заказчике")
    def fill_customer_info(self, name, surname, address, metro_station, phone):
        """
        Заполнить всю информацию о заказчике
        """
        self.fill_name(name)\
            .fill_surname(surname)\
            .fill_address(address)\
            .select_metro_station(metro_station)\
            .fill_phone(phone)\
            .click_next_button()
        return self
    
    @allure.step("Ожидание загрузки формы аренды")
    def wait_for_rent_form_load(self):
        """Ожидание загрузки формы аренды"""
        self.find_element(OrderPageLocators.DATE_INPUT)
    
    @allure.step("Заполнить дату доставки '{date}'")
    def fill_delivery_date(self, date):
        """Заполнить поле 'Когда привезти самокат'"""
        self.input_text(OrderPageLocators.DATE_INPUT, date)
        return self
    
    @allure.step("Выбрать срок аренды '{period}'")
    def select_rental_period(self, period):
        """
        Выбрать срок аренды
        :param period: срок аренды ('сутки', 'двое суток', и т.д.)
        """
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        
        period_locators = {
            'сутки': OrderPageLocators.RENTAL_1_DAY,
            'двое суток': OrderPageLocators.RENTAL_2_DAYS,
            'трое суток': OrderPageLocators.RENTAL_3_DAYS,
            'четверо суток': OrderPageLocators.RENTAL_4_DAYS,
            'пятеро суток': OrderPageLocators.RENTAL_5_DAYS,
            'шестеро суток': OrderPageLocators.RENTAL_6_DAYS,
            'семеро суток': OrderPageLocators.RENTAL_7_DAYS
        }
        
        period_locator = period_locators.get(period)
        if period_locator:
            self.click_element(period_locator)
        else:
            raise ValueError(f"Период аренды '{period}' не поддерживается")
        return self
    
    @allure.step("Выбрать цвет самоката '{color}'")
    def select_scooter_color(self, color):
        """
        Выбрать цвет самоката
        :param color: цвет ('black', 'grey')
        """
        color_locators = {
            'black': OrderPageLocators.BLACK_CHECKBOX,
            'grey': OrderPageLocators.GREY_CHECKBOX
        }
        
        color_locator = color_locators.get(color)
        if color_locator:
            self.click_element(color_locator)
        else:
            raise ValueError(f"Цвет '{color}' не поддерживается")
        return self
    
    @allure.step("Заполнить комментарий для курьера '{comment}'")
    def fill_comment(self, comment):
        """Заполнить поле 'Комментарий для курьера'"""
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
        return self
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        """Нажать кнопку 'Заказать'"""
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        return self
    
    @allure.step("Заполнить информацию об аренде")
    def fill_rent_info(self, date, rental_period, color=None, comment=None):
        """
        Заполнить всю информацию об аренде
        """
        self.fill_delivery_date(date)\
            .select_rental_period(rental_period)
        
        if color:
            self.select_scooter_color(color)
        
        if comment:
            self.fill_comment(comment)
        
        self.click_order_button()
        return self
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        return self
    
    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        """Получить сообщение об успешном оформлении заказа"""
        self.find_element(OrderPageLocators.SUCCESS_MESSAGE)
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
    
    @allure.step("Проверить отображение сообщения об успехе")
    def is_success_message_displayed(self):
        """Проверить отображение сообщения об успехе"""
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
    
    @allure.step("Получить номер заказа")
    def get_order_number(self):
        """Получить номер заказа (если отображается)"""
        try:
            success_text = self.get_success_message()
            return success_text
        except:
            return None