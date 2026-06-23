import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from pages.login_page import LoginPage
from utils.config import load_config

config = load_config()

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu") # desactivar la gpu
    chrome_options.add_argument("--window-size=1920,1080") # configuracion de la pantalla
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_headless(driver):
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.set_username(config["valid_user"])
    login_page.set_password(config["valid_password"])
    login_page.click_login()
    assert login_page.get_title() == "Products"
