from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#espera impicita
#driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
user_field = driver.find_element(By.ID, "user-name")
user_field.send_keys("standard_user")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
title_text = title.text
print("Titulo: ", title_text)

driver.quit()




