from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_find = driver.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_find.text)

    y_find = driver.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_find.text)

    summ = str(x+y)
    print(summ)

    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summ)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
