import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class TestLoginScenario:
    @pytest.mark.validLogin
    def test_positif_login(self, browser: WebDriver):
        login = LoginPage(browser)
        login.open()
        login.inputCredential('standard_user','secret_sauce')
        login.submit()

        assert browser.current_url == 'https://www.saucedemo.com/inventory.html', "Url tidak sesuai"

    @pytest.mark.invalidLogin
    @pytest.mark.parametrize("username, password",[
        ('standard_user', 'invalid'),
        ('standard', 'secret_sauce'),
    ])
    def test_invalid_login(self, browser: WebDriver, username, password):
        login = LoginPage(browser)
        login.open()
        login.inputCredential(username, password)
        login.submit()
        
        message = login.getErrorMessage()
        assert message == 'Epic sadface: Username and password do not match any user in this service', 'Alert message tidak sesuai'

    @pytest.mark.blankLogin
    @pytest.mark.parametrize("username, password",[
        ('', 'invalid'),
        ('standard', ''),
        ('', ''),
    ])
    def test_blank_login(self, browser: WebDriver, username, password):
        login = LoginPage(browser)
        login.open()
        login.inputCredential(username, password)
        login.submit()
        
        message = login.getErrorMessage()
        if username == '':
            assert message == 'Epic sadface: Username is required', 'Alert message tidak sesuai'
        elif password == '':
            assert message == 'Epic sadface: Password is required', 'Alert message tidak sesuai'
        else:
            assert message == 'Epic sadface: Username is required', 'Alert message tidak sesuai'