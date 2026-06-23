from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

logging.info("Iniciando la prueba de saucedemo")

driver.get("https://www.saucedemo.com/")
logging.info("Ingresando el usuario")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
logging.info("Ingresando la contraseña")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
logging.info("Iniciando sesion con el boton login")
driver.find_element(By.ID, "login-button").click()

logging.info("Tomando captura de pantalla")
driver.save_screenshot("login_success.png")

logging.info("Finalizando la prueba")
driver.quit()
