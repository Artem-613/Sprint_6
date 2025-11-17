import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData

@allure.epic("Оформление заказа Яндекс.Самокат")
class TestMakeAnOrder:
    """
    Тесты для оформления заказа самоката
    """
    
    @allure.feature("Позитивные сценарии")
    @allure.story("Оформление заказа через верхнюю кнопку с разными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("order_data", [
        TestData.ORDER_DATA_1,
        TestData.ORDER_DATA_2
    ], ids=["Заказ 1", "Заказ 2"])
    def test_order_through_top_button_success(self, driver, order_data):
        """
        Успешное оформление заказа через верхнюю кнопку
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Нажимаем верхнюю кнопку заказа"):
            main_page.click_order_button_top()
        
        with allure.step("Заполняем информацию о заказчике"):
            order_page.wait_for_order_page_load()\
                .fill_customer_info(
                    order_data["name"],
                    order_data["surname"],
                    order_data["address"],
                    order_data["metro_station"],
                    order_data["phone"]
                )
        
        with allure.step("Заполняем информацию об аренде"):
            order_page.wait_for_rent_form_load()\
                .fill_rent_info(
                    order_data["date"],
                    order_data["rental_period"],
                    order_data["color"],
                    order_data["comment"]
                )
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверяем успешное оформление"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Сообщение об успехе не отображается. Текст: {success_message}"
    
    @allure.feature("Позитивные сценарии")
    @allure.story("Оформление заказа через нижнюю кнопку")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_through_bottom_button_success(self, driver):
        """
        Успешное оформление заказа через нижнюю кнопку
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Нажимаем нижнюю кнопку заказа"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполняем информацию о заказчике"):
            order_page.wait_for_order_page_load()\
                .fill_customer_info(
                    "Анна",
                    "Кузнецова", 
                    "ул. Пушкина, д. 10",
                    "Лубянка",
                    "+79995554433"
                )
        
        with allure.step("Заполняем информацию об аренде"):
            order_page.wait_for_rent_form_load()\
                .fill_rent_info(
                    "18.12.2024",
                    "двое суток",
                    "grey",
                    "Позвонить за 30 минут"
                )
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверяем успешное оформление"):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном оформлении заказа не отображается"