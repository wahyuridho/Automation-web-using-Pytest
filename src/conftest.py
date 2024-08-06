import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")    
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

def get_browser_version():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Menjalankan browser dalam mode headless
    driver = webdriver.Chrome(options=options)
    browser_version = driver.capabilities['browserVersion']
    driver.quit()
    return browser_version

@pytest.fixture(scope='session', autouse=True)
def create_environment_properties():
    browser_version = get_browser_version()
    allure_results_dir = 'allure-results'
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    environment_file = os.path.join(allure_results_dir, 'environment.properties')
    with open(environment_file, 'w') as file:
        file.write(f'Browser=Chrome\n')
        file.write(f'Browser.Version={browser_version}\n')
        file.write('OS=Windows 11\n')
