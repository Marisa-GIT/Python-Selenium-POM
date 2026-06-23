import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_title",
    [
        ("problem_user", "secret_sauce", "Products"),
        ("invalid_user", "wrong_password", "Epic Error")
    ]
)

def test_login(driver, username, password, expected_title):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if expected_title == "Products":
        title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
        assert title == expected_title, f"Experando:{expected_title}, Obtenido:{title}"
    else:
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert error_message.startswith(expected_title), f"Esperado: {expected_title}, Obtenido: {error_message}"
        


