from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/dynamic-properties")

visible_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "enableAfter"))
)
visible_button.click()

assert visible_button.is_enabled(), "El boton está habilitado"

driver.quit()


