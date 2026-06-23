from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/iframe")
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)
editor_body = driver.find_element(By.ID, "tinymce")
editor_body.clear()

editor_body.send_keys("Hola desde selenium")
driver.switch_to.default_content()

title = driver.find_element(By.TAG_NAME, "h3").text
print("Texto:", title)

