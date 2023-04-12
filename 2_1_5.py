from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    link = "https://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)

# check autocheck checkbox People rule
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

# check checkbox Robot rule
    robots_radio = driver.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None

# check button Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_checked = submit_button.get_attribute("disabled")
    print("value ot submit button:", submit_checked)
    assert submit_checked is None

    time.sleep(10)
# check didable button Submit after 10s
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_checked = submit_button.get_attribute("disabled")
    print("value ot submit button:", submit_checked)
    assert submit_checked is not None

finally:
    time.sleep(5)
    driver.quit()
