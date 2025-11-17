import pytest
import allure
from pages.main_page import MainPage

@allure.epic("Навигация Яндекс.Самокат")
class TestPageTransfer:
    
    @allure.feature("Логотипы")
    @allure.story("Переход на главную через логотип Самоката")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirect_to_main(self, driver):
        """
        Проверка что клик на логотип Самоката возвращает на главную страницу
        """
        main_page = MainPage(driver)
        
        with allure.step("Переходим на страницу заказа"):
            main_page.click_order_button_top()
            order_page_url = main_page.get_current_url()
        
        with allure.step("Кликаем на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем что вернулись на главную"):
            main_page.wait_for_page_load()
            current_url = main_page.get_current_url()
            assert "qa-scooter" in current_url, \
                f"Не произошел переход на главную. Текущий URL: {current_url}"
            assert current_url != order_page_url, "URL не изменился после клика на логотип"
    
    @allure.feature("Логотипы") 
    @allure.story("Переход на Дзен через логотип Яндекса")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect_to_dzen(self, driver):
        """
        Проверка что клик на логотип Яндекса открывает Дзен в новом окне
        """
        main_page = MainPage(driver)
        
        with allure.step("Кликаем на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Ожидаем открытия нового окна"):
            main_page.wait_for_new_window()
        
        with allure.step("Переключаемся на новое окно"):
            main_page.switch_to_new_window()
        
        with allure.step("Проверяем что открылся Дзен"):
            main_page.wait_for_url_contains("dzen.ru", timeout=15)
            current_url = main_page.get_current_url()
            assert "dzen.ru" in current_url, \
                f"Открылся не Дзен. Текущий URL: {current_url}"
            
        # Убрали лишние шаги закрытия окна