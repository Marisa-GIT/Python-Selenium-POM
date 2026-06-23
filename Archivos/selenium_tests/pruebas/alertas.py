from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
alert_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
alert_button.click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert_text = alert.text
print("Text: ", alert_text)
time.sleep(3)
alert.accept()

confirm_button = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
confirm_button.click()
alert = driver.switch_to.alert

alert.dismiss() # para hacer clic en cancelar

confirm_prompt = driver.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]')
confirm_prompt.click()
alert = driver.switch_to.alert
alert.send_keys("Texto para la alerta")
alert.accept()

result = driver.find_element(By.ID, "result").text
print("Resultado: ", result)
time.sleep(3)


driver.quit()






