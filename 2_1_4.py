from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    add_text = driver.find_element(By.CSS_SELECTOR, "#answer")
    add_text.send_keys(y)

    checkbox_I_am_rebot = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_I_am_rebot.click()

    radiobatton_robot = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobatton_robot.click()

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
