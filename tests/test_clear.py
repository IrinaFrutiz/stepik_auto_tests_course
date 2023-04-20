import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


login = "i@gmail.com"
pas = "1234"

@pytest.mark.parametrize("URL_part", ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_add_field(browser, URL_part):
    link = f"https://stepik.org/lesson/{URL_part}"
    browser.get(link)
    login_botton = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember33"))
    )
    login_botton.click()
    input_login = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,"id_login_email")))
    input_login.send_keys(login)
    input_pas = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,"id_login_password")))
    input_pas.send_keys(pas)
    log_in_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_form > button")))
    log_in_button.click()
    time.sleep(10)