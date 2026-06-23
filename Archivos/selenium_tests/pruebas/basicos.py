from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
user_field = driver.find_element(By.ID, "user-name")
user_field.send_keys("standard_user")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

title = driver.find_element(By.CLASS_NAME, "title")
title_text = title.text
print("Titulo de la pagina: ", title_text)

driver.quit()