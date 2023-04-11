from selenium import webdriver

driver=webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")

import time
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, first_name)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
