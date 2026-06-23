from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
user_field_by_id = driver.find_element(By.ID, "user-name")
user_field_by_name = driver.find_element(By.NAME, "user-name")
user_field_by_css = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_field_by_xpath = driver.find_element(By.XPATH, '//*[@id="user-name"]')

print("Elemento encontrado por ID: ", user_field_by_id.get_attribute("id"))
time.sleep(3)
driver.quit()


