from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    """
    Базовый класс для всех Page Objects
    """
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout
    
    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator, timeout=None):
        """Найти все элементы с ожиданием"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click_element(self, locator, timeout=None):
        """Кликнуть по элементу"""
        element = self.find_element(locator, timeout)
        element.click()
        return self
    
    def input_text(self, locator, text, timeout=None):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return self
    
    def get_text(self, locator, timeout=None):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def get_attribute(self, locator, attribute, timeout=None):
        """Получить атрибут элемента"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)
    
    def is_element_visible(self, locator, timeout=None):
        """Проверить видимость элемента"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_clickable(self, locator, timeout=None):
        """Проверить кликабельность элемента"""
        try:
            wait_timeout = timeout or self.timeout
            wait = WebDriverWait(self.driver, wait_timeout)
            wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator, timeout=None):
        """Проскроллить к элементу"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self
    
    def wait_for_url_contains(self, text, timeout=None):
        """Ожидать появления текста в URL"""
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        wait.until(EC.url_contains(text))
        return self
    
    def switch_to_window(self, window_index):
        """Переключиться на окно по индексу"""
        windows = self.driver.window_handles
        if window_index < len(windows):
            self.driver.switch_to.window(windows[window_index])
        return self
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url