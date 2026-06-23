from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
start_button = driver.find_element(By.CSS_SELECTOR, "#start > button")
start_button.click()
dynamic_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
dynamic_text = dynamic_element.text
print("Texto: ", dynamic_text)

driver.quit()









