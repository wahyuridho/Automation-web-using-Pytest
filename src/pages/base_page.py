from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((by, value)))
    