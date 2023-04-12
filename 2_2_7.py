from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)

    #find x on page and formula calculation(y)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    #add y to the answer field and scrolling
    add_text = driver.find_element(By.CSS_SELECTOR, "#answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", add_text)
    add_text.send_keys(y)

    #check I am Robot
    checkbox_I_am_robot = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_I_am_robot.click()

    #check Robots rule
    radiobatton_robot = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobatton_robot.click()

    #click Submit
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
