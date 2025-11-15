import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import allure

@pytest.fixture
def driver():
    # Настройка Firefox драйвера
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    # Переход на сайт Яндекс.Самокат
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    
    yield driver
    
    # Закрытие браузера после теста
    driver.quit()

# Создание скриншотов при падении тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to make screenshot: {e}")