import os
import pytest
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
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as driver:
        return driver.capabilities['browserVersion']

@pytest.fixture(scope='session', autouse=True)
def create_environment_properties():
    browser_version = get_browser_version()
    allure_results_dir = 'allure-results'
    os.makedirs(allure_results_dir, exist_ok=True)

    with open(os.path.join(allure_results_dir, 'environment.properties'), 'w') as file:
        file.write(f'Browser=Chrome\n')
        file.write(f'Browser.Version={browser_version}\n')
        file.write('OS=Windows 11\n')
