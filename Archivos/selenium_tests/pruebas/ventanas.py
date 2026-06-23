from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/windows")
original_window = driver.current_window_handle
link = driver.find_element(By.LINK_TEXT, "Click Here")
link.click()

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

new_window_text = driver.find_element(By.TAG_NAME, "h3").text
print("Texto de la nueva ventana: ", new_window_text)

driver.switch_to.window(original_window)
original_text = driver.find_element(By.TAG_NAME, "h3").text
print("Texto de la ventana original: ", original_text)
driver.quit()

