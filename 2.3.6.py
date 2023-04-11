from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    #go by link
    link_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    link_button.click()

    #go to new tab
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    #find x on page and formula calculation(y)
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # add y to the answer
    add_text = driver.find_element(By.CSS_SELECTOR, "#answer")
    add_text.send_keys(y)

    # click Submit
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    driver.quit()
