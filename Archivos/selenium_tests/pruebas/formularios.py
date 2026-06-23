from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
select.select_by_visible_text("Option 1")
time.sleep(2)
select.select_by_value("2")
time.sleep(2)

driver.get("https://the-internet.herokuapp.com/checkboxes")
checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input:nth-child(1)")
is_checked = checkbox.is_selected()
print("Casilla seleccionada: ", is_checked)

if not is_checked:
    checkbox.click()

time.sleep(2)

driver.get("https://the-internet.herokuapp.com/upload")
file_input = driver.find_element(By.ID, "file-upload")
file_path = r"C:\Users\ThinkPad\Downloads\QA_ENGENEER\Selenium+Python\Archivos\selenium_tests\pruebas\test.txt"
file_input.send_keys(file_path)
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()
time.sleep(3)

success_message = driver.find_element(By.TAG_NAME, "h3").text
print("Mensaje de éxito: ", success_message)