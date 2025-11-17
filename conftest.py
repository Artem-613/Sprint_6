import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from urls import Urls  # добавляем импорт

@pytest.fixture
def driver():
    # Настройка Firefox драйвера
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    # Используем URL из внешнего модуля
    driver.get(Urls.BASE_URL)
    
    driver.maximize_window()
    yield driver
    driver.quit()