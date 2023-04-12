from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    #go by link
    link_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    link_button.click()

    #click ok on confirm
    confirm = driver.switch_to.alert
    confirm_text = confirm.text
    print(confirm_text)
    confirm.accept()

    #find x on page and formula calculation(y)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    #add y to the answer field and scrolling
    add_text = driver.find_element(By.CSS_SELECTOR, "#answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", add_text)
    add_text.send_keys(y)

    #click Submit
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    driver.quit()
