from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class BasePage:
    """
    Базовый класс для всех Page Objects
    """
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator, timeout=None):
        """Найти все элементы с ожиданием"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))
    
    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator, timeout=None):
        """Кликнуть по элементу"""
        element = self.find_element(locator, timeout)
        element.click()
    
    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def input_text(self, locator, text, timeout=None):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=None):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text
    
    @allure.step("Получить атрибут '{attribute}' элемента {locator}")
    def get_attribute(self, locator, attribute, timeout=None):
        """Получить атрибут элемента"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)
    
    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=None):
        """Проверить видимость элемента"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проверить кликабельность элемента {locator}")
    def is_element_clickable(self, locator, timeout=None):
        """Проверить кликабельность элемента"""
        try:
            wait_timeout = timeout or self.timeout
            wait = WebDriverWait(self.driver, wait_timeout)
            wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проскроллить к элементу {locator}")
    def scroll_to_element(self, locator, timeout=None):
        """Проскроллить к элементу"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Ожидать появления текста '{text}' в URL")
    def wait_for_url_contains(self, text, timeout=None):
        """Ожидать появления текста в URL"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        wait.until(EC.url_contains(text))
    
    @allure.step("Получить текущее окно")
    def get_current_window(self):
        """Получить handle текущего окна"""
        return self.driver.current_window_handle
    
    @allure.step("Получить все окна")
    def get_all_windows(self):
        """Получить handles всех окон"""
        return self.driver.window_handles
    
    @allure.step("Ожидать открытия нового окна")
    def wait_for_new_window(self, timeout=None):
        """Ожидать открытия нового окна"""
        original_windows = self.get_all_windows()
        
        def new_window_opened(driver):
            current_windows = self.get_all_windows()
            return len(current_windows) > len(original_windows)
        
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        wait.until(new_window_opened)
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        """Переключиться на новое окно (последнее открытое)"""
        windows = self.get_all_windows()
        if len(windows) > 1:
            self.driver.switch_to.window(windows[-1])
    
    @allure.step("Закрыть текущее окно и переключиться на {window_index}")
    def close_current_window_and_switch_to(self, window_index=0):
        """Закрыть текущее окно и переключиться на указанное"""
        self.driver.close()
        windows = self.get_all_windows()
        if window_index < len(windows):
            self.driver.switch_to.window(windows[window_index])
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url