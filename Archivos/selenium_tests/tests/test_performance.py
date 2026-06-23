import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from pages.login_page import LoginPage
from utils.config import load_config
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

config = load_config()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

start_time = time.time()
driver.get(config["base_url"])
loginPage = LoginPage(driver)

loginPage.set_username(config["valid_user"])
loginPage.set_password(config["valid_password"])
loginPage.click_login()
end_time = time.time()
load_time = end_time - start_time
print(f"Tiempo de carga de login:{load_time:2f} segundos")
driver.quit()

